# -*- coding: utf-8 -*-
# Paper / orange motion style engine (reference-inspired). Reuses tts + audio from build_ep.
import json, math, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_ep as B
from build_ep import tw, wrap, ep_dir, EPS, TAIL

PAPER = B.ASSETS + "/" + os.environ.get("PAPER_FILE", "paper.jpg")   # e.g. paper_pink.jpg
CHARACTER = os.environ.get("CHARACTER", "swing")                      # swing | cat
BRAND = os.environ.get("BRAND", "사회복지실천론")
ORANGE = "#dc480e"      # fills
ORANGE_T = "#c43d08"    # text accent on paper
INK = "#141414"

CSS = r"""
      @font-face { font-family:"RBlack"; font-weight:900; src:url("assets/fonts/black-ko.woff2") format("woff2"); unicode-range:U+1100-11FF,U+3130-318F,U+AC00-D7AF; }
      @font-face { font-family:"RBlack"; font-weight:900; src:url("assets/fonts/black-latin.woff2") format("woff2"); unicode-range:U+0000-00FF,U+2000-206F; }
      @font-face { font-family:"RBody"; font-weight:700; src:url("assets/fonts/body-ko.woff2") format("woff2"); unicode-range:U+1100-11FF,U+3130-318F,U+AC00-D7AF; }
      @font-face { font-family:"RBody"; font-weight:700; src:url("assets/fonts/body-latin.woff2") format("woff2"); unicode-range:U+0000-00FF,U+2000-206F; }
      :root { --ink:#141414; --orange:#dc480e; --orange-t:#c43d08; --paper:#d4e6cc; --font-black:"RBlack","RBody",sans-serif; --font-body:"RBody",sans-serif; }
      * { margin:0; padding:0; box-sizing:border-box; }
      html, body { width:1080px; height:1920px; overflow:hidden; background:#d4e6cc; }
      #root { position:relative; width:1080px; height:1920px; overflow:hidden; background:#d4e6cc url("assets/paper.jpg") 0px 0px/1180px 2100px no-repeat; font-family:var(--font-body); color:var(--ink); }
      .full { position:absolute; left:0; top:0; width:1080px; height:1920px; }
      .abs { position:absolute; }
      svg { overflow:visible; }
      #hud { position:absolute; left:120px; top:292px; width:780px; display:flex; justify-content:center; }
      #hud .tag { background:var(--orange); color:#fff; font-size:30px; padding:8px 26px; border-radius:30px; letter-spacing:0.02em; }
      .cap { position:absolute; left:120px; width:780px; bottom:680px; display:flex; justify-content:center; }
      .cap div { background:var(--ink); color:#fff; font-size:42px; line-height:1.36; text-align:center; padding:22px 30px; border-radius:26px; box-shadow:0 12px 26px rgba(0,0,0,0.28); }
      .hl2 { position:absolute; left:120px; top:352px; width:780px; text-align:center; font-family:var(--font-black); font-weight:900; font-size:54px; line-height:1.2; letter-spacing:-0.02em; color:var(--ink); }
      .hl2.big { font-size:64px; }
      .hl2 .ac { color:var(--orange-t); }
      .panel { position:absolute; left:120px; top:506px; width:780px; border-radius:34px; padding:22px; background:rgba(255,255,255,0.42); border:1.5px solid rgba(255,255,255,0.7); box-shadow:0 18px 40px rgba(40,60,40,0.18); display:flex; flex-direction:column; gap:12px; }
      .row { background:#fff; border-radius:26px; display:flex; align-items:center; gap:16px; padding:0 16px; box-shadow:0 4px 12px rgba(0,0,0,0.08); }
      .row .bd { flex:none; border-radius:50%; background:var(--orange); color:#fff; font-family:var(--font-black); font-weight:900; display:flex; align-items:center; justify-content:center; }
      .row .tx { flex:1; min-width:0; }
      .row .tt { font-family:var(--font-black); font-weight:900; color:var(--ink); line-height:1.15; letter-spacing:-0.01em; }
      .row .ds { font-weight:700; color:#4a4a44; line-height:1.28; }
      .row .mk { flex:none; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
      .row .mk svg { width:34px; height:34px; }
      .row .mk.o { background:var(--ink); } .row .mk.x { background:var(--orange); }
      .dpanel { position:absolute; left:120px; top:506px; width:780px; background:#141414; border-radius:34px; padding:22px; box-shadow:0 22px 44px rgba(0,0,0,0.3); }
      .etag { color:#ffa070; font-size:30px; margin:2px 4px 14px; }
      .ecard { background:#f5f0e3; border-radius:24px; padding:30px 24px; font-family:var(--font-black); font-weight:900; font-size:46px; line-height:1.36; text-align:center; color:var(--ink); letter-spacing:-0.01em; }
      .ecard .hlt { background:linear-gradient(transparent 60%, rgba(242,86,26,0.38) 60%); }
      .stamp { position:absolute; right:16px; bottom:-70px; border:9px solid; border-radius:18px; font-family:var(--font-black); font-weight:900; font-size:80px; padding:0 24px; background:rgba(255,255,255,0.94); white-space:nowrap; line-height:1.25; }
      .cq { text-align:center; color:#fff; font-family:var(--font-black); font-weight:900; line-height:1.2; letter-spacing:-0.02em; }
      .btns { display:flex; gap:20px; justify-content:center; margin-top:20px; }
      .btn { font-family:var(--font-black); font-weight:900; font-size:44px; padding:14px 34px; border-radius:50px; white-space:nowrap; }
      .btn.a { background:var(--orange); color:#fff; } .btn.b { background:#f5f0e3; color:var(--ink); }
"""

