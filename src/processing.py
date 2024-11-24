words = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(word, state="EXECUTED"):
    """Функция вывод ключ значение"""
    new_word = []
    for dic_word in word:
        if dic_word["state"] == state:
            new_word.append(dic_word)
    return new_word


print(filter_by_state(words))


by_date = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def sort_by_date(date, reverse: bool = True):
    """Функция сортирующая по убыванию"""
    return sorted(date, key=lambda k: '.'.join(reversed(k['date'].split('.'))), reverse=reverse)


print(sort_by_date(by_date))
