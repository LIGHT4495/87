# -*- coding: utf-8 -*-
# Paper / orange motion style engine (reference-inspired). Reuses tts + audio from build_ep.
import json, math, os, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_ep as B
from build_ep import tw, wrap, ep_dir, EPS, TAIL

PAPER = B.ASSETS + "/" + os.environ.get("PAPER_FILE", "paper.jpg")   # e.g. paper_pink.jpg
CHARACTER = os.environ.get("CHARACTER", "swing")                      # swing | cat | dog | owl | beaver | penguin
STYLE = os.environ.get("STYLE", "")                                   # "" | route | check | law  (card/row layout flavour)
PROGRESS = os.environ.get("PROGRESS", "0") == "1"                     # EP n/total + progress strip in the HUD pill
ACCENT = os.environ.get("ACCENT", "#dc480e")                          # fills (pill, badges, buttons, X marks)
ACCENT_T = os.environ.get("ACCENT_T", "#c43d08")                      # accent text on paper
ACCENT_L = os.environ.get("ACCENT_L", "#ffa070")                      # accent text on dark panel
ACCENT_RGB = os.environ.get("ACCENT_RGB", "242,86,26")                # highlighter tint
BRAND = os.environ.get("BRAND", "사회복지실천론")
ORANGE = "#dc480e"      # fills
ORANGE_T = "#c43d08"    # text accent on paper
INK = "#141414"
GOOD = "#12a37f"

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

CSS = (CSS.replace("--orange:#dc480e; --orange-t:#c43d08;", f"--orange:{ACCENT}; --orange-t:{ACCENT_T};")
          .replace(".etag { color:#ffa070;", f".etag {{ color:{ACCENT_L};").replace("rgba(242,86,26,0.38)", f"rgba({ACCENT_RGB},0.38)"))
CSS += r"""
      #hud .tag { position:relative; overflow:hidden; }
      #hud .tag i { position:absolute; left:0; bottom:0; height:6px; background:rgba(255,255,255,0.9); }
      .row .bd { position:relative; z-index:2; }
      .row .seg { position:absolute; width:10px; background:var(--orange); z-index:1; }
      .panel.route .row .bd { background:#fff; color:var(--orange-t); border:8px solid var(--orange); }
      .panel.check { background:#fff; border-radius:26px; border:none; box-shadow:0 18px 40px rgba(20,60,60,0.22); }
      .panel.check::before { content:""; position:absolute; left:290px; top:-8px; width:200px; height:22px; background:var(--orange); border-radius:12px; }
      .panel.check .row { background:transparent; box-shadow:none; border-radius:0; border-bottom:3px dashed #c9d6d6; }
      .panel.check .row:last-child { border-bottom:none; }
      .panel.check .row .bd { background:#fff; color:var(--orange-t); border:7px solid var(--ink); border-radius:14px; }
      .row .tx { position:relative; }
      .row .rp { position:absolute; left:-12px; right:-8px; top:-3px; bottom:-3px; border:4px solid var(--orange); border-radius:16px; transform:rotate(-0.6deg); pointer-events:none; }
      .panel.law { background:#fbf5e8; border:4px solid var(--orange); border-radius:26px; box-shadow:0 18px 40px rgba(60,40,20,0.2); }
      .panel.law .row { border:2px solid rgba(0,0,0,0.12); border-radius:18px; box-shadow:none; }
      .panel.law .row .bd { border-radius:16px; letter-spacing:-0.02em; }
      .vs { position:absolute; left:120px; top:506px; width:780px; height:460px; }
      .vcard { position:absolute; top:0; width:372px; height:460px; border-radius:30px; padding:20px; box-shadow:0 14px 30px rgba(0,0,0,0.18); }
      .vcard.l { left:0; background:#fff; } .vcard.r { right:0; background:#141414; }
      .vcard .vt { height:78px; border-radius:22px; display:flex; align-items:center; justify-content:center; font-family:var(--font-black); font-weight:900; font-size:42px; white-space:nowrap; }
      .vcard.l .vt { background:var(--orange); color:#fff; } .vcard.r .vt { background:#f5f0e3; color:var(--ink); }
      .vcard .vi { display:flex; align-items:center; justify-content:center; text-align:center; border-radius:18px; font-family:var(--font-black); font-weight:900; font-size:32px; line-height:1.2; margin-top:12px; }
      .vcard.l .vi { background:#f4efe2; color:var(--ink); } .vcard.r .vi { background:#2a2a2a; color:#fff; }
      .vsb { position:absolute; left:342px; top:182px; width:96px; height:96px; border-radius:50%; background:var(--orange); color:#fff; border:6px solid #fff; display:flex; align-items:center; justify-content:center; font-family:var(--font-black); font-weight:900; font-size:38px; z-index:3; box-shadow:0 8px 18px rgba(0,0,0,0.25); }
      .cd { position:absolute; left:0; top:0; right:0; bottom:0; display:flex; align-items:center; justify-content:center; font-family:var(--font-black); font-weight:900; font-size:170px; color:#fff; opacity:0; pointer-events:none; }
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


def dog_markup(sid, cx, by, s):
    """Puppy with an orange scarf on a round stool. Origins for GSAP are LOCAL coordinates."""
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <rect x="-140" y="-34" width="280" height="34" rx="10" fill="#dc480e"></rect>
  <ellipse cx="0" cy="-34" rx="140" ry="24" fill="#ff7d3d"></ellipse>
  <g id="{sid}C">
    <path id="{sid}T" d="M 66 -86 C 130 -84 160 -130 138 -188" stroke="#e9b36a" stroke-width="30" fill="none" stroke-linecap="round"></path>
    <ellipse cx="0" cy="-122" rx="80" ry="90" fill="#f0c27b"></ellipse>
    <ellipse cx="0" cy="-104" rx="48" ry="62" fill="#fff3e0"></ellipse>
    <ellipse cx="-30" cy="-56" rx="24" ry="30" fill="#f0c27b"></ellipse><ellipse cx="30" cy="-56" rx="24" ry="30" fill="#f0c27b"></ellipse>
    <ellipse cx="-30" cy="-44" rx="27" ry="14" fill="#fff3e0"></ellipse><ellipse cx="30" cy="-44" rx="27" ry="14" fill="#fff3e0"></ellipse>
    <g id="{sid}EL"><ellipse cx="-76" cy="-262" rx="34" ry="64" fill="#c9863f" transform="rotate(14 -76 -262)"></ellipse></g>
    <g id="{sid}ER"><ellipse cx="76" cy="-262" rx="34" ry="64" fill="#c9863f" transform="rotate(-14 76 -262)"></ellipse></g>
    <circle cx="0" cy="-256" r="84" fill="#f0c27b"></circle>
    <ellipse cx="0" cy="-232" rx="48" ry="38" fill="#fff3e0"></ellipse>
    <circle cx="-34" cy="-292" r="13" fill="#e9b36a"></circle><circle cx="34" cy="-292" r="13" fill="#e9b36a"></circle>
    <g id="{sid}E"><ellipse cx="-30" cy="-268" rx="10" ry="13" fill="#2a1a12"></ellipse><ellipse cx="30" cy="-268" rx="10" ry="13" fill="#2a1a12"></ellipse>
      <circle cx="-27" cy="-272" r="3.5" fill="#fff"></circle><circle cx="33" cy="-272" r="3.5" fill="#fff"></circle></g>
    <circle cx="-54" cy="-240" r="11" fill="#ff9aa2" opacity="0.55"></circle><circle cx="54" cy="-240" r="11" fill="#ff9aa2" opacity="0.55"></circle>
    <ellipse cx="0" cy="-244" rx="16" ry="11" fill="#3a2a22"></ellipse>
    <path d="M 0 -233 v 10 M -16 -218 Q 0 -202 16 -218" stroke="#3a2a22" stroke-width="4" fill="none" stroke-linecap="round"></path>
    <ellipse cx="0" cy="-200" rx="11" ry="15" fill="#ff7b95"></ellipse>
    <path d="M -64 -180 Q 0 -152 64 -180 L 58 -158 Q 0 -134 -58 -158 Z" fill="#f2561a"></path>
    <path d="M 10 -154 L 36 -118 L 14 -112 Z" fill="#dc480e"></path>
    <g id="{sid}P"><path d="M 52 -150 Q 90 -168 96 -222" stroke="#f0c27b" stroke-width="30" stroke-linecap="round" fill="none"></path>
    <circle cx="98" cy="-230" r="18" fill="#fff3e0"></circle></g>
  </g>
</g>"""
    svg = f'<svg id="{sid}p" class="full" viewBox="0 0 1080 1920" width="1080" height="1920"><g id="{sid}W">{parts}</g></svg>'
    return svg, dict(tail=(66, -86), paw=(52, -150), eye=(0, -268), el=(-58, -312), er=(58, -312))


