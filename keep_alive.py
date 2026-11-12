from playwright.sync_api import sync_playwright

URL = "https://automated-resume-screening-tool-ebysjwrl2ebzs7vhtcjnoz.streamlit.app/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL, timeout=60000)
    try:
        page.get_by_role("button", name="Yes, get this app back up!").click(timeout=10000)
        print("App was asleep, woke it up")
    except Exception:
        print("App already awake")
    page.wait_for_timeout(20000)
    browser.close()
