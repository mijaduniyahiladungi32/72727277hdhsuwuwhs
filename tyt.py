#!/usr/bin/python3
import subprocess

YOUTUBE_LIVE_URL = "https://www.youtube.com/live/eI2P6__3Veg?si=rNvSCw8DlfskzU5G"

def get_stream_url(url):
    try:
        result = subprocess.run(
            ["yt-dlp", "-g", url],
            capture_output=True, text=True, timeout=30
        )
        output = result.stdout.strip()
        if output and ".m3u8" in output:
            return output
        else:
            return None
    except Exception as e:
        print(f"[ERROR] {e}")
        return None

if __name__ == "__main__":
    print(f"[INFO] Fetching stream for: {YOUTUBE_LIVE_URL}")
    stream_url = get_stream_url(YOUTUBE_LIVE_URL)

    if stream_url:
        print(f"[✅] Found stream URL:\n{stream_url}")
    else:
        print("[❌] No .m3u8 stream found or video is not live.")
