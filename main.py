from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import config


def get_streamers():
    with open(config.streamer_text_file, "r") as file:
        streamers = [streamer.rstrip() for streamer in file]
    return streamers


def main():
    streamers = get_streamers()
    streamer_urls = [f'https://www.twitch.tv/{streamer}' for streamer in streamers]
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={config.chrome_profile_path}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    for posts in range(len(streamer_urls)):
        driver.get(streamer_urls[posts])
        if posts != len(streamer_urls) - 1:
            driver.execute_script("window.open('');")
            tabs = driver.window_handles
            driver.switch_to.window(tabs[-1])
    window_tabs = driver.window_handles
    while True:
        sleep(config.browser_refresh_time)
        for tab in window_tabs:
            driver.switch_to.window(tab)
            driver.refresh()


if __name__ == '__main__':
    main()
