#!/usr/bin/env bash
# One-time setup of a reels workspace: fonts, GSAP, paper texture, python venv (edge-tts).
# Usage: REELS_WORK=/path/to/work bash setup.sh      (default: ./reels_work)
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
WORK=${REELS_WORK:-$PWD/reels_work}
mkdir -p "$WORK/assets_src/fonts" "$WORK/_dl"
cd "$WORK/_dl"

echo "[1/4] fonts + gsap from the npm registry (CDNs are often blocked, npm is not)"
npm pack @fontsource/black-han-sans @fontsource/noto-sans-kr gsap@3.15.0 >/dev/null
for f in *.tgz; do d="${f%.tgz}"; mkdir -p "$d"; tar xzf "$f" -C "$d"; done
BH=$(ls -d fontsource-black-han-sans-*/package/files); NS=$(ls -d fontsource-noto-sans-kr-*/package/files)
cp "$BH/black-han-sans-korean-400-normal.woff2" "$WORK/assets_src/fonts/display-ko.woff2"
cp "$BH/black-han-sans-latin-400-normal.woff2"  "$WORK/assets_src/fonts/display-latin.woff2"
cp "$NS/noto-sans-kr-korean-700-normal.woff2"   "$WORK/assets_src/fonts/body-ko.woff2"
cp "$NS/noto-sans-kr-latin-700-normal.woff2"    "$WORK/assets_src/fonts/body-latin.woff2"
cp "$NS/noto-sans-kr-korean-900-normal.woff2"   "$WORK/assets_src/fonts/black-ko.woff2"
cp "$NS/noto-sans-kr-latin-900-normal.woff2"    "$WORK/assets_src/fonts/black-latin.woff2"
cp gsap-*/package/dist/gsap.min.js "$WORK/assets_src/gsap.min.js"

echo "[2/4] python venv with edge-tts, numpy, pillow"
if [ ! -x "$WORK/venv/bin/python" ]; then
  if command -v uv >/dev/null; then uv venv "$WORK/venv" --python 3.12 >/dev/null 2>&1 || uv venv "$WORK/venv" >/dev/null
  else python3 -m venv "$WORK/venv"; fi
fi
if command -v uv >/dev/null; then VIRTUAL_ENV="$WORK/venv" uv pip install -q edge-tts numpy pillow
else "$WORK/venv/bin/pip" install -q edge-tts numpy pillow; fi

echo "[3/4] paper texture (for the paper/orange style)"
"$WORK/venv/bin/python" "$HERE/paper.py" "$WORK/assets_src/paper.jpg" "${PAPER_BASE:-212,230,204}"

echo "[4/4] tools check"
for t in ffmpeg ffprobe node npm; do command -v $t >/dev/null && echo "  ok: $t" || echo "  MISSING: $t"; done
echo "workspace ready: $WORK"
