# Music Cover Maker

A small Python utility that embeds cover art into an MP3 file's ID3 tags so the artwork shows up in Windows Explorer, Google Drive, and music players.

## How it works
1. Opens the MP3 and adds ID3 tags if missing
2. Removes any existing (possibly broken) embedded images
3. Embeds your image as the **Front Cover** (APIC type 3)
4. Saves as **ID3v2.3** for maximum compatibility

## Usage
```bash
pip install -r requirements.txt
```
Edit `AUDIO_FILE` and `IMAGE_FILE` at the top of `Music_Cover_Maker.py`, then:
```bash
python Music_Cover_Maker.py
```
