# Liber Ventorum — demo film

One example among many. Don't reuse its story, arc, shots, props or timings.

**第一次起风 · 前 464**, 38 s, 1920×1080, 24 fps, silent master.

## Story

The sky over 2026 rolls back to 前 464: Jupiter and Saturn meet in Libra (3.9°). The wind blows the stars into light, and the light settles into a bundle of bamboo slips from 稷下 (约前 300). A loupe finds 不治而议论. Dark down; a second bundle lights up with 荀子's 天行有常. Only the slips keep glowing, then the series card.

## Shots

| t (s) | Shot | Signature on screen |
|---|---|---|
| 0.0–5.6 | Sky: planets converge along the ecliptic, readout `天秤 3.9°` | Year stamp rolls 2026 → 前 464 (odometer) |
| 5.6–9.8 | **The wind**: gold bloom, 1,300 motes, settle into slips | Native move |
| 9.8–22.5 | Scroll 1 (《史记·田敬仲完世家》), loupe on 不治而议论, characters turn gold | Year stamp rolls to 约前 300; source card + seal |
| 22.5–23.4 | Dark down / light up | Transition |
| 23.4–30.4 | Scroll 2 (《荀子·天论》), 天行有常 lit character by character; the rest dims, the slips keep glowing | Gold for the line read |
| 30.6–38.2 | End card: LIBER VENTORUM / 风起之书 / slogan / references / disclaimer | Title and end card |

## Palette, type, sound

Palette and type as `STYLE.md` §3–4. No voice, no music: a silent stereo AAC track; `EV` keeps `wind`, `seal`, `light` cues for a later sound pass.

## Build

`demo/build.sh` (needs the lemo-opuscar library as `LIB`): reading check → `events.mjs` → `video.mjs` → ffmpeg (silent track + `noise=alls=5:allf=t` grain). Fonts are subset by `demo/tools/subset.py` from the OFL originals (Noto Serif SC, Cormorant SC, IBM Plex Mono).

## Which part draws what (`demo/index.html`)

`ground()` lamp pool and fibre · `yearStamp()` odometer · `seal()` + `sourceCard()` · `caption()` gold keywords · `sky()` stars, ecliptic, planets · `wind()` particle gust · `drawSlips()` bamboo slips with per-character light · `loupe()` magnifier over the offscreen layer · `endCard()`.