def dog_js(sid, meta, t0, dur):
    out = []
    out.append(f'tl.fromTo("#{sid}C", {{ y: 0 }}, {{ y: -8, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / 0.8) - 1)} }}, {t0});')
    tx, ty = meta["tail"]
    out.append(f'tl.fromTo("#{sid}T", {{ rotation: -14, svgOrigin: "{tx} {ty}" }}, {{ rotation: 18, svgOrigin: "{tx} {ty}", duration: 0.32, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / 0.32) - 1)} }}, {t0});')
    for k, sign in (("el", 1), ("er", -1)):
        ox, oy = meta[k]
        out.append(f'tl.fromTo("#{sid}{k.upper()}", {{ rotation: {-5 * sign}, svgOrigin: "{ox} {oy}" }}, {{ rotation: {5 * sign}, svgOrigin: "{ox} {oy}", duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / 0.9) - 1)} }}, {t0});')
    px, py = meta["paw"]
    out.append(f'tl.fromTo("#{sid}P", {{ rotation: -14, svgOrigin: "{px} {py}" }}, {{ rotation: 12, svgOrigin: "{px} {py}", duration: 0.5, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / 0.5) - 1)} }}, {t0});')
    ex, ey = meta["eye"]
    t = t0 + 1.6
    while t < t0 + dur - 0.3:
        out.append(f'tl.to("#{sid}E", {{ scaleY: 0.1, svgOrigin: "{ex} {ey}", duration: 0.07, yoyo: true, repeat: 1 }}, {round(t, 2)});')
        t += 2.4
    return out


def _wrap(sid, parts):
    return f'<svg id="{sid}p" class="full" viewBox="0 0 1080 1920" width="1080" height="1920"><g id="{sid}W">{parts}</g></svg>'


def _blink(out, sid, ex, ey, t0, dur, first=1.8, step=2.6):
    t = t0 + first
    while t < t0 + dur - 0.3:
        out.append(f'tl.to("#{sid}E", {{ scaleY: 0.1, svgOrigin: "{ex} {ey}", duration: 0.07, yoyo: true, repeat: 1 }}, {round(t, 2)});')
        t += step


