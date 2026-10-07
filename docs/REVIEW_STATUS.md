# Version 1.0 review status

## Checked

- Two decks contain 104 notes/cards each.
- Each has four subdecks with 46, 20, 5, and 33 cards.
- Front includes a typed romaji answer field.
- Back retains typed-answer comparison and omits the duplicate plain romaji line.
- All referenced images and audio files are bundled.
- Audio clips regenerated from one decoded WAV to avoid invalid short MP3s caused by repeated direct MP3 decoding/seeking.
- Credits retain source and license links and distinguish SpeechGen audio.
- Sample layout and typing were tested by the project creator in Anki.

## Still to review

- Full pronunciation and clip-to-character alignment. Boundaries were detected from pauses and labels follow the supplied input order; no independent native-speaker certification was performed.
- In particular: は/ハ, へ/ヘ, を/ヲ, ん/ン, and voiced/combined sounds.
- All 208 card appearances on desktop and mobile, including mnemonic crops.
- The content of the workbooks before classroom use; this package preserves the completed workbook files rather than reauthoring them.

## Design limits

- One canonical typed answer; alternative romanization variants may be highlighted as incorrect.
- Modified kana and combinations reuse base-character artwork, not a newly drawn mnemonic for every sound.
- Long vowels, small っ/ッ, loanword combinations, and word exercises are outside the four current subdecks.
- Anki import may keep previously installed templates. Edit the installed note type through Cards… when necessary.

Please report the script and kana when flagging a problem.
