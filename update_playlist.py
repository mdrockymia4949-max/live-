import requests

SOURCE_URL = "https://raw.githubusercontent.com/sm-monirulislam/Toffee-Auto-Update-Playlist/refs/heads/main/toffee_data.json"

data = requests.get(SOURCE_URL).json()
channels = data.get("response", [])

m3u = '#EXTM3U\n'
m3u += '#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Linux; Android 14; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36\n\n'

for ch in channels:
    name = ch.get("name", "Unknown")
    link = ch.get("link", "")
    logo = ch.get("logo", "")
    group = ch.get("category_name", "Live")

    m3u += f'#EXTINF:-1 group-title="{group}" tvg-logo="{logo}",{name}\n'
    m3u += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Linux; Android 14; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36\n'
    m3u += f"{link}\n\n"

with open("toffee_playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u)

print(f"✅ Updated {len(channels)} channels")
