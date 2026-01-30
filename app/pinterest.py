import requests
from bs4 import BeautifulSoup


def download_pinterest(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        raise Exception("Pinterest page not reachable")

    soup = BeautifulSoup(r.text, "html.parser")

    # वीडियो ढूँढना
    video = soup.find("video")
    if video and video.get("src"):
        return {
            "type": "video",
            "download_url": video["src"]
        }

    # इमेज ढूँढना
    image = soup.find("img")
    if image and image.get("src"):
        return {
            "type": "image",
            "download_url": image["src"]
        }

    raise Exception("No downloadable media found")
