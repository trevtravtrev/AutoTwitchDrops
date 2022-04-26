"""
main.py file. run main.py.
"""
from time import sleep
from random import choices
import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_streamers() -> list:
    """
    Parse streamer names from streamers.txt into a list. streamers.txt must be newline separated streamer names. Just
    twitch names not url.
    :return: list of streamers
    """
    with open(settings.STREAMER_TEXT_FILE, "r", encoding="utf-8") as file:
        streamers = [streamer.rstrip() for streamer in file]
    return choices(streamers, k=settings.STREAMER_COUNT)


def main():
    """
    Main method. Opens browser tab for each streamer. Auto refreshes all tabs every settings.BROWSER_REFRESH_TIME
    seconds.
    :return: None
    """
    streamers: list = get_streamers()
    streamer_urls: list = [
        f"https://www.twitch.tv/{streamer}" for streamer in streamers
    ]
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={settings.CHROME_PROFILE_PATH}")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    for i, streamer_url in enumerate(streamer_urls):
        driver.get(streamer_url)
        if i != len(streamer_urls) - 1:
            driver.execute_script("window.open('');")
            tabs = driver.window_handles
            driver.switch_to.window(tabs[-1])
    window_tabs = driver.window_handles
    while True:
        sleep(settings.BROWSER_REFRESH_TIME)
        for tab in window_tabs:
            driver.switch_to.window(tab)
            driver.refresh()


if __name__ == "__main__":
    main()