DEFS = r"""
    <svg width="0" height="0" style="position:absolute">
      <defs>
        <radialGradient id="ballG" cx="0.35" cy="0.3" r="0.85"><stop offset="0" stop-color="#ffb877"/><stop offset="0.5" stop-color="#ff6a1f"/><stop offset="1" stop-color="#bf3a04"/></radialGradient>
        <g id="girl">
          <circle r="105" fill="url(#ballG)"></circle>
          <ellipse cx="-42" cy="-50" rx="34" ry="19" fill="#fff" opacity="0.32" transform="rotate(-32 -42 -50)"></ellipse>
          <path d="M -22 -92 L -62 -48 L -76 -6" stroke="#2f2b2a" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" fill="none"></path>
          <path d="M 26 -90 L 66 -44 L 82 -2" stroke="#2f2b2a" stroke-width="36" stroke-linecap="round" stroke-linejoin="round" fill="none"></path>
          <ellipse cx="-80" cy="4" rx="28" ry="15" fill="#fff"></ellipse>
          <path d="M -106 12 Q -80 24 -52 12" stroke="#ff6a1f" stroke-width="7" fill="none" stroke-linecap="round"></path>
          <ellipse cx="88" cy="8" rx="28" ry="15" fill="#fff"></ellipse>
          <path d="M 62 16 Q 88 28 116 16" stroke="#ff6a1f" stroke-width="7" fill="none" stroke-linecap="round"></path>
          <rect x="-54" y="-198" width="108" height="118" rx="44" fill="#f2e4d0"></rect>
          <path d="M -26 -146 q 7 -11 14 0 q 7 -11 14 0 q 0 11 -14 22 q -14 -11 -14 -22z" fill="#ff6a1f"></path>
          <path d="M -44 -170 Q -80 -140 -58 -108" stroke="#f2e4d0" stroke-width="28" stroke-linecap="round" fill="none"></path>
          <circle cx="-54" cy="-100" r="14" fill="#f9dcc4"></circle>
          <path d="M 46 -172 Q 84 -215 78 -288" stroke="#f2e4d0" stroke-width="28" stroke-linecap="round" fill="none"></path>
          <circle cx="78" cy="-300" r="15" fill="#f9dcc4"></circle>
          <circle cx="0" cy="-262" r="66" fill="#3a2418"></circle>
          <path d="M -66 -262 Q -78 -205 -52 -188 L 52 -188 Q 78 -205 66 -262 Z" fill="#3a2418"></path>
          <ellipse cx="0" cy="-248" rx="54" ry="56" fill="#f9dcc4"></ellipse>
          <path d="M -54 -272 Q -20 -302 0 -284 Q 24 -304 54 -272 L 54 -300 L -54 -300 Z" fill="#3a2418"></path>
          <path d="M -66 -276 Q -66 -354 0 -354 Q 66 -354 66 -276 Z" fill="#ff6a1f"></path>
          <rect x="-69" y="-292" width="138" height="30" rx="15" fill="#ff8a3d"></rect>
          <ellipse cx="-21" cy="-238" rx="8" ry="11" fill="#2a1a12"></ellipse>
          <ellipse cx="21" cy="-238" rx="8" ry="11" fill="#2a1a12"></ellipse>
          <circle cx="-18" cy="-242" r="3" fill="#fff"></circle>
          <circle cx="24" cy="-242" r="3" fill="#fff"></circle>
          <circle cx="-37" cy="-220" r="9" fill="#ff9aa2" opacity="0.65"></circle>
          <circle cx="37" cy="-220" r="9" fill="#ff9aa2" opacity="0.65"></circle>
          <path d="M -9 -216 Q 0 -205 9 -216" stroke="#7a3b2a" stroke-width="4" fill="none" stroke-linecap="round"></path>
        </g>
      </defs>
    </svg>
"""