def _swing(out, sel, a, b, org, per, t0, dur):
    ox, oy = org
    out.append(f'tl.fromTo("{sel}", {{ rotation: {a}, svgOrigin: "{ox} {oy}" }}, {{ rotation: {b}, svgOrigin: "{ox} {oy}", duration: {per}, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / per) - 1)} }}, {t0});')


def _bob(out, sid, amp, per, t0, dur):
    out.append(f'tl.fromTo("#{sid}C", {{ y: 0 }}, {{ y: {-amp}, duration: {per}, ease: "sine.inOut", yoyo: true, repeat: {max(1, math.ceil(dur / per) - 1)} }}, {t0});')


def owl_markup(sid, cx, by, s):
    """Owl professor (graduation cap, round glasses) on a bar-chart podium. Drawing coords are local; no transforms on animated groups."""
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <rect x="-150" y="-70" width="90" height="70" rx="8" fill="{ACCENT}"></rect>
  <rect x="-60" y="-140" width="120" height="140" rx="8" fill="#f5c842"></rect>
  <rect x="60" y="-100" width="90" height="100" rx="8" fill="{ACCENT}"></rect>
  <g transform="translate(0 -140)">
   <g id="{sid}C">
    <g id="{sid}WL"><ellipse cx="-92" cy="-150" rx="26" ry="66" fill="#9a6a3c" transform="rotate(14 -92 -150)"></ellipse></g>
    <g id="{sid}WR"><ellipse cx="92" cy="-150" rx="26" ry="66" fill="#9a6a3c" transform="rotate(-14 92 -150)"></ellipse></g>
    <ellipse cx="0" cy="-160" rx="90" ry="110" fill="#b9824f"></ellipse><ellipse cx="0" cy="-130" rx="58" ry="78" fill="#f6e3c4"></ellipse>
    <path d="M -30 -150 q 14 12 28 0 M 2 -150 q 14 12 28 0 M -30 -120 q 14 12 28 0 M 2 -120 q 14 12 28 0" stroke="#d9bd93" stroke-width="5" fill="none"></path>
    <ellipse cx="-44" cy="6" rx="30" ry="12" fill="#f2a33a"></ellipse><ellipse cx="44" cy="6" rx="30" ry="12" fill="#f2a33a"></ellipse>
    <path d="M -78 -262 L -62 -312 L -34 -272 Z M 78 -262 L 62 -312 L 34 -272 Z" fill="#9a6a3c"></path>
    <circle cx="-36" cy="-238" r="36" fill="#fff"></circle><circle cx="36" cy="-238" r="36" fill="#fff"></circle>
    <g id="{sid}E"><circle cx="-36" cy="-238" r="16" fill="#2a1a12"></circle><circle cx="36" cy="-238" r="16" fill="#2a1a12"></circle><circle cx="-31" cy="-244" r="5" fill="#fff"></circle><circle cx="41" cy="-244" r="5" fill="#fff"></circle></g>
    <circle cx="-36" cy="-238" r="40" fill="none" stroke="{ACCENT}" stroke-width="6"></circle><circle cx="36" cy="-238" r="40" fill="none" stroke="{ACCENT}" stroke-width="6"></circle><path d="M -2 -238 h 4" stroke="{ACCENT}" stroke-width="6"></path>
    <path d="M -12 -214 L 12 -214 L 0 -190 Z" fill="#f2a33a"></path>
    <path d="M -100 -290 L 0 -330 L 100 -290 L 0 -254 Z" fill="{ACCENT}"></path><rect x="-54" y="-292" width="108" height="26" fill="{ACCENT}"></rect>
    <g id="{sid}TS"><path d="M 84 -296 L 100 -230" stroke="#f5c842" stroke-width="6"></path><circle cx="100" cy="-226" r="10" fill="#f5c842"></circle></g>
   </g>
  </g>
