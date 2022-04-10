# Скрипт сокращения ссылок

Данный скрипт содержит в себе набор функций для сокращения ссылок при помощи сервиса ***Bit.ly*** через его API.


## Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
`pip install -r requirements.txt`

## Получение токена

Для работы необходима регистрация на сервисе ***Bit.ly*** и токен авторизации API (инструкция по его получению [здесь](https://bitly.com/a/oauth_apps))

Полученный токен следует поместить в файл `.env` в папку с програмой в формате `BITLY_TOKEN = a45a8a4859db0ca7902f4915434fa9ef0943576h`

## Использование

`main.py link`

В качестве параметра *link* передается url в формате `https://example.com` или `example.com`.

Скрипт проверяет ссылку на корректность, в случае ошибки выводит в консоль соответствующее ей сообщение.

Если *link* не является сокращенной ссылкой сервиса  ***Bit.ly***, скрипт выводит в консоль сокращенную ссылку.

Если *link* - сокращенная ссылка сервиса bit.ly, принадлежащая пользователю, то скрипт выведет в консоль общее количество переходов по данной ссылке. Если сокращенная ссылка не принадлежит пользователю, то скрипт выведет сообщение о соответствующей ошибке.

# Встроенные функции

Скрипт содержит отдельные встроенные функции для сокращения ссылок, проверки их на валидность, получения информации о количестве переходов по ссылке.

## shorten_link(headers, url)

Функция возвращает сокращенную ссылку "битлинк" либо сообщение об ошибке в случае, если ссылка некорректна.

### Параметры

**headers**  - словарь (dict) Python, содержащий токен авторизации в формате `{"Authorization": "Bearer {}".format(AUTH_TOKEN)}`

**url** - url в формате `http://example.com`

Пример использования

	>>>from main.py import shorten_link
	>>>headers = {"Authorization": "Bearer {}".format("a45a8a4859db0ca7902f4915434fa9ef0943576h")}
	>>>url = "https://dvmn.org"
	>>>print(shorten_link(headers, url))
	https://bit.ly/38t3s3b

## count_clicks(headers, bitlink)

Функция возвращает количество переходов по сокращенной ссылке либо сообщение об ошибке.

### Параметры

**headers** - словарь (dict) Python, содержащий токен авторизации в формате `{"Authorization": "Bearer {}".format(AUTH_TOKEN)}`

**bitlink** - "битлинк" в формате `https://bit.ly/38t3s3b`

Пример использования

	>>>from main.py import count_clicks
	>>>headers = {"Authorization": "Bearer {}".format("a45a8a4859db0ca7902f4915434fa9ef0943576h")}
	>>>url = "https://bit.ly/38t3s3b"
	>>>print("По вашей ссылке прошли {} раза".format(count_clicks(headers, url))
	По вашей ссылке прошли 4 раза

## is_bitlink(headers, url)

Функция возвращает True, если ссылка является битлинком, False - если ссылка не является битлинком, вызывает ошибку, если битлинк не принадлежит данному пользователю.

### Параметры

**headers** - словарь (dict) Python, содержащий токен авторизации в формате `{"Authorization": "Bearer {}".format(AUTH_TOKEN)}`

**url** - "битлинк" в формате `https://bit.ly/38t3s3b`

Пример использования

	>>>from main.py import is_bitlink
	>>>headers = {"Authorization": "Bearer {}".format("a45a8a4859db0ca7902f4915434fa9ef0943576h")}
	>>>url = "https://bit.ly/38t3s3b"
	>>>print(is_bitlink(headers, url))
	True
