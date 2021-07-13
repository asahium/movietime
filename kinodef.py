import kinopoisk_api
from aiogram.utils.markdown import text

from kinopoisk_api import KP
from config import KP_TOKEN

kinopoisk = KP(token=KP_TOKEN)

def search(name):
    search = kinopoisk.search(name)
    i = 1
    for item in search:
        print(i, item.ru_name, item.year)
        print(", ".join(item.genres))
        print(", ".join(item.countries))
        print(item.kp_url)
        print()
        i += 1
        if i == 5:
            break

def info(num):
    t = kinopoisk.get_film(num)

    ans = text(
        t.ru_name, t.year,'\n',
        ", ".join(t.genres),'\n',
        ", ".join(t.countries),'\n',
        t.tagline, "\n",
    )
    return ans

def search(name):
    search = kinopoisk.search_by_genre(name)
    i = 1
    for item in search:
        print(i, item.ru_name, item.year)
        print(", ".join(item.genres))
        print(", ".join(item.countries))
        print(item.kp_url)
        print()
        i += 1
        if i == 5:
            break
