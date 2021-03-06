import kinopoisk
from aiogram.utils.markdown import text
from kinopoisk import KINOPOISK
from config import KP_TOKEN

kino = KINOPOISK(token=KP_TOKEN)


def info(num):
    item = kino.get_film(num)

    ans = text(
        item.ru_name, '\n',
        '📆 ', item.year, '\n',
        '🎭 ', ", ".join(item.genres), '\n',
        '🗺 ', ", ".join(item.countries), '\n',
        item.tagline, "\n", '\n',
        '🔗 ', item.kp_url, "\n",
        sep='')
    return ans


def search(name):
    search = kino.search(name)
    i = 1
    answ = []
    for item in search:
        answ.append(item)
        i += 1
        if i == 6:
            break
    i = 1
    answer = []
    for item in answ:
        ans = text(
            i, ') ', item.ru_name, '\n',
            '📆 ', item.year, '\n',
            '🎭 ', ", ".join(item.genres), '\n',
            '🗺 ', ", ".join(item.countries), '\n', '\n',
            '🔗 ', item.kp_url, "\n",
            sep='')
        answer.append(ans)
        i += 1
        if i == 6:
            break

    return "\n\n".join(answer)


def search_genre(name):
    top = kino.top500()
    i = 1
    answer = []
    for item in top:
        if name in item.genres:
            ans = text(
                i, ') ', item.ru_name, '\n',
                '📆 ', item.year, '\n',
                '🎭 ', ", ".join(item.genres), '\n',
                '🗺 ', ", ".join(item.countries), '\n', '\n',
                '🔗 ', item.kp_url, "\n",
                sep='')
            answer.append(ans)
            i += 1
        if i == 6:
            break

    return "\n\n".join(answer)


def new_in():
    top = kino.topnew()
    i = 1
    answer = []
    for item in top:
        ans = text(
            i, ') ', item.ru_name, '\n',
            '📆 ', item.year, '\n',
            '🎭 ', ", ".join(item.genres), '\n',
            '🗺 ', ", ".join(item.countries), '\n', '\n',
            '🔗 ', item.kp_url, "\n",
            sep='')
        answer.append(ans)
        i += 1
        if i == 6:
            break

    return "\n\n".join(answer)
