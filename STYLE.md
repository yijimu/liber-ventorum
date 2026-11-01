# Liber Ventorum 风起之书 — Style Prompt

Made from a blank page; techniques from Visual Investigation (visual-investigation) in Lemo-Opuscar, with moves borrowed from Archive Light Table (archive-lighttable) and Data Storytelling (dataviz).

> A dark reading room at night. Objects from one era (bamboo slips, a bronze tally, a law code, a paper banknote, a star chart) lie on a warm black table under one low lamp, drawn entirely in code. Every screen carries the same two signs: a **year stamp** at the top left (year · place) that rolls like an odometer when time moves, and a **source card** at the top right (the original book title with a red seal). The story is told only in on-screen captions, one line at a time, keywords in gold. The sky is the film's clock: when Jupiter and Saturn meet, a gust of wind blows the objects of one era into light, and the light settles into the next.
> References (grammar only): museum night-lighting of single objects; archive documentaries that push into one line of a page; data stories where one dot is a character. Copy none of their layouts, typefaces, shots or music, and never name them in the film.

## 1. Essence, and what it is not

1. **One era, one object, one line.** Each shot shows one object, one number or one quoted line, and says one thing about it. The object is the evidence; the caption is the reading.
2. **Time is read in the picture.** The year stamp is always on screen and always true. When the story jumps, the stamp rolls (2026 → 前 464 → 约前 300) instead of a title card announcing it.
3. **Every claim wears its source.** A shot that quotes or counts something shows the original title in the source card. No source, no card; never a fake one.
4. **Silence carries the voice.** There is no narrator. Captions are the voice, written as spoken second-person lines ("假如你……"), paced for reading, never for a soundtrack. Music is added by the platform afterwards; the film itself is silent.
5. **Restraint.** War, plague and massacre are shown as numbers, dots and a darkened region, never as bodies, fire or spectacle.

Not **Visual Investigation** (no cold blue-grey desk, no real footage grid, no white flashes, no stopwatch). Not **Archive Light Table** (no backlit glass, no hands; objects lie in lamplight, not transmitted light). Not a keynote (no bullet lists, no slide turns). Not an AI-video montage (no generated photorealistic people, no morphing faces). Not a fantasy/astrology aesthetic (no glowing runes, purple nebulae or tarot frames).

## 2. Materials & rendering

- **Ground**: warm black `#0E0C0A`, a soft radial lamp pool (centre +6 % luminance, corners −35 %), a faint paper-fibre texture (static, seeded, α ≈ 0.05). Film grain is added at mux time only (`mux.sh … 2`), never in the page.
- **Objects are drawn, not photographed.** Bamboo slips, bronze, paper, silk, stone are built in Canvas 2D (or three.js for a turning object) with one key light from the upper left (warm, ≈ 3200 K), a cast shadow to the lower right, and a thin rim highlight in gold on the lit edge. Material is told by gradient and edge, not by texture photos.
- **Text on objects** (slips, codes, notes, coins) is typeset by code from a checked transcription, in ink `#2A1D10` on the object, and the decisive characters are lit in gold when they are read. Label it as a transcription in `FACTS.md`, never pass it off as a scan.
- **Sky**: a seeded star field (≈ 900 stars, 3 magnitudes), a thin ecliptic arc, zodiac signs as sectors (tropical signs, labelled `示意`), planets as discs with soft glow: Jupiter gold, Saturn pale gold with a hairline ring.
- **Maps**: line drawings only (coast and rivers in paper colour α 0.5, no filled countries), regions marked by a dashed outline or a darkening, labelled with historical state names. Follow DIRECTOR.md's map rules; a historical map is always marked `示意`.
- **Data**: counters in mono, dots for people (one dot = N people, stated once), small line charts drawn stroke by stroke in paper colour with the one value that matters in gold.
- Real archival images (public domain or CC BY only, TECHNIQUE.md §11) may appear inside a frame on the table, graded warm monochrome (`sepia(.35) grayscale(.6) contrast(1.08) brightness(.88)`); never generated images standing in for history.

## 3. Colour logic

| Use | Value |
|---|---|
| Ground | `#0E0C0A` |
| Raised surfaces, panels | `#17140F` |
| Hairlines, frames, ecliptic | `#3A3226` |
| Text, line work, paper | `#E8DCC0` |
| Secondary text | `#9C8F78` |
| **Gold: the thing being read** (keyword, planet, the decisive number or character) | `#C9A45C` |
| **Seal red: the source seal, and one turning point per film** | `#A8322A` |
| Ink on objects | `#2A1D10` |

