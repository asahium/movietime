import kinopoisk_api
from aiogram.utils.markdown import text

from kinopoisk_api import KP
from config import KP_TOKEN

kinopoisk = KP(token=KP_TOKEN)

def info(num):
    t = kinopoisk.get_film(num)

    ans = text(
        t.ru_name, t.year,'\n',
        ", ".join(t.genres),'\n',
        ", ".join(t.countries),'\n',
        t.tagline, "\n",
        t.kp_url
    )
    return ans


def search(name):
    search = kinopoisk.search(name)
    i = 1
    answ = []
    for item in search:
        answ.append(item)
        i += 1
        if i == 6:
            break
    '''for item in answer:
        print(item.ru_name, item.year)
        print(", ".join(item.genres))
        print(", ".join(item.countries))
    i = 1'''
    i = 1
    answer = []
    for item in answ:
        ans = text(
            item.ru_name, item.year,'\n',
            ", ".join(item.genres),'\n',
            ", ".join(item.countries),'\n',
            item.kp_url,"\n","\n"
            )
        answer.append(ans)
        i += 1
        if i == 6:
            break

    return "\n\n".join(answer)

def search_genre(name):
    top = kinopoisk.top500()
    i = 1
    answer = []
    for item in top:
        if name in item.genres:
            ans = text(
                item.ru_name, item.year,'\n',
                ", ".join(item.genres),'\n',
                ", ".join(item.countries),'\n',
                item.kp_url,"\n"
            )
            answer.append(ans)
            i += 1
        if i == 6:
            break

    return "\n\n".join(answer)

def new_in():
    top = kinopoisk.topnew()
    i = 1
    answer = []
    for item in top:
        ans = text(
            item.ru_name, item.year,'\n',
            ", ".join(item.genres),'\n',
            ", ".join(item.countries),'\n',
            item.kp_url,"\n","\n"
        )
        answer.append(ans)
        i += 1
        if i == 6:
            break

    return "\n\n".join(answer)
