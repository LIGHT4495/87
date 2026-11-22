# -*- coding: utf-8 -*-
import asyncio, json, math, os, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
import importlib
P = "#6c4df6"; T = "#0e9488"; C = "#e0344f"; A = "#c26a0e"   # card palette
sys.path.insert(0, os.environ.get("REELS_CONTENT", os.getcwd()))
EPS = importlib.import_module(os.environ['EPMOD']).EPS   # e.g. EPMOD=episodes_josaron
BRAND = os.environ.get('BRAND', '조사리 마을 사건일지')
GROUND = os.environ.get('GROUND', '#fff6e5')
BLOB_A = os.environ.get('BLOB_A', 'rgba(108,77,246,0.22)')
BLOB_B = os.environ.get('BLOB_B', 'rgba(14,148,136,0.2)')

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.environ.get("REELS_WORK", os.path.join(os.getcwd(), "reels_work"))
ASSETS = os.path.join(WORK, "assets_src")          # fonts / gsap / paper.jpg (made by setup.sh)
PROJECT_FILES = os.path.join(HERE, "..", "assets", "project")
SERIES = WORK + "/" + os.environ.get("SERIESDIR", "series")

GAP = 0.45
LEAD = 0.3
TAIL = 2.0


def ep_dir(n):
    return f"{SERIES}/ep{n}"


# ------------------------------------------------------------------ text wrapping for captions
def cw(ch):
    if "가" <= ch <= "힣":
        return 1.0
    if ch.isalnum():
        return 0.58
    if ch in ",.?!·":
        return 0.38
    return 0.3


def tw(s):
    return sum(cw(c) for c in s)


def wrap(text, maxw=16.3):
    words = text.split(" ")
    total = tw(text)
    for k in range(max(1, math.ceil(total / maxw)), 5):
        best = None
        # dp over words: split into k lines minimizing the max width
        n = len(words)
        INF = 1e9
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        cut = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for j in range(1, k + 1):
            for i in range(1, n + 1):
                for m in range(j - 1, i):
                    w = tw(" ".join(words[m:i]))
                    v = max(dp[j - 1][m], w)
                    if v < dp[j][i]:
                        dp[j][i] = v
                        cut[j][i] = m
        if dp[k][n] <= maxw:
            lines = []
            i = n
            for j in range(k, 0, -1):
                m = cut[j][i]
                lines.append(" ".join(words[m:i]))
                i = m
            return "<br>".join(reversed(lines))
    return text


# ------------------------------------------------------------------ TTS
async def tts_all(ns):
    import edge_tts
    proxy = os.environ.get("HTTPS_PROXY")
    sem = asyncio.Semaphore(5)

    async def one(n, i, say):
        d = ep_dir(n) + "/tts"
        os.makedirs(d, exist_ok=True)
        async with sem:
            for attempt in range(3):
                try:
                    await edge_tts.Communicate(say, "ko-KR-SunHiNeural", rate="+0%", pitch="-3Hz", proxy=proxy).save(f"{d}/l{i}.mp3")
                    return
                except Exception as e:  # retry
                    await asyncio.sleep(1.5)
            raise RuntimeError(f"tts failed ep{n} line{i}")

    jobs = []
    for n in ns:
        for i, ln in enumerate(EPS[n]["lines"]):
            jobs.append(one(n, i, ln["say"]))
    await asyncio.gather(*jobs)
    for n in ns:
        info = []
        d = ep_dir(n) + "/tts"
        for i, ln in enumerate(EPS[n]["lines"]):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{d}/l{i}.mp3", "-af",
                            "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse",
                            "-ar", "44100", f"{d}/l{i}.wav"], check=True)
            dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{d}/l{i}.wav"]))
            info.append(dict(i=i, dur=round(dur, 2)))
        t = LEAD
        for x in info:
            x["start"] = round(t, 2)
            t += x["dur"] + GAP
        json.dump(info, open(d + "/info.json", "w"))
        print(f"ep{n}: {len(info)} lines, ends {info[-1]['start'] + info[-1]['dur']:.1f}s")