CHECK = '<svg viewBox="0 0 24 24"><path d="M4 12l5 5L20 6" stroke="#fff" stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
CROSS = '<svg viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19" stroke="#fff" stroke-width="3.6" fill="none" stroke-linecap="round"></path></svg>'


def esc_ac(s):
    return s.replace("[[", '<span class="ac">').replace("]]", "</span>")


def esc_hl(s):
    return s.replace("[[", '<span class="hlt">').replace("]]", "</span>")


def pend(sid, cx, cy, s):
    hx = round(cx + 78 * s, 1)
    hy = round(cy - 300 * s, 1)
    svg = (f'<svg id="{sid}p" class="full" viewBox="0 0 1080 1920" width="1080" height="1920"><g id="{sid}W"><g id="{sid}G">'
           f'<line x1="{hx}" y1="-60" x2="{hx}" y2="{hy}" stroke="#1d1d1d" stroke-width="3.5"></line>'
           f'<g transform="translate({cx} {cy}) scale({s})"><use href="#girl"></use></g></g></g></svg>')
    return svg, hx


def cat_markup(sid, cx, by, s):
    """Glasses cat on a stack of books. Returns (svg, global coords for animation origins)."""
    g = lambda x, y: (x, y)   # GSAP svgOrigin is read in the (scaled) parent group's LOCAL units
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <rect x="-150" y="-54" width="300" height="54" rx="12" fill="#2a2a2a"></rect><rect x="-150" y="-36" width="300" height="8" fill="#f2561a"></rect>
  <rect x="-135" y="-104" width="270" height="50" rx="12" fill="#f2561a"></rect><rect x="-135" y="-82" width="270" height="7" fill="#f5f0e3" opacity="0.85"></rect>
  <rect x="-118" y="-150" width="236" height="46" rx="12" fill="#f5f0e3"></rect><rect x="-118" y="-128" width="236" height="6" fill="#d9cfb8"></rect>
  <g id="{sid}C">
    <path id="{sid}T" d="M 60 -175 C 132 -170 172 -215 150 -282" stroke="#ff9a3d" stroke-width="30" fill="none" stroke-linecap="round"></path>
    <ellipse cx="0" cy="-215" rx="78" ry="72" fill="#ff9a3d"></ellipse>
    <ellipse cx="0" cy="-205" rx="48" ry="52" fill="#fff3e2"></ellipse>
    <ellipse cx="-52" cy="-158" rx="30" ry="14" fill="#ff9a3d"></ellipse><ellipse cx="52" cy="-158" rx="30" ry="14" fill="#ff9a3d"></ellipse>
    <ellipse cx="-22" cy="-157" rx="22" ry="12" fill="#fff3e2"></ellipse><ellipse cx="22" cy="-157" rx="22" ry="12" fill="#fff3e2"></ellipse>
    <path d="M -66 -352 L -54 -424 L -12 -380 Z" fill="#ff9a3d"></path><path d="M -56 -362 L -49 -402 L -26 -378 Z" fill="#ffb3c1"></path>
    <path d="M 66 -352 L 54 -424 L 12 -380 Z" fill="#ff9a3d"></path><path d="M 56 -362 L 49 -402 L 26 -378 Z" fill="#ffb3c1"></path>
    <circle cx="0" cy="-318" r="74" fill="#ff9a3d"></circle>
    <path d="M -14 -384 v 18 M 0 -388 v 22 M 14 -384 v 18" stroke="#e07a1f" stroke-width="7" stroke-linecap="round" fill="none"></path>
    <circle cx="-48" cy="-296" r="11" fill="#ff9aa2" opacity="0.6"></circle><circle cx="48" cy="-296" r="11" fill="#ff9aa2" opacity="0.6"></circle>
    <g id="{sid}E"><ellipse cx="-26" cy="-322" rx="9" ry="12" fill="#2a1a12"></ellipse><ellipse cx="26" cy="-322" rx="9" ry="12" fill="#2a1a12"></ellipse>
      <circle cx="-23" cy="-326" r="3" fill="#fff"></circle><circle cx="29" cy="-326" r="3" fill="#fff"></circle></g>
    <circle cx="-26" cy="-322" r="21" fill="none" stroke="#2a2a2a" stroke-width="5"></circle><circle cx="26" cy="-322" r="21" fill="none" stroke="#2a2a2a" stroke-width="5"></circle>
    <path d="M -5 -322 h 10" stroke="#2a2a2a" stroke-width="5"></path>
    <path d="M -7 -300 h 14 l -7 9 z" fill="#ff7b95"></path>
    <path d="M -12 -288 Q -6 -280 0 -290 Q 6 -280 12 -288" stroke="#7a3b2a" stroke-width="4" fill="none" stroke-linecap="round"></path>
    <path d="M -44 -296 L -104 -306 M -44 -288 L -102 -284 M 44 -296 L 104 -306 M 44 -288 L 102 -284" stroke="#7a3b2a" stroke-width="3" stroke-linecap="round"></path>
    <g id="{sid}P"><path d="M 62 -245 Q 102 -262 110 -320" stroke="#ff9a3d" stroke-width="30" stroke-linecap="round" fill="none"></path>
    <circle cx="110" cy="-328" r="17" fill="#fff3e2"></circle></g>
  </g>
