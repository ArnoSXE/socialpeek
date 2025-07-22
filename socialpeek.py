import requests
import argparse

def check_username(username):
    platforms = {
       "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "YouTube": f"https://www.youtube.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}/",
        "Tumblr": f"https://{username}.tumblr.com",
        "Twitch": f"https://www.twitch.tv/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Product Hunt": f"https://www.producthunt.com/@{username}",
        "Koo": f"https://www.kooapp.com/profile/{username}",
        "Blogger": f"https://{username}.blogspot.com",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Quora": f"https://www.quora.com/profile/{username}"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    print(f"\n🔍 Searching for username: '{username}' across platforms...\n")
    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"✅ {platform}: Found ➜ {url}")
            elif response.status_code == 404:
                print(f"❌ {platform}: Not Found")
            elif response.status_code == 400:
                print(f"⚠️  {platform}: Bad Request (HTTP 400)")
            elif response.status_code == 999:
                print(f"🚫 {platform}: Blocked by site (HTTP 999 - Anti-bot)")
            else:
                print(f"⚠️  {platform}: Unknown status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"🚫 {platform}: Error connecting ({e.__class__.__name__})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a username across multiple social media platforms.")
    parser.add_argument("username", help="The username to search for.")
    args = parser.parse_args()

    check_username(args.username)
