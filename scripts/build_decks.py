#!/usr/bin/env python3
"""Build both decks from editable JSON, templates, and bundled media."""
import argparse,json,re
from pathlib import Path
import genanki

def build(root, output):
    output.mkdir(parents=True, exist_ok=True)
    media = {p.name:p for p in (root/'assets').rglob('*') if p.is_file()}
    for script in ('hiragana','katakana'):
        data=json.loads((root/f'anki/{script}.json').read_text(encoding='utf-8'))
        model=genanki.Model(data['model_id'],data['model_name'],
            fields=[{'name':x} for x in data['field_names']],
            templates=[{'name':'Read and type','qfmt':(root/'anki/front.html').read_text(encoding='utf-8'),
                        'afmt':(root/'anki/back.html').read_text(encoding='utf-8')}],
            css=(root/'anki/style.css').read_text(encoding='utf-8'))
        decks={d['id']:genanki.Deck(d['id'],d['name'],description=d['description']) for d in data['decks']}
        used=set(); guids=set()
        for card in data['cards']:
            if card['guid'] in guids: raise ValueError('Duplicate card GUID')
            guids.add(card['guid'])
            fields=[card['fields'][x] for x in data['field_names']]
            for name in re.findall(r'(?:src="|\[sound:)([^"\]]+)', '\n'.join(fields)):
                if name not in media: raise FileNotFoundError(f'Missing media: {name}')
                used.add(name)
            decks[card['deck_id']].add_note(genanki.Note(model=model,fields=fields,tags=card['tags'],guid=card['guid']))
        package=genanki.Package(list(decks.values()));package.media_files=[str(media[n]) for n in sorted(used)]
        path=output/f'Open-Source-{data["script"]}.apkg';package.write_to_file(str(path))
        print(f'{path.name}: {len(data["cards"])} cards, {len(used)} media files')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(); root=args.root.resolve()
    build(root,args.output.resolve() if args.output else root/'dist')
