Project : Insta Linker

Architectural decision - Using the 'instaloader' , popular open-source Python wrapper around Instagram's web endpoints.

Decision to make - There were two options for the API call , one was the official 'MetaGraph API' which required a FB developer account, connected instagram professional account and an access token and second was the 'instaloader' , the python wrapper for instagram web endpoints.

To reduce hassle, I opted the instaloader wrapper for this.

Instagram may limit requests. 


**Creating a session file for instaloader to use :**

 instaloader --login=... is a one-time setup command run in your terminal, not inside our Python program.

Our Python code uses the session file after that command creates it:

loader.load_session_from_file(username, session_file)

Do this once:

pip install -r requirements.txt
instaloader --login=YOUR_INSTAGRAM_USERNAME

For example, if your username is shriya_fit:

instaloader --login=shriya_fit

It will ask for your Instagram password in the terminal, and possibly a 2FA code. Do not put the password in .env or send it anywhere.

After successful login, Instaloader creates a session file, usually on your Mac here:

/Users/your-mac-user/.config/instaloader/session-shriya_fit

Check it with:

ls ~/.config/instaloader

Then update .env:

INSTAGRAM_USERNAME=shriya_fit
INSTAGRAM_SESSION_FILE=/Users/your-mac-user/.config/instaloader/session-shriya_fit

## Using hashtag._node instead of get_posts()##
- get_posts() was throwing error "more available" 
- hastatg._node returns a dict or list of raw data 


**Using textual for TUI**

