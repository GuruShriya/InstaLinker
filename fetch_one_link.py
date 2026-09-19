"""
Print one instgaram link based on the hashtag #gym
"""
from __future__ import annotations

import os
import sys
import instaloader 
from dotenv import load_dotenv

HASHTAG = "gym"

load_dotenv()

def build_loader() -> instaloader.Instaloader :
    """
    Create a read-only Instaloader client,optionally using a saved-session
    """
    loader = instaloader.Instaloader(
        quiet = True, #so instaloader doesn't push too many messages in the terminal
        download_videos = False,
        download_pictures = False,
        save_metadata = False,
        compress_json = False,
    )

    username = os.getenv("INSTAGRAM_USERNAME")
    session_file = os.getenv("INSTAGRAM_SESSION_FILE")
    if username and session_file :
        loader.load_session_from_file(username,session_file)
    return loader

def walk_dicts(value):
    """
    Instagram containes many different kind of boxes/dict, so to search inside each box is critical.
    Using recursion here and solving through dict and list approach.
    """
    if isinstance(value, dict):
        yield value #Understand it better yield TODO
        for child in value.values():
            yield from walk_dicts(child)

    elif isinstance(value, list):
        for item in value:
            yield from walk_dicts(item)

def fetch_video_link() -> str:
    loader = build_loader()

    hashtag = instaloader.Hashtag.from_name(loader.context, HASHTAG)

    # Do NOT use hashtag.get_posts(); it causes the more_available error.
    raw_data = getattr(hashtag, "_node", {})

    seen_shortcodes = set()

    for item in walk_dicts(raw_data):
        shortcode = item.get("shortcode") or item.get("code")

        is_video = (
            item.get("is_video") is True
            or item.get("media_type") == 2
            or "video_versions" in item
        )

        if is_video and shortcode and shortcode not in seen_shortcodes:
            seen_shortcodes.add(shortcode)
            return f"https://www.instagram.com/p/{shortcode}/"

    raise RuntimeError("No #gym video link was found in Instagram's returned data.")

# def fetch_video_link() -> str:
#     loader = build_loader()
#     hashtag = instaloader.Hashtag.from_name(loader.context, HASHTAG)

#     for post in hashtag.get_posts():
#         if post.is_video:
#             #post.shortcode is instagram unique ID for a link
#             return f"https://www.instagram.com/p/{post.shortcode}/"
        
#     raise RuntimeError("No videos for #gym")

def main() -> None:
    try:
        print(fetch_video_link())
    except Exception as error:
        print(f"Program failed.ERROR MESSAGE :{error}" , file=sys.stderr)
        raise SystemExit(1) #from error not used here TODO

if __name__ == "__main__": #TODO remove this once TUI is setup
    main()



