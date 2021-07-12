import kinopoisk_api
from kinopoisk_api import KP


kinopoisk = kinopoisk_api.KP(token='Push your token here')

def search(name):
    search = kinopoisk.search(name)
    i = 1
    for item in search:
        print(i, item.ru_name, item.year)
        print(", ".join(item.genres))
        print(", ".join(item.countries))
        i += 1

def info(t):
    kinopoisk = KP(token='Push your token here')

    t = kinopoisk.get_film(1236063)

    print(t.ru_name, t.year)
    print(", ".join(t.genres))
    print(", ".join(t.countries))
    print(t.tagline)
