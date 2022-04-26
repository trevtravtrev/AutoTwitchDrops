"""
/////////////AUTO TWITCH DROPS SETTINGS FILE/////////////

- READ INSTRUCTIONS AND ADJUST VARIABLES CAREFULLY BEFORE RUNNING -

--VARIABLES--
STREAMER_TEXT_FILE:
file name for text file that contains just newline separated streamer names (must be in same directory as code)

BROWSER_REFRESH_TIME:
time in seconds to refresh all streams (starts streams that were started since last refresh)

CHROME_PROFILE_PATH:
**** MAKE SURE YOU ARE SIGNED IN TO TWITCH IN YOUR CHROME PROFILE ****
1. Type "chrome://version/" into your chrome browser address bar
2. Copy your "Profile Path" into chrome_profile_path
3. Delete "\Default\" from the end of chrome_profile_path if it is there
(Must close all open browser windows using this profile. Or create new profile, sign in twitch, and start over @ step 1)
"""

STREAMER_TEXT_FILE: str = "streamers.txt"
BROWSER_REFRESH_TIME: int = 30 * 60
CHROME_PROFILE_PATH: str = r"your_profile_path"