</g>"""
    return _wrap(sid, parts), dict(wl=(-96, -205), wr=(96, -205), ts=(84, -296), eye=(0, -238))


def owl_js(sid, meta, t0, dur):
    out = []
    _bob(out, sid, 8, 0.9, t0, dur)
    _swing(out, f"#{sid}WL", -4, 16, meta["wl"], 0.7, t0, dur)
    _swing(out, f"#{sid}WR", 4, -22, meta["wr"], 0.55, t0, dur)
    _swing(out, f"#{sid}TS", -10, 12, meta["ts"], 0.8, t0, dur)
    _blink(out, sid, *meta["eye"], t0, dur, 1.9, 2.7)
    return out


def beaver_markup(sid, cx, by, s):
    """Beaver team lead (hard hat, clipboard) on stacked file boxes."""
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <rect x="-130" y="-44" width="260" height="44" rx="10" fill="{ACCENT}"></rect><rect x="-20" y="-30" width="40" height="8" rx="4" fill="#fff" opacity="0.75"></rect>
  <rect x="-110" y="-88" width="220" height="44" rx="10" fill="#ffd36b"></rect><rect x="-20" y="-74" width="40" height="8" rx="4" fill="#fff" opacity="0.75"></rect>
  <g transform="translate(0 -88)">
   <g id="{sid}C">
    <g id="{sid}T"><ellipse cx="96" cy="-110" rx="64" ry="26" fill="#6e4524" transform="rotate(-28 96 -110)"></ellipse><path d="M 62 -126 l 20 18 M 80 -138 l 22 18 M 98 -150 l 20 18" stroke="#4e2f16" stroke-width="4" stroke-linecap="round" fill="none"></path></g>
    <ellipse cx="0" cy="-130" rx="84" ry="96" fill="#a0693a"></ellipse><ellipse cx="0" cy="-112" rx="52" ry="66" fill="#e8c9a0"></ellipse>
    <ellipse cx="-40" cy="-10" rx="30" ry="12" fill="#6e4524"></ellipse><ellipse cx="40" cy="-10" rx="30" ry="12" fill="#6e4524"></ellipse>
    <circle cx="-62" cy="-290" r="22" fill="#a0693a"></circle><circle cx="62" cy="-290" r="22" fill="#a0693a"></circle><circle cx="-62" cy="-290" r="11" fill="#6e4524"></circle><circle cx="62" cy="-290" r="11" fill="#6e4524"></circle>
    <circle cx="0" cy="-236" r="76" fill="#a0693a"></circle><ellipse cx="0" cy="-216" rx="42" ry="30" fill="#e8c9a0"></ellipse>
    <ellipse cx="0" cy="-230" rx="15" ry="10" fill="#3a2a22"></ellipse><rect x="-12" y="-212" width="12" height="26" rx="4" fill="#fff" stroke="#c9b08a" stroke-width="2"></rect><rect x="0" y="-212" width="12" height="26" rx="4" fill="#fff" stroke="#c9b08a" stroke-width="2"></rect>
    <g id="{sid}E"><circle cx="-30" cy="-250" r="9" fill="#2a1a12"></circle><circle cx="30" cy="-250" r="9" fill="#2a1a12"></circle><circle cx="-27" cy="-253" r="3" fill="#fff"></circle><circle cx="33" cy="-253" r="3" fill="#fff"></circle></g>
    <circle cx="-48" cy="-226" r="9" fill="#ff9aa2" opacity="0.55"></circle><circle cx="48" cy="-226" r="9" fill="#ff9aa2" opacity="0.55"></circle>
    <path d="M -82 -270 Q 0 -350 82 -270 Z" fill="#ffc93c"></path><rect x="-94" y="-274" width="188" height="16" rx="8" fill="#ffb300"></rect><rect x="-10" y="-322" width="20" height="40" fill="#ff8a3d"></rect>
    <g id="{sid}P"><rect x="-78" y="-150" width="108" height="136" rx="10" fill="#fff" stroke="#6e4524" stroke-width="6"></rect><rect x="-44" y="-160" width="40" height="18" rx="6" fill="{ACCENT}"></rect>
     <path d="M -60 -116 h 70 M -60 -86 h 70 M -60 -56 h 50" stroke="#c9d6d6" stroke-width="6" stroke-linecap="round"></path><path d="M -62 -118 l 8 8 l 14 -16" stroke="{ACCENT}" stroke-width="6" fill="none" stroke-linecap="round"></path>
     <circle cx="-50" cy="-60" r="14" fill="#e8c9a0"></circle><circle cx="26" cy="-70" r="14" fill="#e8c9a0"></circle></g>
   </g>
  </g>
</g>"""
    return _wrap(sid, parts), dict(tail=(50, -86), clip=(-24, -14), eye=(0, -250))


def beaver_js(sid, meta, t0, dur):
    out = []
    _bob(out, sid, 7, 0.85, t0, dur)
    _swing(out, f"#{sid}T", -8, 18, meta["tail"], 0.45, t0, dur)
    _swing(out, f"#{sid}P", -3, 3, meta["clip"], 0.6, t0, dur)
    _blink(out, sid, *meta["eye"], t0, dur, 1.7, 2.5)
    return out


def penguin_markup(sid, cx, by, s):
    """Penguin judge (white wig, gavel) on a stack of law books."""
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <rect x="-140" y="-38" width="280" height="38" rx="8" fill="{ACCENT}"></rect><rect x="-120" y="-72" width="240" height="34" rx="8" fill="#b08d3c"></rect><rect x="-100" y="-104" width="200" height="32" rx="8" fill="{ACCENT}"></rect>
  <path d="M -80 -56 h 160" stroke="#fff" stroke-width="3" opacity="0.6"></path>
  <g transform="translate(0 -104)">
   <g id="{sid}C">
    <ellipse cx="-34" cy="-4" rx="28" ry="12" fill="#f2a33a"></ellipse><ellipse cx="34" cy="-4" rx="28" ry="12" fill="#f2a33a"></ellipse>
    <ellipse cx="-94" cy="-150" rx="22" ry="62" fill="#2b2d42" transform="rotate(14 -94 -150)"></ellipse>
    <ellipse cx="0" cy="-130" rx="88" ry="110" fill="#2b2d42"></ellipse><ellipse cx="0" cy="-116" rx="58" ry="84" fill="#fff"></ellipse>
    <g id="{sid}G"><ellipse cx="98" cy="-200" rx="22" ry="62" fill="#2b2d42" transform="rotate(-32 98 -200)"></ellipse>
     <path d="M 112 -246 L 156 -312" stroke="#8a5a2b" stroke-width="14" stroke-linecap="round"></path><rect x="132" y="-346" width="70" height="32" rx="8" fill="#8a5a2b" transform="rotate(-36 167 -330)"></rect></g>
    <circle cx="0" cy="-262" r="70" fill="#2b2d42"></circle><ellipse cx="-26" cy="-258" rx="30" ry="38" fill="#fff"></ellipse><ellipse cx="26" cy="-258" rx="30" ry="38" fill="#fff"></ellipse>
    <g id="{sid}E"><circle cx="-26" cy="-262" r="9" fill="#2a1a12"></circle><circle cx="26" cy="-262" r="9" fill="#2a1a12"></circle><circle cx="-23" cy="-266" r="3" fill="#fff"></circle><circle cx="29" cy="-266" r="3" fill="#fff"></circle></g>
    <path d="M -16 -242 L 16 -242 L 0 -218 Z" fill="#f2a33a"></path><circle cx="-46" cy="-240" r="9" fill="#ff9aa2" opacity="0.6"></circle><circle cx="46" cy="-240" r="9" fill="#ff9aa2" opacity="0.6"></circle>
    <g fill="#fff" stroke="#d8d8e4" stroke-width="3"><circle cx="-62" cy="-300" r="24"></circle><circle cx="-70" cy="-268" r="22"></circle><circle cx="62" cy="-300" r="24"></circle><circle cx="70" cy="-268" r="22"></circle><circle cx="-34" cy="-332" r="24"></circle><circle cx="0" cy="-340" r="26"></circle><circle cx="34" cy="-332" r="24"></circle></g>
   </g>
  </g>