</g>"""
    svg = f'<svg id="{sid}p" class="full" viewBox="0 0 1080 1920" width="1080" height="1920"><g id="{sid}W">{parts}</g></svg>'
    return svg, dict(tail=g(60, -175), paw=g(62, -245), eye=g(0, -322))


def cat_js(sid, meta, t0, dur):
    out = []
    reps = max(1, math.ceil(dur / 0.9) - 1)
    out.append(f'tl.fromTo("#{sid}C", {{ y: 0 }}, {{ y: -9, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: {reps} }}, {t0});')
    tx, ty = meta["tail"]
    out.append(f'tl.fromTo("#{sid}T", {{ rotation: -9, svgOrigin: "{tx} {ty}" }}, {{ rotation: 11, svgOrigin: "{tx} {ty}", duration: 0.7, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / 0.7) - 1)} }}, {t0});')
    px, py = meta["paw"]
    out.append(f'tl.fromTo("#{sid}P", {{ rotation: -16, svgOrigin: "{px} {py}" }}, {{ rotation: 12, svgOrigin: "{px} {py}", duration: 0.55, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / 0.55) - 1)} }}, {t0});')
    ex, ey = meta["eye"]
    t = t0 + 1.8
    while t < t0 + dur - 0.3:
        out.append(f'tl.to("#{sid}E", {{ scaleY: 0.1, svgOrigin: "{ex} {ey}", duration: 0.07, yoyo: true, repeat: 1 }}, {round(t, 2)});')
        t += 2.6
    return out


def build(n):
    ep = EPS[n]
    d = ep_dir(n)
    info = json.load(open(d + "/tts/info.json"))
    lines = ep["lines"]
    st = [x["start"] for x in info]
    en = [round(x["start"] + x["dur"], 2) for x in info]
    total = round(en[-1] + TAIL, 2)
    scenes = ep["scenes"]
    rng = []
    for k, sc in enumerate(scenes):
        a, b = sc["lines"][0], sc["lines"][-1]
        t0 = 0.0 if k == 0 else round(st[a] - 0.1, 2)
        t1 = total if k == len(scenes) - 1 else round(en[b] + 0.35, 2)
        rng.append((t0, t1))

    html_scenes, js = [], []
    for k, sc in enumerate(scenes):
        t0, t1 = rng[k]
        sid = f"sc{k}"
        dur = round(t1 - t0, 2)
        head = f'<div id="{sid}" class="clip full" data-start="{t0}" data-duration="{dur}" data-track-index="2">'
        exit_js = f'tl.to("#{sid} > *", {{ opacity: 0, duration: 0.22 }}, {round(t1 - 0.27, 2)});' if k < len(scenes) - 1 else ""
        hl = f'<div class="hl2{" big" if sc["type"] == "hook" else ""}" id="{sid}h">{esc_ac(sc["headline"])}</div>'
        if sc["type"] == "hook":
            js.append(f'tl.from("#{sid}h", {{ scale: 0.86, y: 24, duration: 0.55, ease: "back.out(1.7)" }}, 0);')
            if CHARACTER == "cat":
                svg, meta = cat_markup(sid, 540, 1015, 0.92)
                html_scenes.append(head + svg + hl + "</div>")
                js.extend(cat_js(sid, meta, 0, dur))
            else:
                svg, hx = pend(sid, 540, 900, 1.15)
                html_scenes.append(head + svg + hl + "</div>")
                reps = max(1, math.ceil(dur / 1.7) - 1)
                js.append(f'tl.fromTo("#{sid}G", {{ rotation: -7, svgOrigin: "{hx} -60" }}, {{ rotation: 7, svgOrigin: "{hx} -60", duration: 1.7, ease: "sine.inOut", yoyo: true, repeat: {reps} }}, 0);')
            js.append(exit_js)
        elif sc["type"] == "cards":
            rows = sc["rows"]
            nrow = len(rows)
            gap = 12
            avail = 460
            h = min(200, (avail - (nrow - 1) * gap) // nrow)
            two = any("<br>" in r["desc"] for r in rows)
            if h >= 170:
                tf, df, bd, bf = 52, 36, 72, 30
            elif h >= 125:
                tf, df, bd, bf = (44, 30, 64, 28) if two else (46, 32, 64, 28)
            else:
                tf, df, bd, bf = 40, 31, 56, 28
            ph = nrow * h + (nrow - 1) * gap + 44
            body = ""
            for i, r in enumerate(rows):
                mark = ""
                if r.get("mark") == "o":
                    mark = f'<div class="mk o">{CHECK}</div>'
                elif r.get("mark") == "x":
                    mark = f'<div class="mk x">{CROSS}</div>'
                badge = r.get("badge", f"{i + 1:02d}")
                body += (f'<div class="row" id="{sid}r{i}" style="height:{h}px;"><div class="bd" style="width:{bd}px; height:{bd}px; font-size:{bf}px;">{badge}</div>'
                         f'<div class="tx"><div class="tt" style="font-size:{tf}px;">{r["title"]}</div><div class="ds" style="font-size:{df}px;">{r["desc"]}</div></div>{mark}</div>')
            html_scenes.append(head + hl + f'<div class="panel" id="{sid}panel" style="height:{ph}px;">{body}</div></div>')
            js.append(f'tl.from("#{sid}h", {{ opacity: 0, y: 36, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.1, 2)});')
            js.append(f'tl.from("#{sid}panel", {{ opacity: 0, y: 60, scale: 0.97, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.2, 2)});')
            seen = {}
            for i, r in enumerate(rows):
                c = seen.get(r["line"], 0)
                seen[r["line"]] = c + 1
                tt = round(st[r["line"]] + 0.05 + 0.2 * c, 2)
                x = -70 if i % 2 == 0 else 70
                js.append(f'tl.from("#{sid}r{i}", {{ opacity: 0, x: {x}, duration: 0.5, ease: "power3.out" }}, {tt});')
            fr = max(1, math.ceil((dur - 1.0) / 1.6) - 1)
            js.append(f'tl.to("#{sid}panel", {{ y: -6, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: {fr} }}, {round(t0 + 0.9, 2)});')
            js.append(exit_js)
        elif sc["type"] == "exam":
            nl = sc["html"].count("<br>") + 1
            card_h = int(nl * 46 * 1.36 + 60)
            ph = 22 + 38 + 14 + card_h + 22
            stamp = f'<div class="stamp" id="{sid}stamp" style="color:{sc["stamp_color"]}; border-color:{sc["stamp_color"]};">{sc["stamp"]}</div>'
            body = (f'<div class="dpanel" id="{sid}panel" style="height:{ph}px;"><div class="etag">{sc["tag"]}</div>'
                    f'<div class="ecard" id="{sid}ecard">“{esc_hl(sc["html"])}”</div>{stamp}</div>')
            html_scenes.append(head + hl + body + "</div>")
            js.append(f'tl.from("#{sid}h", {{ opacity: 0, y: 36, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.1, 2)});')
            js.append(f'tl.from("#{sid}panel", {{ opacity: 0, y: 70, scale: 0.95, duration: 0.55, ease: "back.out(1.4)" }}, {round(t0 + 0.2, 2)});')
            sl = sc["stamp_line"]
            ts = round(st[sl] + info[sl]["dur"] * sc["stamp_frac"], 2)
            js.append(f'tl.fromTo("#{sid}stamp", {{ opacity: 0, scale: 1.7, rotation: -16, transformOrigin: "100% 60%" }}, {{ opacity: 1, scale: 1, rotation: -8, transformOrigin: "100% 60%", duration: 0.32, ease: "power4.in" }}, {ts});')
            js.append(f'tl.to("#{sid}panel", {{ x: 7, duration: 0.05, yoyo: true, repeat: 3 }}, {round(ts + 0.32, 2)});')
            fr = max(1, math.ceil((dur - 1.0) / 1.6) - 1)
            js.append(f'tl.to("#{sid}ecard", {{ y: -5, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: {fr} }}, {round(t0 + 0.9, 2)});')
            js.append(exit_js)
        elif sc["type"] == "cta":
            qfs = min(70, int(700 / max(1.0, tw(sc["q"]))))
            btns = "".join(f'<div class="btn {"a" if c == 0 else "b"}">{t}</div>' for t, c in sc["buttons"])
            ph = 22 + int(qfs * 1.2) + 20 + 80 + 22
            body = (f'<div class="dpanel" id="{sid}panel" style="height:{ph}px;"><div class="cq" style="font-size:{qfs}px;">{sc["q"]}</div><div class="btns">{btns}</div></div>')
            if CHARACTER == "cat":
                svg, meta = cat_markup(sid, 540, 1020, 0.58)
                hx = None
            else:
                svg, hx = pend(sid, 540, 958, 0.64)
            html_scenes.append(head + svg + hl + body + "</div>")
            js.append(f'tl.from("#{sid}h", {{ opacity: 0, y: 36, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.1, 2)});')
            js.append(f'tl.from("#{sid}panel", {{ opacity: 0, y: 70, scale: 0.95, duration: 0.55, ease: "back.out(1.4)" }}, {round(t0 + 0.2, 2)});')
            js.append(f'tl.from("#{sid} .btn", {{ opacity: 0, scale: 0.6, duration: 0.4, ease: "back.out(2)", stagger: 0.25 }}, {round(t0 + 1.4, 2)});')
            js.append(f'tl.from("#{sid}W", {{ y: -520, duration: 0.9, ease: "bounce.out" }}, {round(t0 + 0.6, 2)});')
            if CHARACTER == "cat":
                js.extend(cat_js(sid, meta, round(t0 + 1.2, 2), round(dur - 1.2, 2)))
            else:
                reps = max(1, math.ceil((dur - 1.2) / 1.7) - 1)
                js.append(f'tl.fromTo("#{sid}G", {{ rotation: -7, svgOrigin: "{hx} -60" }}, {{ rotation: 7, svgOrigin: "{hx} -60", duration: 1.7, ease: "sine.inOut", yoyo: true, repeat: {reps} }}, {round(t0 + 1.2, 2)});')

    caps, capjs = "", []
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
    <style>{CSS}</style>
  </head>
  <body>
{DEFS}
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total}" data-width="1080" data-height="1920">
      {chr(10).join("      " + s for s in html_scenes).strip()}
      <div id="hud" class="clip" data-start="0" data-duration="{total}" data-track-index="1"><div class="tag">{BRAND} · EP.{n}</div></div>
      <audio id="mix" class="clip" src="assets/mix.wav" data-start="0" data-duration="{total}" data-track-index="9"></audio>
{caps}    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.to("#root", {{ backgroundPosition: "-100px -180px", duration: {total}, ease: "none" }}, 0);
      {chr(10).join("      " + s for s in capjs).strip()}
      {chr(10).join("      " + s for s in js).strip()}
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""
    os.makedirs(d + "/assets/fonts", exist_ok=True)
    shutil.copy(PAPER, d + "/assets/paper.jpg")
    shutil.copy(B.ASSETS + "/gsap.min.js", d + "/assets/gsap.min.js")
    for f in ("black-ko.woff2", "black-latin.woff2", "body-ko.woff2", "body-latin.woff2"):
        shutil.copy(f"{B.ASSETS}/fonts/{f}", f"{d}/assets/fonts/{f}")
    for f in ("hyperframes.json", "meta.json", "package.json"):
        shutil.copy(f"{B.PROJECT_FILES}/{f}", f"{d}/{f}")
    open(d + "/index.html", "w", encoding="utf-8").write(html)
    json.dump(dict(total=total, starts=st, ends=en), open(d + "/timing.json", "w"))
    print(f"ep{n}: html ok, total {total}s, scenes {len(scenes)}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    ns = [int(x) for x in sys.argv[2:]] or sorted(EPS)
    if cmd == "html":
        for n in ns:
            build(n)
