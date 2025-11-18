class UrlUtils:
    def __init__(self, page):
        self.page = page
        page.set_viewport_size({"width": 1920, "height": 1080})
        self.home = f"https://vod.film/"

    def url_home(self):
        self.page.goto(self.home)


def connect_to_home(page):
    urls = UrlUtils(page)
    urls.url_home()