</g>"""
    return _wrap(sid, parts), dict(arm=(84, -170), eye=(0, -262))


def penguin_js(sid, meta, t0, dur):
    out = []
    _bob(out, sid, 7, 0.9, t0, dur)
    ax, ay = meta["arm"]
    t = t0 + 0.9
    while t < t0 + dur - 0.6:      # gavel slam, then a small recoil
        out.append(f'tl.fromTo("#{sid}G", {{ rotation: -6, svgOrigin: "{ax} {ay}" }}, {{ rotation: 30, svgOrigin: "{ax} {ay}", duration: 0.13, ease: "power2.in" }}, {round(t, 2)});')
        out.append(f'tl.to("#{sid}G", {{ rotation: -6, svgOrigin: "{ax} {ay}", duration: 0.45, ease: "power2.out" }}, {round(t + 0.13, 2)});')
        t += 2.0
    _blink(out, sid, *meta["eye"], t0, dur, 1.5, 2.6)
    return out


def rabbit_markup(sid, cx, by, s):
    """White rabbit with long wobbling ears on a round cushion."""
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <rect x="-130" y="-30" width="260" height="30" rx="10" fill="{ACCENT}"></rect><ellipse cx="0" cy="-30" rx="130" ry="22" fill="{ACCENT}" opacity="0.75"></ellipse>
  <g id="{sid}C">
    <ellipse cx="-44" cy="-36" rx="30" ry="14" fill="#fff"></ellipse><ellipse cx="44" cy="-36" rx="30" ry="14" fill="#fff"></ellipse>
    <ellipse cx="0" cy="-120" rx="72" ry="92" fill="#fff"></ellipse><ellipse cx="0" cy="-110" rx="46" ry="62" fill="#ffeef2"></ellipse>
    <circle cx="82" cy="-70" r="20" fill="#fff"></circle>
    <g id="{sid}EL"><ellipse cx="-36" cy="-352" rx="24" ry="78" fill="#fff" transform="rotate(-8 -36 -352)"></ellipse><ellipse cx="-36" cy="-352" rx="11" ry="58" fill="#ffb3c1" transform="rotate(-8 -36 -352)"></ellipse></g>
    <g id="{sid}ER"><ellipse cx="36" cy="-352" rx="24" ry="78" fill="#fff" transform="rotate(8 36 -352)"></ellipse><ellipse cx="36" cy="-352" rx="11" ry="58" fill="#ffb3c1" transform="rotate(8 36 -352)"></ellipse></g>
    <circle cx="0" cy="-240" r="80" fill="#fff"></circle>
    <circle cx="-48" cy="-216" r="11" fill="#ffb3c1" opacity="0.7"></circle><circle cx="48" cy="-216" r="11" fill="#ffb3c1" opacity="0.7"></circle>
    <g id="{sid}E"><ellipse cx="-28" cy="-246" rx="9" ry="13" fill="#2a1a12"></ellipse><ellipse cx="28" cy="-246" rx="9" ry="13" fill="#2a1a12"></ellipse><circle cx="-25" cy="-250" r="3" fill="#fff"></circle><circle cx="31" cy="-250" r="3" fill="#fff"></circle></g>
    <path d="M -8 -226 h 16 l -8 10 z" fill="#ff7b95"></path><path d="M -14 -212 Q -7 -204 0 -214 Q 7 -204 14 -212" stroke="#7a3b2a" stroke-width="4" fill="none" stroke-linecap="round"></path>
    <path d="M -46 -226 L -96 -234 M -46 -216 L -94 -212 M 46 -226 L 96 -234 M 46 -216 L 94 -212" stroke="#c9b8bd" stroke-width="3" stroke-linecap="round"></path>
    <path d="M -22 -170 Q 0 -160 22 -170 L 16 -150 Q 0 -140 -16 -150 Z" fill="{ACCENT}"></path>
    <g id="{sid}P"><path d="M 50 -150 Q 90 -168 98 -222" stroke="#fff" stroke-width="28" stroke-linecap="round" fill="none"></path><circle cx="100" cy="-230" r="17" fill="#ffeef2"></circle></g>
  </g>
</g>"""
    return _wrap(sid, parts), dict(el=(-36, -290), er=(36, -290), paw=(50, -150), eye=(0, -246))


