# Open Source Kana

Free Hiragana and Katakana workbooks and typed-answer Anki decks for individual learners, study groups, and classrooms.

Created by **Soreasan / ソレアサン**, with AI assistance. Pronunciation audio is synthesized, not a human recording.

## Downloads

The starter archive includes ready-to-import packages in `releases/v1.0.0/`:

- **Open Source Hiragana** — 104 cards
- **Open Source Katakana** — 104 cards

Each deck has four numbered subdecks: basic kana (46), dakuten (20), handakuten (5), and yōon (33). The editable workbooks are in `workbooks/`.

After publishing this repository, attach the finished packages and workbooks to a GitHub Release and add its link here. The repository name and GitHub account URL have deliberately not been guessed.

## Using the decks

Import the `.apkg` into Anki. The front shows the kana and an answer box. Type lowercase romaji, reveal the answer, then select your review rating. The back includes the green/red comparison, audio, a mnemonic, base-character stroke order, and expandable source credits.

Use `shi`, `chi`, `tsu`, `fu`, `ji`, and `sha/shu/sho`. Type `wo` for を/ヲ, although its usual pronunciation is `o`. Type `ji` for ぢ/ヂ and `zu` for づ/ヅ; these usually share the pronunciations of じ/ジ and ず/ズ in standard Japanese. The built-in comparison uses one canonical answer; alternative romanization spellings are not accepted automatically.

Modified kana and yōon reuse the base-character artwork with an explanatory note. Their stroke-order picture illustrates the **base character**, not the full combination. Loanword combinations and long-vowel/small-っ examples are not included in these four subdecks.

## Repository layout

| Path | Contents |
| --- | --- |
| `workbooks/` | Editable PowerPoint workbooks |
| `anki/` | Editable card data, front/back HTML, and CSS |
| `assets/mnemonics/` | Cropped mnemonic illustrations |
| `assets/stroke-order/` | Cropped stroke-order diagrams |
| `assets/source-charts/` | Full chart images embedded in the workbooks |
| `assets/audio/` | Original 80% recording, decoded WAV master, 138 clips, and boundary index |
| `scripts/` | Portable deck builder and audio splitter |
| `docs/` | Attribution, review status, and GitHub setup instructions |
| `releases/v1.0.0/` | Prepared Anki packages for an initial release |

The original external SVG source files are linked in `docs/ATTRIBUTION.md`; the bundled full chart images are the raster copies actually embedded in the workbooks.

## Rebuild the decks

Requires Python 3.10 or later. From the repository root:

```sh
python -m venv .venv
python -m pip install -r requirements.txt
python scripts/build_decks.py
```

Activate `.venv` before installing: on Windows PowerShell use `.venv\Scripts\Activate.ps1`; on macOS/Linux use `source .venv/bin/activate`. If PowerShell blocks activation, use `.venv\Scripts\python.exe` instead of `python` in the remaining commands.

Generated packages go to `dist/`. This build needs no API key or online TTS service. It uses the supplied audio clips and images. Stable note GUIDs are retained across builds; avoid changing them for routine content corrections.

## Edit cards or appearance

Edit `anki/hiragana.json` or `anki/katakana.json` for content. Each entry has a stable GUID, subdeck ID, tags, and named fields. Edit `front.html`, `back.html`, or `style.css` for presentation, then rebuild.

Anki may preserve an existing note type's templates when importing an updated package. To apply a template change to an installed deck, open **Browse → select a card → Cards…** and update the template there. Do not delete cards merely to apply HTML changes. Both complete decks share the `Open Source Kana · Typed Romaji` note type.

## Recreate audio clips

Install FFmpeg and add it to PATH, then run:

```sh
python scripts/split_audio.py
```

The index contains 138 recordings: 104 deck entries, 28 additional loanword combinations, and six example words. Only the first 104 are used in these decks. The clips were matched using the supplied text order and pauses. **The full audio set has not received an independent pronunciation review.** See `docs/REVIEW_STATUS.md`.

## Sharing and licenses

You are welcome to edit and share this project under the applicable terms. This is a mixed-license project, not a blanket CC license for every file:

- Original educational contributions: CC BY-SA 4.0, to the extent copyrightable rights are held.
- Mnemonic artwork: B. Domangue (LeafPiece), CC BY-SA 4.0.
- Stroke-order artwork: Pmx, CC BY-SA 3.0; Hiragana based on Karine Widmer's table.
- Overview charts: TealComet, CC0 1.0.
- Audio: AI-generated using SpeechGen Asuka at 80% speed; separate SpeechGen usage terms.
- Original build scripts: MIT, to the extent copyrightable rights are held. Third-party dependencies retain their licenses.

See `LICENSE.md`, `LICENSE-CODE.txt`, and `docs/ATTRIBUTION.md`. Preserve source credits when sharing edited decks or workbooks. A CC notice does not create copyright in otherwise unprotected AI-generated material.

## Feedback

Once hosted on GitHub, use this repository's **Issues** to report problems. Include the script, kana, affected file, Anki version/device, and what seems wrong. If this archive is shared before the repository exists, contact the person who provided it. Please report audio errors before treating version 1.0 as a fully reviewed pronunciation resource.