Gold points; it never decorates. At most two gold things on screen at once. Seal red appears in every source seal and **once more per film** for the turning point (a battle region darkening, a broken law, a currency collapsing); a second red moment cheapens the first.

## 4. Type & captions

- **Chinese**: Noto Serif SC (OFL). Captions 500, titles 700–900. **Latin**: Cormorant SC 500, tracked +18 %, for the series line `LIBER VENTORUM` and Latin book titles. **Numbers, degrees, counters**: IBM Plex Mono 400/500. Subset fonts to the film's characters.
- **Year stamp** (top left, x 64, y 52): the year in Noto Serif SC 600, 46 px, paper colour (`前 464`, `约前 300`, `1233`, `2020.12.21`); under it the place in 22 px secondary (`齐 · 临淄 · 稷下`). Digits roll vertically like an odometer when the year changes (0.8–1.6 s, ease in-out); the place cross-fades. Never hidden, except on the title and end cards.
- **Source card** (top right, right edge x 1856, y 52): the original title in 26 px paper colour (`《史记·田敬仲完世家》`), and to its right a 44 px square seal in seal red with the two characters `风起` cut out in 白文 (paper colour), slightly rotated (−2°) with a rough edge. Fades in 0.4 s after the claim appears; swaps with a 0.3 s cross-fade.
- **Captions** (the film's only voice): one line, centred, baseline y ≈ 1000, Noto Serif SC 500, 40 px, paper colour, max width 1,500 px, no box, no outline, a soft dark shadow (0 2 12 px rgba(0,0,0,.6)). Keywords (1–2 per line) in gold. A long sentence becomes two captions. Fade in 0.35 s, out 0.35 s, never typed on.
- **Reading time**: every caption and every key text stays still and whole for CJK ÷ 4.5 + other ÷ 15 + 1.5 s (`readcheck.mjs`, exact). Counters and tick labels are exempt. The caption is the pace of the film: shots are cut to the captions, not the other way round.
- **Few words on screen.** Besides the caption: the year stamp, the source card, and at most one readout (a number, a degree, a short label). No eyebrows, no English twins, no footnotes.

## 5. Motion quality

- 24 fps. Everything moves slowly and continuously, as if read by lamplight: pushes ≤ 1.25× over a shot, drifts ≤ 40 px, objects settle with ease-out (0.6–1.2 s), never bounce or pop.
- **Transitions**: *dark down / light up* (the lamp dims to the ground in 0.5 s, the next shot lights up in 0.6 s) between shots inside an era; the **wind** (§8) between eras. No hard cuts with flashes, no wipes, no slide turns.
- Things that are drawn are progressive: line maps stroke by stroke, chart lines left to right, characters lit one by one along the reading order (top to bottom, right to left on slips), 0.12–0.2 s per character.
- Something changes at least every 1.5 s (a light, a character, a drift); holds are for the closing question only.

## 6. Shot & layout grammar

- 1920×1080, 64 px margins. Top band (y 40–130) belongs to the year stamp (left) and the source card (right); content y 150–930; the caption lives at y ≈ 960–1030 and nothing else does.
- **Typical shots**: one object on the table, slightly off-centre, under the lamp; **loupe on a line** (a 150 px-radius magnifier over the decisive characters); **sky** (planets converging over the ecliptic, one mono readout `天秤 3.9° · 1 / 136`); **line map** with one region marked; **counter** (a large mono number climbing to its value, `1,470,000`); **three objects in a row** (what an era left behind), each lighting up in turn.
- **Title card**: `LIBER VENTORUM` (Cormorant SC, gold, 30 px, tracked) over the episode title (Noto Serif SC 900, 88 px), centred, no year stamp.
- **End card**: the series line `借你一阵风，看看你会成为谁。` (40 px), the references as a short list of titles (22 px secondary), and one 18 px line: `风象时代为西方占星说法，本片只作一面镜子；合相年份由作者以天文软件计算；画面为 AI 生成动画。`

## 7. Sound palette

The master is **silent**: no voice, no music, no foley. Music is added on each platform. Deliver a silent stereo AAC track so platforms accept the file, and keep `EV` cue events in the page (`wind`, `seal`, `light`) so a future version can add sound without re-timing.

## 8. Native moves (and how to code them)

- **The wind (the signature, once per era change).** Two planets meet; a soft gold bloom (not white) swells from the meeting point; every star and the objects of the old era break into light motes (≈ 1,200 seeded particles), carried along one curved gust across the frame with curl noise; the motes slow and settle onto the outlines of the next era's object, which then fills in from its edges. Particle paths are a pure function of t (start point, target point, per-particle delay, noise phase): any frame renders alone. *Fits:* every jump between air eras.
- **Odometer year.** The year stamp rolls digit by digit from one year to the next; BCE/CE switches by cross-fading the `前` prefix at year 1. *Fits:* every jump in time.
- **Loupe on the line.** A magnifier (black ring, gold hairline bevel, 2.4×, slight pincushion at the rim) slides onto the decisive characters; inside the lens the characters turn gold one by one. Drawn from an offscreen canvas of the same layer, so the lens is never a separate picture. *Fits:* 不治而议论; a seal on a banknote; a clause in a law code.
- **Counter to a life-size number.** A mono counter climbs to the number while dots fill a grid (one dot = 10,000 people). *Fits:* 1,470,000 people of Bianliang.
- **What was left.** At an era's end the lamp dims and only the object that survived keeps glowing. *Fits:* "风吹散了七个国家，留下来的，是一卷《荀子》。"
- **The empty place.** At the series' present day, the objects of past eras glow in a row, with one place left empty for "you". *Fits:* the flagship's ending.

## 9. Pitfalls

- **Anachronism in the stamp.** The year stamp must match the object and place (稷下 flourished c. 前 319–前 284; do not stamp it 前 464). When the story's year and the object's year differ, roll the stamp.
- **Astrology passed off as history.** Air eras are a Western astrological frame; say so once per film (end card) and never claim the sky caused events.
- **Invented quotes.** Every quoted line has a source in `FACTS.md`; captions that paraphrase (白话) do not wear quotation marks.
- **Too much gold.** Gold everywhere is no gold. Two gold things at most; red once.
- **Captions too fast.** Without a voice, a caption that leaves early is lost. Run `readcheck.mjs` every render.
- **Dark crush.** On phones the ground can swallow line work; keep line work at ≥ α 0.5 and test the poster frame at 50 % brightness.
- **Political mapping.** Never map ancient states or dynasties onto present-day countries or politics, in pictures or captions.
- **Spectacle of suffering.** No blood, bodies or fire; numbers and a darkened region.

## 10. Material (素材)

1. Ask the user first for their own scans, photos or data.
2. Prefer drawing in code; when a real object helps (杜虎符, a 中统钞 plate), use only public-domain or CC BY images, credited on the end card, graded as in §2.
3. Transcriptions of classical text come from a checked edition; record the edition in `FACTS.md`.

## 11. Facts

Keep `FACTS.md`: each caption or on-screen claim → source (book, chapter) → original wording; each year stamp → why that year; every inference listed separately.

## 12. Engine

- One Canvas-2D page (`demo/index.html`), `window.render(t)` deterministic, `window.TEXTS(t)` for `readcheck.mjs`, `window.EV` for cues, all timing in one `SHOTS` / `CAPS` table at the top of the page.
- Reusable parts in `demo/index.html`: `ground()` (lamp pool + fibre), `yearStamp()` (odometer), `sourceCard()` (title + seal), `caption()` (one line, gold keywords), `sky()` (stars, ecliptic, planets), `wind()` (particle gust between two point sets), `slips()` (bamboo slips with typeset text and per-character light), `loupe()` (magnifier over an offscreen layer), `titleCard()`, `endCard()`.
- Fonts: `demo/tools/subset.py` subsets the OFL fonts to the film's text.
- Build: `demo/build.sh` (render → silent track → mux with grain).

## 13. Variation space

The agent decides per film: the era, the object, the order of shots, which native moves beyond the wind, the opening and the ending.

- **Three structures:** "假如你是 X" (one object or person through its life); "四次醒来" (one viewer across several eras, the wind between them); "一个数字" (one number opened up shot by shot).
- **Three openings:** the sky converging; an object already under the loupe; the year stamp rolling over black.
- **Three endings:** what was left (one object glowing); a question to the viewer held on the table; the empty place among the objects.