def rabbit_js(sid, meta, t0, dur):
    out = []
    _bob(out, sid, 9, 0.85, t0, dur)
    _swing(out, f"#{sid}EL", -6, 10, meta["el"], 0.9, t0, dur)
    _swing(out, f"#{sid}ER", 6, -12, meta["er"], 1.1, t0, dur)
    _swing(out, f"#{sid}P", -14, 12, meta["paw"], 0.5, t0, dur)
    _blink(out, sid, *meta["eye"], t0, dur, 1.7, 2.5)
    return out


def bear_markup(sid, cx, by, s):
    """Brown bear with a scarf on a stack of books."""
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <rect x="-140" y="-44" width="280" height="44" rx="10" fill="{ACCENT}"></rect><rect x="-120" y="-84" width="240" height="40" rx="10" fill="#f5e6c8"></rect><rect x="-120" y="-70" width="240" height="6" fill="#d9c6a0"></rect>
  <g id="{sid}C">
    <ellipse cx="-46" cy="-88" rx="30" ry="14" fill="#7a4a2a"></ellipse><ellipse cx="46" cy="-88" rx="30" ry="14" fill="#7a4a2a"></ellipse>
    <ellipse cx="0" cy="-170" rx="84" ry="92" fill="#a56a3a"></ellipse><ellipse cx="0" cy="-156" rx="54" ry="66" fill="#e8c9a0"></ellipse>
    <circle cx="-62" cy="-312" r="30" fill="#a56a3a"></circle><circle cx="62" cy="-312" r="30" fill="#a56a3a"></circle><circle cx="-62" cy="-312" r="15" fill="#e8c9a0"></circle><circle cx="62" cy="-312" r="15" fill="#e8c9a0"></circle>
    <circle cx="0" cy="-262" r="82" fill="#a56a3a"></circle><ellipse cx="0" cy="-240" rx="40" ry="32" fill="#e8c9a0"></ellipse>
    <ellipse cx="0" cy="-252" rx="14" ry="10" fill="#3a2a22"></ellipse><path d="M 0 -243 v 8 M -14 -232 Q 0 -218 14 -232" stroke="#3a2a22" stroke-width="4" fill="none" stroke-linecap="round"></path>
    <g id="{sid}E"><circle cx="-30" cy="-282" r="9" fill="#2a1a12"></circle><circle cx="30" cy="-282" r="9" fill="#2a1a12"></circle><circle cx="-27" cy="-285" r="3" fill="#fff"></circle><circle cx="33" cy="-285" r="3" fill="#fff"></circle></g>
    <circle cx="-52" cy="-250" r="10" fill="#ff9aa2" opacity="0.5"></circle><circle cx="52" cy="-250" r="10" fill="#ff9aa2" opacity="0.5"></circle>
    <path d="M -66 -204 Q 0 -176 66 -204 L 60 -182 Q 0 -158 -60 -182 Z" fill="{ACCENT}"></path><path d="M 10 -178 L 36 -140 L 14 -134 Z" fill="{ACCENT}"></path>
    <g id="{sid}P"><path d="M 56 -170 Q 96 -190 102 -246" stroke="#a56a3a" stroke-width="32" stroke-linecap="round" fill="none"></path><circle cx="104" cy="-254" r="19" fill="#e8c9a0"></circle></g>
  </g>
</g>"""
    return _wrap(sid, parts), dict(paw=(56, -170), eye=(0, -282))


def bear_js(sid, meta, t0, dur):
    out = []
    _bob(out, sid, 7, 0.95, t0, dur)
    _swing(out, f"#{sid}P", -16, 14, meta["paw"], 0.55, t0, dur)
    _blink(out, sid, *meta["eye"], t0, dur, 1.9, 2.7)
    return out


def turtle_markup(sid, cx, by, s):
    """Little turtle scholar (round glasses) on a stone."""
    parts = f"""
<g transform="translate({cx} {by}) scale({s})">
  <ellipse cx="0" cy="-26" rx="150" ry="28" fill="#9aa3a8"></ellipse><rect x="-150" y="-26" width="300" height="26" rx="12" fill="#7f898e"></rect>
  <g id="{sid}C">
    <ellipse cx="0" cy="-128" rx="112" ry="96" fill="{ACCENT}"></ellipse>
    <path d="M -50 -170 l 22 -20 l 28 12 l 6 30 l -26 18 l -30 -10 z M 14 -172 l 28 -14 l 22 20 l -8 28 l -30 6 l -18 -22 z M -26 -110 l 30 -6 l 16 24 l -14 24 l -30 0 l -12 -22 z" fill="none" stroke="#ffffff" stroke-width="5" opacity="0.55"></path>
    <ellipse cx="0" cy="-104" rx="62" ry="70" fill="#d8efd0"></ellipse>
    <ellipse cx="-50" cy="-34" rx="32" ry="16" fill="#6fae6a"></ellipse><ellipse cx="50" cy="-34" rx="32" ry="16" fill="#6fae6a"></ellipse>
    <g id="{sid}H">
      <circle cx="0" cy="-248" r="74" fill="#7fc47a"></circle><circle cx="-46" cy="-228" r="10" fill="#ff9aa2" opacity="0.6"></circle><circle cx="46" cy="-228" r="10" fill="#ff9aa2" opacity="0.6"></circle>
      <g id="{sid}E"><circle cx="-26" cy="-256" r="9" fill="#2a1a12"></circle><circle cx="26" cy="-256" r="9" fill="#2a1a12"></circle><circle cx="-23" cy="-259" r="3" fill="#fff"></circle><circle cx="29" cy="-259" r="3" fill="#fff"></circle></g>
      <circle cx="-26" cy="-256" r="24" fill="none" stroke="#2a2a2a" stroke-width="5"></circle><circle cx="26" cy="-256" r="24" fill="none" stroke="#2a2a2a" stroke-width="5"></circle><path d="M -2 -256 h 4" stroke="#2a2a2a" stroke-width="5"></path>
      <path d="M -16 -222 Q 0 -206 16 -222" stroke="#3a5a38" stroke-width="5" fill="none" stroke-linecap="round"></path>
    </g>
    <g id="{sid}P"><path d="M 74 -140 Q 112 -160 118 -212" stroke="#7fc47a" stroke-width="30" stroke-linecap="round" fill="none"></path><circle cx="120" cy="-220" r="17" fill="#d8efd0"></circle></g>
  </g>
