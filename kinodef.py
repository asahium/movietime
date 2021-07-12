import kinopoisk_api
from kinopoisk_api import KP
from config import KP_TOKEN

kinopoisk = kinopoisk_api.KP(token=KP_TOKEN)

def search(name):
    search = kinopoisk.search(name)
    i = 1
    for item in search:
        print(i, item.ru_name, item.year)
        print(", ".join(item.genres))
        print(", ".join(item.countries))
        i += 1
        if i == 5:
            break

def info(t):
    kinopoisk = KP(token=KP_TOKEN)

    t = kinopoisk.get_film(1236063)

    print(t.ru_name, t.year)
    print(", ".join(t.genres))
    print(", ".join(t.countries))
    print(t.tagline)
