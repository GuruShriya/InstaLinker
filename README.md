# Insta Linker

A terminal app for finding Instagram `#gym` videos. The final goal is to show the five most-viewed videos from the last hour or last 24 hours.

## Current progress

- Fetch-one-link proof of concept using Instaloader and a saved Instagram session.
- Textual TUI welcome screen: **Welcome to InstaLinker** / **Hello World**.
- Press `Q` to quit the current TUI.

## Run the welcome screen

```bash
pip install -r requirements.txt
python3 insta_linker_tui.py
```

## Instagram setup

Create a `.env` file locally:

```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_SESSION_FILE=/full/path/to/session-your_username
```

Do not store a password in code or `.env`.

## Current workarounds

- `hashtag.get_posts()` can fail with `KeyError: 'more_available'`. The working proof of concept reads the initial `hashtag._node` data instead of requesting more pages. `_node` is internal Instaloader data, so this is a temporary workaround.
- If Instagram checkpoint login loops, log in normally in Firefox and use Instaloader's [Firefox session-import helper](https://instaloader.github.io/troubleshooting.html) to create a local session file.

## Project files

- [HLD.md](HLD.md) — current high-level design.
- [fetch_one_gym_link.py](fetch_one_gym_link.py) — first link-fetch test.
- [insta_linker_tui.py](insta_linker_tui.py) — TUI entry point.
- [insta_linker.tcss](insta_linker.tcss) — TUI styles.
- [requirements.txt](requirements.txt) — Python dependencies.

## Next

Add the two time-window choices to the welcome screen.