</g>"""
    return _wrap(sid, parts), dict(head=(0, -180), paw=(74, -140), eye=(0, -256))


def turtle_js(sid, meta, t0, dur):
    out = []
    _bob(out, sid, 6, 1.0, t0, dur)
    _swing(out, f"#{sid}H", -4, 5, meta["head"], 1.2, t0, dur)
    _swing(out, f"#{sid}P", -14, 12, meta["paw"], 0.55, t0, dur)
    _blink(out, sid, *meta["eye"], t0, dur, 1.8, 2.6)
    return out


MASCOTS = {"cat": (cat_markup, cat_js, (1015, 0.92), (1020, 0.58)), "dog": (dog_markup, dog_js, (1015, 1.0), (1020, 0.62)),
           "owl": (owl_markup, owl_js, (1015, 0.86), (1020, 0.5)), "beaver": (beaver_markup, beaver_js, (1015, 1.0), (1020, 0.58)),
           "penguin": (penguin_markup, penguin_js, (1015, 0.92), (1020, 0.54)),
           "rabbit": (rabbit_markup, rabbit_js, (1015, 0.9), (1020, 0.52)), "bear": (bear_markup, bear_js, (1015, 0.95), (1020, 0.56)),
           "turtle": (turtle_markup, turtle_js, (1015, 1.0), (1020, 0.6))}


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
            if CHARACTER in MASCOTS:
                mk, mjs, (mby, ms), _ = MASCOTS[CHARACTER]
                svg, meta = mk(sid, 540, mby, ms)
                html_scenes.append(head + svg + hl + "</div>")
                js.extend(mjs(sid, meta, 0, dur))
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
                if STYLE == "check":
                    badge = "✓" if r.get("mark") != "x" else "!"
                elif STYLE == "law":
                    badge = r.get("badge", f"§{i + 1}")
                seg = ""
                if STYLE == "route" and nrow > 1:
                    cxs = 16 + bd // 2 - 5
                    if i == 0:
                        seg = f'<div class="seg" style="left:{cxs}px; top:50%; bottom:-14px;"></div>'
                    elif i == nrow - 1:
                        seg = f'<div class="seg" style="left:{cxs}px; top:-14px; bottom:50%;"></div>'
                    else:
                        seg = f'<div class="seg" style="left:{cxs}px; top:-14px; bottom:-14px;"></div>'
                rp = '<div class="rp" id="%sp%d"></div>' % (sid, i) if STYLE == "check" and r.get("mark") == "x" else ""
                body += (f'<div class="row" id="{sid}r{i}" style="height:{h}px;">{seg}<div class="bd" style="width:{bd}px; height:{bd}px; font-size:{bf}px;">{badge}</div>'
                         f'<div class="tx"><div class="tt" style="font-size:{tf}px;">{r["title"]}</div><div class="ds" style="font-size:{df}px;">{r["desc"]}</div>{rp}</div>{mark}</div>')
            pcls = {"route": "panel route", "check": "panel check", "law": "panel law"}.get(STYLE, "panel")
            html_scenes.append(head + hl + f'<div class="{pcls}" id="{sid}panel" style="height:{ph}px;">{body}</div></div>')
            js.append(f'tl.from("#{sid}h", {{ opacity: 0, y: 36, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.1, 2)});')
            js.append(f'tl.from("#{sid}panel", {{ opacity: 0, y: 60, scale: 0.97, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.2, 2)});')
            seen = {}
            for i, r in enumerate(rows):
                c = seen.get(r["line"], 0)
                seen[r["line"]] = c + 1
                tt = round(st[r["line"]] + 0.05 + 0.2 * c, 2)
                x = -70 if i % 2 == 0 else 70
                js.append(f'tl.from("#{sid}r{i}", {{ opacity: 0, x: {x}, duration: 0.5, ease: "power3.out" }}, {tt});')
                if STYLE == "check" and r.get("mark") == "x":
                    js.append(f'tl.from("#{sid}p{i}", {{ opacity: 0, scale: 0.5, duration: 0.3, ease: "back.out(2)" }}, {round(tt + 0.55, 2)});')
            fr = max(1, math.ceil((dur - 1.0) / 1.6) - 1)
            js.append(f'tl.to("#{sid}panel", {{ y: -6, duration: 1.6, ease: "sine.inOut", yoyo: true, repeat: {fr} }}, {round(t0 + 0.9, 2)});')
            js.append(exit_js)
        elif sc["type"] == "versus":
            L, R = sc["left"], sc["right"]
            def vcard(side, d):
                n = len(d["items"])
                ih = (460 - 40 - 78 - 12 - (n - 1) * 12) // n
                its = "".join(f'<div class="vi" id="{sid}{side}i{j}" style="height:{ih}px;">{t}</div>' for j, t in enumerate(d["items"]))
                return f'<div class="vcard {side}" id="{sid}{side}"><div class="vt">{d["title"]}</div>{its}</div>'
            body = f'<div class="vs" id="{sid}panel">{vcard("l", L)}{vcard("r", R)}<div class="vsb" id="{sid}vsb">VS</div></div>'
            html_scenes.append(head + hl + body + "</div>")
            js.append(f'tl.from("#{sid}h", {{ opacity: 0, y: 36, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.1, 2)});')
            tl_, tr_ = round(st[L["line"]] + 0.05, 2), round(st[R["line"]] + 0.05, 2)
            js.append(f'tl.from("#{sid}l", {{ opacity: 0, x: -90, duration: 0.5, ease: "power3.out" }}, {tl_});')
            js.append(f'tl.from("#{sid}r", {{ opacity: 0, x: 90, duration: 0.5, ease: "power3.out" }}, {tr_});')
            for side, tt in (("l", tl_), ("r", tr_)):
                n = len(L["items"] if side == "l" else R["items"])
                for j in range(n):
                    js.append(f'tl.from("#{sid}{side}i{j}", {{ opacity: 0, y: 22, duration: 0.35, ease: "power2.out" }}, {round(tt + 0.35 + 0.22 * j, 2)});')
            js.append(f'tl.from("#{sid}vsb", {{ scale: 0, rotation: -40, duration: 0.45, ease: "back.out(2.2)" }}, {round(tr_ - 0.1, 2)});')
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
            btns = "".join(f'<div class="btn {"a" if c == 0 else "b"}" id="{sid}b{j}">{t}</div>' for j, (t, c) in enumerate(sc["buttons"]))
            rv = sc.get("reveal")
            cds = "".join(f'<div class="cd" id="{sid}cd{k}" style="color:{ACCENT_L};">{k}</div>' for k in (3, 2, 1)) if rv else ""
            ph = 22 + int(qfs * 1.2) + 20 + 80 + 22
            body = (f'<div class="dpanel" id="{sid}panel" style="height:{ph}px;"><div class="cq" style="font-size:{qfs}px;">{sc["q"]}</div><div class="btns">{btns}</div>{cds}</div>')
            if CHARACTER in MASCOTS:
                mk, mjs, _, (mby, ms) = MASCOTS[CHARACTER]
                svg, meta = mk(sid, 540, mby, ms)
                hx = None
            else:
                svg, hx = pend(sid, 540, 958, 0.64)
            html_scenes.append(head + svg + hl + body + "</div>")
            js.append(f'tl.from("#{sid}h", {{ opacity: 0, y: 36, duration: 0.5, ease: "power3.out" }}, {round(t0 + 0.1, 2)});')
            js.append(f'tl.from("#{sid}panel", {{ opacity: 0, y: 70, scale: 0.95, duration: 0.55, ease: "back.out(1.4)" }}, {round(t0 + 0.2, 2)});')
            js.append(f'tl.from("#{sid} .btn", {{ opacity: 0, scale: 0.6, duration: 0.4, ease: "back.out(2)", stagger: 0.25 }}, {round(t0 + 1.4, 2)});')
            js.append(f'tl.from("#{sid}W", {{ y: -520, duration: 0.9, ease: "bounce.out" }}, {round(t0 + 0.6, 2)});')
            if rv:   # 3-2-1 countdown (fills the pause before the answer line), then highlight the right button
                tr = st[rv["line"]]
                js.append(f'tl.to("#{sid}panel .cq, #{sid}panel .btns", {{ opacity: 0.12, duration: 0.25 }}, {round(tr - 2.3, 2)});')
                for k, tk in ((3, tr - 2.1), (2, tr - 1.4), (1, tr - 0.7)):
                    js.append(f'tl.fromTo("#{sid}cd{k}", {{ opacity: 0, scale: 1.8 }}, {{ opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)" }}, {round(tk, 2)});')
                    js.append(f'tl.to("#{sid}cd{k}", {{ opacity: 0, duration: 0.12 }}, {round(tk + 0.55, 2)});')
                js.append(f'tl.to("#{sid}panel .cq, #{sid}panel .btns", {{ opacity: 1, duration: 0.2 }}, {round(tr, 2)});')
                for j in range(len(sc["buttons"])):
                    if j == rv["answer"]:
                        js.append(f'tl.to("#{sid}b{j}", {{ backgroundColor: "{GOOD}", color: "#fff", scale: 1.14, duration: 0.35, ease: "back.out(2.4)" }}, {round(tr + 0.05, 2)});')
                    else:
                        js.append(f'tl.to("#{sid}b{j}", {{ opacity: 0.3, scale: 0.9, duration: 0.3 }}, {round(tr + 0.05, 2)});')
            if CHARACTER in MASCOTS:
                js.extend(mjs(sid, meta, round(t0 + 1.2, 2), round(dur - 1.2, 2)))
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

    hud_extra = f"/{len(EPS)}" if PROGRESS else ""
    hud_bar = f'<i style="width:{round(100 * n / len(EPS))}%"></i>' if PROGRESS else ""
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
      <div id="hud" class="clip" data-start="0" data-duration="{total}" data-track-index="1"><div class="tag">{BRAND} · EP.{n}{hud_extra}{hud_bar}</div></div>
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
