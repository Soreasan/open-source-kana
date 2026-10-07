# Sources and attribution

## Mnemonics

**B. Domangue (LeafPiece), 2016 — Japanese Kana Mnemonic Chart**

- Source: https://commons.wikimedia.org/wiki/File:Japanese_Kana_Mnemonic_Chart.png
- License: https://creativecommons.org/licenses/by-sa/4.0/
- Used in: `assets/mnemonics/`, source-chart copies, workbooks, and Anki card fields.
- Changes: mnemonic illustrations are cropped and resized from the original chart. Some illustrations were cleaned to remove stray text or marks.

## Hiragana stroke order

**Pmx, 2007, based on Karine Widmer's table — Table hiragana.svg**

- Source: https://commons.wikimedia.org/wiki/File:Table_hiragana.svg
- Original vector: https://upload.wikimedia.org/wikipedia/commons/2/28/Table_hiragana.svg
- License: https://creativecommons.org/licenses/by-sa/3.0/
- Changes: diagrams were rendered at high resolution, cropped, and resized. The repository includes the crops and raster chart embedded in the workbook; the original SVG is linked rather than bundled.

## Katakana stroke order

**Pmx — Table katakana.svg**

- Source: https://commons.wikimedia.org/wiki/File:Table_katakana.svg
- License: https://creativecommons.org/licenses/by-sa/3.0/
- Changes: diagrams were rendered at high resolution, cropped, and resized. The repository includes the crops and raster chart embedded in the workbook; obtain the original SVG from its Commons page if needed.

## Overview charts

**TealComet — Hiragana/Katakana Chart Seion Dakuon Yoon**

- Hiragana: https://commons.wikimedia.org/wiki/File:Hiragana_Chart_Seion_Dakuon_Yoon.png
- Katakana: https://commons.wikimedia.org/wiki/File:Katakana_Chart_Seion_Dakuon_Yoon.png
- License: https://creativecommons.org/publicdomain/zero/1.0/
- Changes: cropped/resized sections; adapted overview layout, corrected basic-row positions, and common combinations shown in the workbooks.

## Audio

**AI-generated pronunciation — SpeechGen Asuka, 80% speed**

- Generator: https://speechgen.io/en/tts-japanese/
- Published usage policy: https://speechgen.io/en/node/privacy/ (section 4).
- Generated and supplied by Soreasan / ソレアサン on October 6, 2026.
- Original: `assets/audio/original/asuka-80-percent.mp3`. A decoded WAV master is also bundled for reliable splitting; converting to WAV does not add source fidelity.
- Changes: split into clips with small leading/trailing silence margins; re-encoded as MP3. Re-encoding does not add source fidelity.
- Licensing: separate service usage terms; not represented as CC BY-SA audio.
- Feedback: GitHub Issues after publication, or the person supplying the archive before publication.

## Original contributions and tools

**Soreasan / ソレアサン**, with AI assistance — educational text/design and project assembly. See `LICENSE.md` for scope. Individual kana and unprotected facts are not claimed as exclusive property.

Deck packages are produced with [genanki](https://github.com/kerrickstaley/genanki), which has its own MIT license. Audio splitting uses [FFmpeg](https://ffmpeg.org/); no FFmpeg executable is bundled. The project does not include Tofugu artwork, audio, or deck source code.

The attributions above were carried forward from the completed workbook source notices. See the respective Commons pages for original source records.
