#!/bin/sh
# Build the Liber Ventorum demo: reading check → frames → silent stereo track + light grain.
# LIB = the lemo-opuscar library folder (holds core/render). OUT = where the film goes.
# Linux without the bundled browser: PLAYWRIGHT_CHROME=/path/to/chrome sh build.sh
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
LIB=${LIB:-$HOME/lemo-opuscar}
OUT=${OUT:-$HERE/../out}
[ -f "$LIB/core/render/video.mjs" ] || { echo "set LIB to the lemo-opuscar library folder"; exit 1; }
mkdir -p "$OUT"
cd "$LIB"
node core/render/readcheck.mjs "$HERE"
node core/render/events.mjs "$HERE" --out "$OUT/events.json"
node core/render/video.mjs "$HERE" --fps 24 --workers 3 --out "$OUT/video.mp4"
# Silent master (music is added on each platform): a silent stereo AAC track and light film grain.
ffmpeg -v error -y -i "$OUT/video.mp4" -f lavfi -i anullsrc=r=48000:cl=stereo \
  -vf "noise=alls=2:allf=t" -c:v libx264 -preset medium -crf 21 -pix_fmt yuv420p \
  -c:a aac -b:a 128k -shortest -movflags +faststart "$OUT/liber-ventorum-demo.mp4"
echo "→ $OUT/liber-ventorum-demo.mp4"