# ------------------------------------------------------------------ layout helpers
def rows_layout(n, has_header):
    top = 446 if has_header else 380
    H = 1000 - top
    gap = 18 if n >= 4 else 22
    h = min(226, (H - (n - 1) * gap) // n)
    total = n * h + (n - 1) * gap
    y0 = top + (H - total) // 2
    if h >= 200:
        tf, df, av = 56, 38, 112
    elif h >= 160:
        tf, df, av = 48, 34, 100
    else:
        tf, df, av = 42, 33, 86
    return [y0 + i * (h + gap) for i in range(n)], h, tf, df, av


def esc_hl(s):
    return s.replace("[[", '<span class="hl">').replace("]]", "</span>")


CSS = r"""
      @font-face { font-family: "RDisplay"; src: url("assets/fonts/display-ko.woff2") format("woff2"); unicode-range: U+1100-11FF, U+3130-318F, U+AC00-D7AF; }
      @font-face { font-family: "RDisplay"; src: url("assets/fonts/display-latin.woff2") format("woff2"); unicode-range: U+0000-00FF, U+2000-206F; }
      @font-face { font-family: "RBody"; src: url("assets/fonts/body-ko.woff2") format("woff2"); font-weight: 700; unicode-range: U+1100-11FF, U+3130-318F, U+AC00-D7AF; }
      @font-face { font-family: "RBody"; src: url("assets/fonts/body-latin.woff2") format("woff2"); font-weight: 700; unicode-range: U+0000-00FF, U+2000-206F; }
      :root { --ground:#fff6e5; --ink:#2b2a4c; --purple:#6c4df6; --teal:#0e9488; --coral:#e0344f; --amber:#c26a0e; --yellow:#ffc93c; --font-display:"RDisplay","RBody",sans-serif; --font-body:"RBody",sans-serif; }
      * { margin:0; padding:0; box-sizing:border-box; }
      html, body { width:1080px; height:1920px; overflow:hidden; background:var(--ground); }
      #root { position:relative; width:1080px; height:1920px; overflow:hidden; background:var(--ground); font-family:var(--font-body); color:var(--ink); }
      .full { position:absolute; left:0; top:0; width:1080px; height:1920px; }
      .abs { position:absolute; }
      .blob { position:absolute; border-radius:50%; filter:blur(80px); }
      svg { overflow:visible; }
      #hud { position:absolute; left:120px; top:296px; width:780px; display:flex; justify-content:center; }
      #hud .tag { background:var(--ink); color:#fff; font-size:32px; padding:10px 30px; border-radius:40px; }
      .cap { position:absolute; left:120px; width:780px; bottom:680px; display:flex; justify-content:center; }
      .cap div { background:var(--ink); color:#fff; font-size:42px; line-height:1.36; text-align:center; padding:22px 30px; border-radius:28px; box-shadow:0 12px 26px rgba(43,42,76,0.25); }
      .hook-sub { position:absolute; left:120px; top:372px; width:780px; text-align:center; font-size:34px; color:var(--purple); }
      .hook-title { position:absolute; left:120px; top:430px; width:780px; text-align:center; font-family:var(--font-display); line-height:1.08; }
      .hook-title span { display:block; }
      .hook-title .vs { font-size:80px; color:var(--coral); margin:4px 0; }
      .hdr { position:absolute; left:120px; top:368px; width:780px; display:flex; justify-content:center; }
      .hdr div { background:var(--yellow); color:var(--ink); font-size:34px; padding:8px 28px; border-radius:30px; }
      .crow { position:absolute; left:120px; width:780px; border-radius:30px; display:flex; align-items:center; gap:20px; padding:0 22px; color:#fff; }
      .crow .av { flex:none; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; }
      .crow .tx { flex:1; min-width:0; }
      .crow .tt { font-family:var(--font-display); font-weight:400; line-height:1.12; }
      .crow .ds { line-height:1.28; }
      .crow .mk { flex:none; width:64px; height:64px; border-radius:50%; background:#fff; display:flex; align-items:center; justify-content:center; }
      .crow .mk svg { width:40px; height:40px; }
      .qtag { position:absolute; left:120px; top:392px; background:var(--yellow); color:var(--ink); font-size:32px; padding:10px 26px; border-radius:30px; }
      .card { position:absolute; left:120px; top:470px; width:780px; background:#fff; border-radius:36px; padding:50px 44px 56px; box-shadow:0 26px 60px rgba(43,42,76,0.2); font-size:50px; line-height:1.42; }
      .hl { background:linear-gradient(transparent 62%, rgba(255,201,60,0.75) 62%); }
      .stamp { position:absolute; right:24px; bottom:-84px; border:12px solid; font-family:var(--font-display); font-size:108px; padding:2px 30px; border-radius:22px; background:rgba(255,255,255,0.92); white-space:nowrap; }
      .cq { position:absolute; left:120px; top:390px; width:780px; background:#fff; border-radius:36px; padding:44px 30px; text-align:center; box-shadow:0 26px 60px rgba(43,42,76,0.2); }
      .cq .t { font-family:var(--font-display); font-size:84px; color:var(--ink); line-height:1.15; }
      .cq .btns { display:flex; gap:24px; justify-content:center; margin-top:30px; }
      .cq .btn { font-size:44px; color:#fff; padding:18px 36px; border-radius:60px; white-space:nowrap; }
      .chint { position:absolute; left:120px; top:745px; width:780px; text-align:center; font-size:40px; color:var(--purple); }
"""

DEFS = r"""
    <svg width="0" height="0" style="position:absolute">
      <defs>
        <g id="critterBody">
          <circle cx="-62" cy="-92" r="30" style="fill:var(--c)"></circle>
          <circle cx="62" cy="-92" r="30" style="fill:var(--c)"></circle>
          <circle cx="-62" cy="-92" r="15" fill="rgba(255,255,255,0.55)"></circle>
          <circle cx="62" cy="-92" r="15" fill="rgba(255,255,255,0.55)"></circle>
          <ellipse cx="-42" cy="92" rx="30" ry="15" style="fill:var(--c)"></ellipse>
          <ellipse cx="42" cy="92" rx="30" ry="15" style="fill:var(--c)"></ellipse>
          <ellipse cx="0" cy="0" rx="100" ry="92" style="fill:var(--c)"></ellipse>
          <ellipse cx="0" cy="34" rx="60" ry="46" fill="rgba(255,255,255,0.6)"></ellipse>
          <circle cx="-34" cy="-14" r="11" fill="#2b2a4c"></circle>
          <circle cx="34" cy="-14" r="11" fill="#2b2a4c"></circle>
          <circle cx="-30" cy="-18" r="4" fill="#fff"></circle>
          <circle cx="38" cy="-18" r="4" fill="#fff"></circle>
          <circle cx="-62" cy="14" r="13" fill="#ff9aa8" opacity="0.75"></circle>
          <circle cx="62" cy="14" r="13" fill="#ff9aa8" opacity="0.75"></circle>
          <path d="M -13 12 Q 0 26 13 12" stroke="#2b2a4c" stroke-width="5" fill="none" stroke-linecap="round"></path>
          <path d="M -92 -42 Q 0 -78 92 -42" stroke="var(--hb)" stroke-width="16" fill="none" stroke-linecap="round"></path>
        </g>
        <g id="tail">
          <path d="M -70 40 C -190 30 -200 -150 -100 -190 C -150 -90 -110 -40 -70 -30 Z" fill="#e07a2f"></path>
          <path d="M -100 10 C -160 0 -165 -110 -110 -150" stroke="#f4b266" stroke-width="12" fill="none" stroke-linecap="round"></path>
        </g>
      </defs>
    </svg>
"""

HOST = ('<svg id="{id}" class="abs" style="left:210px; top:{top}px;" width="600" height="300" viewBox="0 0 600 300">'
        '<g transform="translate(300 150) scale({sc})"><use href="#tail"></use>'
        '<use href="#critterBody" style="--c:#f59e42; --hb:#ffc93c"></use></g></svg>')

MARK_O = '<div class="mk"><svg viewBox="0 0 24 24"><path d="M4 12l5 5L20 6" stroke="{c}" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>'
MARK_X = '<div class="mk"><svg viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19" stroke="{c}" stroke-width="3.5" fill="none" stroke-linecap="round"></path></svg></div>'


def build(n):
    ep = EPS[n]
    d = ep_dir(n)
    info = json.load(open(d + "/tts/info.json"))
    lines = ep["lines"]
    st = [x["start"] for x in info]
    en = [round(x["start"] + x["dur"], 2) for x in info]
    total = round(en[-1] + TAIL, 2)
    scenes = ep["scenes"]
    # scene time ranges
    rng = []
    for k, sc in enumerate(scenes):
        a, b = sc["lines"][0], sc["lines"][-1]
        t0 = 0.0 if k == 0 else round(st[a] - 0.1, 2)
        t1 = total if k == len(scenes) - 1 else round(en[b] + 0.35, 2)
        rng.append((t0, t1))

    html_scenes = []
    js = []
    tid = 2  # track index for scenes
    for k, sc in enumerate(scenes):
        t0, t1 = rng[k]
        sid = f"sc{k}"
        dur = round(t1 - t0, 2)
        head = f'<div id="{sid}" class="clip full" data-start="{t0}" data-duration="{dur}" data-track-index="{tid}">'
        exit_js = f'tl.to("#{sid} > *", {{ opacity: 0, duration: 0.22 }}, {round(t1 - 0.27, 2)});' if k < len(scenes) - 1 else ""
        if sc["type"] == "hook":
            words = sc["words"]
            cnt = len(words)
            base = {2: 150, 3: 112, 4: 90}[cnt]
            maxlen = max(len(w) for w in words)
            fs = min(base, int(740 / (maxlen * 0.98)))
            cols = [P, T, C, A]
            parts = []
            for i, w in enumerate(words):
                if i > 0 and sc["joiner"]:
                    parts.append(f'<span class="vs">{sc["joiner"]}</span>')
                parts.append(f'<span class="w w{i}" style="font-size:{fs}px; color:{cols[i % 4]};">{w}</span>')
            body = (f'<div class="hook-sub" id="{sid}sub">{sc["sub"]}</div>'
                    f'<div class="hook-title">{"".join(parts)}</div>'
                    + HOST.format(id=sid + "host", top=840, sc=0.6))
            html_scenes.append(head + body + "</div>")
            js.append(f'tl.from("#{sid}sub", {{ opacity: 0, y: -20, duration: 0.4 }}, 0);')
            for i in range(cnt):
                js.append(f'tl.from("#{sid} .w{i}", {{ opacity: 0, scale: 0.6, duration: 0.5, ease: "back.out(1.8)" }}, {round(0.0 + i * 0.25, 2)});')
            if sc["joiner"]:
                js.append(f'tl.from("#{sid} .vs", {{ opacity: 0, scale: 2, duration: 0.4, ease: "power3.out" }}, 0.35);')
            js.append(f'tl.from("#{sid}host", {{ y: 80, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }}, 0.9);')
            js.append(f'tl.to("#{sid}host", {{ y: -14, duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 3 }}, 1.5);')
            js.append(exit_js)
        elif sc["type"] == "cards":
            rows = sc["rows"]
            ys, h, tf, df, av = rows_layout(len(rows), bool(sc.get("header")))
            body = ""
            if sc.get("header"):
                body += f'<div class="hdr" id="{sid}hdr"><div>{sc["header"]}</div></div>'
            for i, r in enumerate(rows):
                col = r["color"]
                mark = ""
                if r.get("mark") == "o":
                    mark = MARK_O.format(c=col)
                elif r.get("mark") == "x":
                    mark = MARK_X.format(c=col)
                avs = int(av * 0.78)
                body += (f'<div id="{sid}r{i}" class="crow" style="top:{ys[i]}px; height:{h}px; background:{col};">'
                         f'<div class="av" style="width:{av}px; height:{av}px;"><svg viewBox="-125 -135 250 270" width="{avs}" height="{int(avs * 1.08)}">'
                         f'<use href="#critterBody" style="--c:{col}; --hb:#ffc93c"></use></svg></div>'
                         f'<div class="tx"><div class="tt" style="font-size:{tf}px;">{r["title"]}</div><div class="ds" style="font-size:{df}px;">{r["desc"]}</div></div>{mark}</div>')
            html_scenes.append(head + body + "</div>")
            if sc.get("header"):
                js.append(f'tl.from("#{sid}hdr", {{ opacity: 0, y: -24, duration: 0.4, ease: "back.out(1.6)" }}, {round(t0 + 0.15, 2)});')
            for i, r in enumerate(rows):
                tt = round(st[r["line"]] + 0.05 + (0.18 if rows[i - 1]["line"] == r["line"] and i > 0 else 0), 2)
                x = -80 if i % 2 == 0 else 80
                js.append(f'tl.from("#{sid}r{i}", {{ opacity: 0, x: {x}, duration: 0.5, ease: "power3.out" }}, {tt});')
            js.append(exit_js)
        elif sc["type"] == "exam":
            stamp = f'<div class="stamp" id="{sid}stamp" style="color:{sc["stamp_color"]}; border-color:{sc["stamp_color"]};">{sc["stamp"]}</div>'
            body = (f'<div class="qtag" id="{sid}tag">{sc["tag"]}</div>'
                    f'<div class="card" id="{sid}card">“{esc_hl(sc["html"])}”{stamp}</div>')
            html_scenes.append(head + body + "</div>")
            js.append(f'tl.from("#{sid}tag", {{ opacity: 0, y: -30, duration: 0.4, ease: "power3.out" }}, {round(t0 + 0.1, 2)});')
            js.append(f'tl.from("#{sid}card", {{ opacity: 0, y: 80, scale: 0.92, duration: 0.55, ease: "back.out(1.5)" }}, {round(t0 + 0.2, 2)});')
            sl = sc["stamp_line"]
            ts = round(st[sl] + info[sl]["dur"] * sc["stamp_frac"], 2)
            js.append(f'tl.fromTo("#{sid}stamp", {{ opacity: 0, scale: 1.6, rotation: -16, transformOrigin: "100% 60%" }}, {{ opacity: 1, scale: 1, rotation: -10, transformOrigin: "100% 60%", duration: 0.35, ease: "power4.in" }}, {ts});')
            js.append(f'tl.to("#{sid}card", {{ x: 8, duration: 0.05, yoyo: true, repeat: 3 }}, {round(ts + 0.35, 2)});')
            js.append(exit_js)
        elif sc["type"] == "cta":
            btns = "".join(f'<div class="btn" style="background:{c};">{t}</div>' for t, c in sc["buttons"])
            qfs = min(84, int(700 / max(1.0, tw(sc["q"]))))
            body = (f'<div class="cq" id="{sid}q"><div class="t" style="font-size:{qfs}px;">{sc["q"]}</div><div class="btns">{btns}</div></div>'
                    f'<div class="chint" id="{sid}hint">{sc["hint"]}</div>'
                    + HOST.format(id=sid + "host", top=775, sc=0.62))
            html_scenes.append(head + body + "</div>")
            js.append(f'tl.from("#{sid}q", {{ opacity: 0, y: 70, scale: 0.94, duration: 0.55, ease: "back.out(1.5)" }}, {round(t0 + 0.2, 2)});')
            js.append(f'tl.from("#{sid} .btn", {{ opacity: 0, scale: 0.6, duration: 0.4, ease: "back.out(2)", stagger: 0.25 }}, {round(t0 + 1.4, 2)});')
            hint_t = round(max(t0 + 2.0, min(t0 + 3.4, total - 2.6)), 2)
            js.append(f'tl.from("#{sid}hint", {{ opacity: 0, y: 20, duration: 0.4 }}, {hint_t});')
            js.append(f'tl.from("#{sid}host", {{ y: 90, opacity: 0, duration: 0.5, ease: "back.out(1.6)" }}, {round(t0 + 0.8, 2)});')
            js.append(f'tl.to("#{sid}host", {{ y: -12, duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: 5 }}, {round(t0 + 1.6, 2)});')

    # captions
    caps = ""
    capjs = []
    for i, ln in enumerate(lines):
        text = ln.get("cap", ln["say"])
        c0 = round(st[i] - 0.05, 2)
        cd = round(info[i]["dur"] + 0.1, 2)
        caps += f'      <div class="clip cap" id="c{i}" data-start="{c0}" data-duration="{cd}" data-track-index="3"><div>{wrap(text)}</div></div>\n'
        capjs.append(f'tl.from("#c{i} div", {{ opacity: 0, y: 30, duration: 0.3, ease: "power3.out" }}, {c0});')
        if i < len(lines) - 1:
            capjs.append(f'tl.to("#c{i} div", {{ opacity: 0, duration: 0.2 }}, {round(c0 + cd - 0.2, 2)});')

    html = f"""<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/gsap.min.js"></script>
    <style>{CSS.replace("#fff6e5", GROUND)}</style>
  </head>
  <body>
{DEFS}
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      <div id="bg" class="clip full" data-start="0" data-duration="{total}" data-track-index="0">
        <div class="blob" id="blob-a" style="left:-140px; top:360px; width:560px; height:560px; background:{BLOB_A};"></div>
        <div class="blob" id="blob-b" style="left:620px; top:1050px; width:600px; height:600px; background:{BLOB_B};"></div>
      </div>
      <div id="hud" class="clip" data-start="0" data-duration="{total}" data-track-index="1"><div class="tag">{BRAND} · EP.{n}</div></div>
      {chr(10).join("      " + s for s in html_scenes).strip()}
      <audio id="mix" class="clip" src="assets/mix.wav" data-start="0" data-duration="{total}" data-track-index="9"></audio>
{caps}    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.to("#blob-a", {{ x: 120, y: 80, duration: {total}, ease: "none" }}, 0);
      tl.to("#blob-b", {{ x: -120, y: -80, duration: {total}, ease: "none" }}, 0);
      {chr(10).join("      " + s for s in capjs).strip()}
      {chr(10).join("      " + s for s in js).strip()}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""
    os.makedirs(d + "/assets/fonts", exist_ok=True)
    for f in ("display-ko.woff2", "display-latin.woff2", "body-ko.woff2", "body-latin.woff2"):
        shutil.copy(f"{ASSETS}/fonts/{f}", f"{d}/assets/fonts/{f}")
    shutil.copy(ASSETS + "/gsap.min.js", d + "/assets/gsap.min.js")
    for f in ("hyperframes.json", "meta.json", "package.json"):
        shutil.copy(f"{PROJECT_FILES}/{f}", f"{d}/{f}")
    open(d + "/index.html", "w", encoding="utf-8").write(html)
    json.dump(dict(total=total, starts=st, ends=en), open(d + "/timing.json", "w"))
    print(f"ep{n}: html ok, total {total}s, scenes {len(scenes)}")


def audio(n):
    ep = EPS[n]
    d = ep_dir(n)
    t = json.load(open(d + "/timing.json"))
    total = t["total"]
    info = json.load(open(d + "/tts/info.json"))
    ins, fl, lab = [], [], []
    for k, x in enumerate(info):
        ins += ["-i", f"{d}/tts/l{x['i']}.wav"]
        ms = int(x["start"] * 1000)
        fl.append(f"[{k}:a]adelay={ms}|{ms}[n{k}]")
        lab.append(f"[n{k}]")
    fl.append("".join(lab) + f"amix=inputs={len(info)}:duration=longest:normalize=0[nar]")
    open(d + "/nar_filter.txt", "w").write(";\n".join(fl))
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex_script", d + "/nar_filter.txt", "-map", "[nar]", "-ar", "44100", "-ac", "1", d + "/narration.wav"], check=True)
    bpm, prog, seed = ep["music"]
    subprocess.run([sys.executable, "-I", HERE + "/music.py", d + "/music.wav", str(total + 0.5), str(bpm), str(prog), str(seed)], check=True)
    subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-i", d + "/music.wav", "-i", d + "/narration.wav", "-filter_complex",
                    "[1:a]volume=1.5,asplit=2[n1][n2];"
                    "[0:a]volume='if(lt(t,0.3),0.5,0.2)':eval=frame[mus];"
                    "[mus][n1]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=500[duck];"
                    f"[duck][n2]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.93,apad=whole_dur={total},atrim=0:{total},afade=t=out:st={total - 2}:d=2[a]",
                    "-map", "[a]", "-ar", "44100", d + "/assets/mix.wav"], check=True)
    print(f"ep{n}: audio ok")


if __name__ == "__main__":
    cmd = sys.argv[1]
    ns = [int(x) for x in sys.argv[2:]] or sorted(EPS)
    if cmd == "tts":
        asyncio.run(tts_all(ns))
    elif cmd == "html":
        for n in ns:
            build(n)
    elif cmd == "audio":
        for n in ns:
            audio(n)
