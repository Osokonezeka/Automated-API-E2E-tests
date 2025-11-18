import re

from playwright.sync_api import expect

from utils.connection import connect_to_home

"""
Wejście na stronę główną.

Kliknięcie ikonę lupki

Wyszukanie "frazy"

Sprawdzenie, czy "fraza" pojawia się w wyszukiwaniach.

Wejście na stronę szczegółów tego filmu.

Sprawdzenie, czy nagłówek H1 na stronie filmu zawiera "frazę".

Sprawdzenie, czy na stronie widoczny jest odtwarzacz wideo.

Uruchomienie odtwarzania filmu (kliknięcie "play").

Weryfikacja asynchroniczności: Sprawdzenie, czy w przedziale od 1 do 60 sekund odtwarzanie zostanie przerwane i na ekranie pojawi się popup.

Sprawdzenie, na jaki adres URL (lub domenę) próbuje przekierować użytkownika klikając ten popup.
"""


def test_e2e(page):
    search_icon = page.locator(".mr-0.hidden.lg:block.lg:mr-4")  # no ID?
    search_bar = page.locator("#search")

    movie_not_found = page.locator(".w-full.flex.justify-center.mt-24.xl:mt-36.text-base.xl:text-xl")  # no ID?
    movie_link = page.locator(".search__ResultsContainer-sc-87cf44fc-7.iGbxAq.animation-fade-in > article:nth-child(1)")  # no ID?
    movie_header = page.locator(".relative > h1")  # no ID?
    movie_player = page.locator("")
    movie_play_button = page.locator("")

    phrase = ["the pickup", "abcxyz123"]

    connect_to_home(page)
    search_icon.click()
    # search_bar.click()
    for x in range(2):
        phrase = phrase[x]
        if phrase[0]:
            search_bar.fill(phrase)
            # expect(movie_link).to_have_attribute("href", "/filmy/the-pickup-caly-film")
            movie_link.click()
            expect(movie_header).to_have_text(re.compile(r"(%s).*" % phrase[0], re.IGNORECASE))
            expect(movie_player).to_be_visible()
            movie_play_button.click()
        else:
            search_bar.fill(phrase)
            expect(movie_not_found).to_have_text(re.compile(r"Nie znaleziono filmów i seriali dla podanej frazy"))
