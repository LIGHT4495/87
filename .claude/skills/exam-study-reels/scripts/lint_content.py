# -*- coding: utf-8 -*-
# Pre-flight text-width lint for an episodes module.
#   REELS_CONTENT=<dir> EPMOD=episodes_xxx ENGINE=v1|v2 python3 lint_content.py
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault("EPMOD", os.environ.get("EPMOD", ""))
import build_ep as B
from build_ep import tw, EPS

ENGINE = os.environ.get("ENGINE", "v1")
strip = lambda s: re.sub(r"\[\[|\]\]", "", s)
bad = 0
for n, ep in sorted(EPS.items()):
    covered = sorted(i for sc in ep["scenes"] for i in sc["lines"])
    if covered != list(range(len(ep["lines"]))):
        bad += 1; print(f"EP{n}: scenes do not cover lines 0..{len(ep['lines'])-1} exactly once -> {covered}")
    for i, ln in enumerate(ep["lines"]):
        nl = B.wrap(ln.get("cap", ln["say"])).count("<br>") + 1
        if nl > 3: bad += 1; print(f"EP{n} line {i}: caption wraps to {nl} lines (max 3) -> shorten: {ln.get('cap', ln['say'])[:40]}...")
    for k, sc in enumerate(ep["scenes"]):
        if sc["type"] == "cards":
            rows = sc["rows"]; N = len(rows)
            if N > 4: bad += 1; print(f"EP{n} s{k}: {N} rows (max 4)")
            if ENGINE == "v2":
                gap = 12; h = min(200, (460 - (N - 1) * gap) // N)
                two = any("<br>" in r["desc"] for r in rows)
                tf, df, bd = (52, 36, 72) if h >= 170 else (((44, 30, 64) if two else (46, 32, 64)) if h >= 125 else (40, 31, 56))
                base = 780 - 44 - 32 - bd - 16
            else:
                _, h, tf, df, av = B.rows_layout(N, bool(sc.get("header")))
                base = 780 - 44 - av - 20
            for r in rows:
                avail = base - (76 if r.get("mark") else 0)
                wt = tw(r["title"]) * tf
                lines = r["desc"].split("<br>")
                wd = max(tw(x) * df for x in lines)
                if wt > avail * 0.97: bad += 1; print(f"EP{n} s{k} title too wide: {r['title']} ({wt:.0f}>{avail})")
                if wd > avail * 0.97: bad += 1; print(f"EP{n} s{k} desc too wide: {r['desc']} ({wd:.0f}>{avail})")
                if h < 140 and len(lines) > 1: bad += 1; print(f"EP{n} s{k} 4-row card should have a 1-line desc: {r['title']}")
        elif sc["type"] == "versus":
            for side in ("left", "right"):
                d = sc[side]
                if not 2 <= len(d["items"]) <= 4: bad += 1; print(f"EP{n} s{k} {side}: items must be 2~4")
                if tw(d["title"]) * 42 > 316: bad += 1; print(f"EP{n} s{k} {side} title too wide: {d['title']}")
                for t in d["items"]:
                    if tw(t) * 32 > 2 * 296 * 0.97 or (tw(t) * 32 > 296 * 0.97 and "<br>" not in t and False): bad += 1; print(f"EP{n} s{k} {side} item too long: {t}")
                    if "<br>" not in t and tw(t) * 32 > 296 * 0.97: print(f"EP{n} s{k} {side} item wraps to 2 lines (ok if intended): {t}")
        elif sc["type"] == "exam":
            for x in sc["html"].split("<br>"):
                w = tw(strip(x)) * (46 if ENGINE == "v2" else 50)
                if w > 688 * 0.97: bad += 1; print(f"EP{n} s{k} exam line too wide: {strip(x)} ({w:.0f})")
        elif sc["type"] == "cta":
            btn = sum(tw(t) * 44 + 68 for t, _ in sc["buttons"]) + 20 * (len(sc["buttons"]) - 1)
            if btn > 736: bad += 1; print(f"EP{n} s{k} quiz buttons too wide ({btn:.0f})")
            if tw(sc["q"]) > 14.6: bad += 1; print(f"EP{n} s{k} quiz question long: {sc['q']}")
print("lint: no problems" if not bad else f"lint: {bad} problem(s)")
sys.exit(1 if bad else 0)
