# -*- coding: utf-8 -*-
# 완성된 mp4를 "교시_과목/EPnn_주제.mp4" 폴더로 정리하고 zip(무압축)으로 묶는다.
#   REELS_WORK=<작업폴더> REELS_CONTENT=<examples> python3 scripts/package_by_area.py <출력폴더> [교시 필터...]
# AREAS를 프로젝트에 맞게 고친다: (폴더명, episodes 모듈, {번호: mp4 경로}, {번호: 주제 덮어쓰기})
import os, re, shutil, sys, zipfile
R = os.environ["REELS_WORK"]; EX = os.environ.get("REELS_CONTENT", "examples")
OUT = sys.argv[1]; only = sys.argv[2:]
def S(series, n): return f"{R}/{series}/reel_ep{n}.mp4"
AREAS = [
    ("1교시_사회복지조사론", "episodes_josaron_v2", {n: S("series_josa2", n) for n in range(1, 10)}, {1: "신뢰도_vs_타당도"}),
    ("1교시_인간행동과사회환경", "episodes_hbse_v2", {n: S("series_hbse2", n) for n in range(1, 11)}, {}),
    ("2교시_사회복지실천론", "episodes_prac_v2", {n: S("series_prac2", n) for n in range(1, 11)}, {}),
    ("2교시_사회복지실천기술론", "episodes_tech", {n: S("series_tech", n) for n in range(1, 10)}, {}),
    ("2교시_지역사회복지론", "episodes_community", {n: S("series_community", n) for n in range(1, 10)}, {}),
    ("3교시_사회복지정책론", "episodes_policy", {n: S("series_policy", n) for n in range(1, 10)}, {}),
    ("3교시_사회복지행정론", "episodes_admin", {n: S("series_admin", n) for n in range(1, 8)}, {}),
    ("3교시_사회복지법제론", "episodes_law", {n: S("series_law", n) for n in range(1, 9)}, {}),
]
def topics(mod):
    d = {}; exec(open(f"{EX}/{mod}.py", encoding="utf-8").read(), d)
    t = {}
    for n, ep in d["EPS"].items():
        hs = [s for s in ep["scenes"] if s["type"] == "hook"]
        hl = hs[0].get("headline") or " ".join(hs[0].get("words", [])) if hs else f"EP{n}"
        t[n] = re.sub(r"\s+", "_", re.sub(r"<br>|\[\[|\]\]|[·&]", " ", hl).strip())
    return t
os.makedirs(OUT, exist_ok=True)
for name, mod, files, extra in AREAS:
    if only and not any(o in name for o in only): continue
    t = topics(mod); t.update(extra)
    d = f"{OUT}/{name}"; os.makedirs(d, exist_ok=True)
    for n, src in sorted(files.items()):
        if os.path.exists(src): shutil.copy(src, f"{d}/EP{n:02d}_{t.get(n, '')}.mp4")
        else: print("missing", name, n)
    with zipfile.ZipFile(f"{OUT}/{name}.zip", "w", zipfile.ZIP_STORED) as z:
        for f in sorted(os.listdir(d)): z.write(f"{d}/{f}", f"{name}/{f}")
    print(name, len(os.listdir(d)), "files ->", f"{name}.zip")
