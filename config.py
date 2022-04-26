"""
/////////////AUTO TWITCH DROPS CONFIG FILE/////////////

- READ INSTRUCTIONS AND ADJUST VARIABLES CAREFULLY BEFORE RUNNING -

--VARIABLES--
streamer_text_file:
file name for text file that contains just newline separated streamer names (must be in same directory as code)

browser_refresh_time:
time in seconds to refresh all streams (starts streams that were started since last refresh)

chrome_profile_path:
**** MAKE SURE YOU ARE SIGNED IN TO TWITCH IN YOUR CHROME PROFILE ****
1. Type "chrome://version/" into your chrome browser address bar
2. Copy your "Profile Path" into chrome_profile_path
3. Delete "\Default\" from the end of chrome_profile_path if it is there
(Must close all open browser windows using this profile. Or create new profile, sign in twitch, and start over @ step 1)
"""

streamer_text_file = "streamers.txt"
browser_refresh_time = 30*60
chrome_profile_path = r'your_profile_path'
