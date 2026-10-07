#!/usr/bin/env python3
"""Recreate the 138 indexed clips; requires FFmpeg on PATH.

The supplied index records the initial silence-based alignment. It is not
speech recognition or a certification of pronunciation. Edit Start/End after
listening if needed. These values mark speech boundaries, not padded boundaries.
"""
import argparse,csv,shutil,subprocess,tempfile,wave
from pathlib import Path

def split(root, output):
    if not shutil.which('ffmpeg'): raise SystemExit('Install FFmpeg and add it to PATH first.')
    output.mkdir(parents=True,exist_ok=True)
    source=root/'assets/audio/original/asuka-80-percent.mp3'
    with (root/'assets/audio/clip-index.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    # Decode once: repeated direct seeks into the supplied MP3 yielded invalid short clips.
    scratch=tempfile.TemporaryDirectory()
    decoded=Path(scratch.name)/'source.wav'
    bundled_pcm=root/'assets/audio/original/asuka-80-percent.wav'
    if bundled_pcm.exists():
        decoded=bundled_pcm
    else:
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(source),'-c:a','pcm_s16le',str(decoded)],check=True)
    with wave.open(str(decoded),'rb') as wav:
        rate=wav.getframerate(); channels=wav.getnchannels(); width=wav.getsampwidth(); pcm=wav.readframes(wav.getnframes())
    if width!=2:raise ValueError('Expected 16-bit PCM master')
    for row in rows:
        start=max(0,float(row['Start'])-.04);end=float(row['End'])+.08
        if int(row['Order'])==len(rows):end=float(row['End'])
        name=row['Filename']
        if Path(name).name!=name:raise ValueError('Clip filename must be a basename')
        clip=pcm[int(start*rate)*channels*width:int(end*rate)*channels*width]
        if not clip:raise ValueError(f'Empty PCM clip: {name}')
        subprocess.run(['ffmpeg','-v','error','-y','-f','s16le','-ar',str(rate),'-ac',str(channels),'-i','pipe:0',
                        '-c:a','libmp3lame','-b:a','96k',str(output/name)],input=clip,check=True)
    scratch.cleanup()
    print(f'Created {len(rows)} clips. Listen to verify the indexed labels and boundaries.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--output',type=Path)
    a=p.parse_args();root=a.root.resolve();split(root,a.output.resolve() if a.output else root/'assets/audio/clips')
