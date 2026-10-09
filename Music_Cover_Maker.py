from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
import os

# ========================================================
#             SETTINGS
# ========================================================
AUDIO_FILE = "Apple_in_China_Complete.mp3"
IMAGE_FILE = "cover.png"

def embed_album_art():
    print(f"🎨 Embedding '{IMAGE_FILE}' into '{AUDIO_FILE}'...")

    if not os.path.exists(AUDIO_FILE):
        print(f"❌ Error: Audio file '{AUDIO_FILE}' not found.")
        return
    if not os.path.exists(IMAGE_FILE):
        print(f"❌ Error: Image file '{IMAGE_FILE}' not found.")
        return

    # 1. Open the MP3
    audio = MP3(AUDIO_FILE, ID3=ID3)

    # 2. Add ID3 tags if missing
    try:
        audio.add_tags()
    except error:
        pass

    # 3. DELETE existing broken images (Start fresh)
    audio.tags.delall("APIC")

    # 4. Read the image data
    with open(IMAGE_FILE, 'rb') as img:
        img_data = img.read()

    # 5. Add the Image Tag (APIC)
    # Critical: Google Drive/Windows prefer 'front cover' type and specifically 'image/jpeg' or 'image/png'
    audio.tags.add(
        APIC(
            encoding=3,          # 3 = UTF-8
            mime='image/png',    # Ensure this matches your file (png/jpeg)
            type=3,              # 3 = Front Cover (Important!)
            desc=u'Cover',
            data=img_data
        )
    )

    # 6. SAVE AS ID3v2.3 (The "Compatibility Mode")
    # v2=3 forces the older standard that Google Drive & Windows prefer.
    audio.save(v2_version=3)

    print("✅ Success! Saved with ID3v2.3 compatibility.")
    print("   -> Upload to Google Drive again to test.")

if __name__ == "__main__":
    embed_album_art()