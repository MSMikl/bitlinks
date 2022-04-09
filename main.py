import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse



load_dotenv()
AUTH_TOKEN = os.getenv("BITLY_TOKEN")
AUTH_HEADERS = {"Authorization": "Bearer {}".format(AUTH_TOKEN)}


def shorten_link(headers, url):
    payload = {"long_url": url, "domain": "bit.ly"}
    response = requests.post("https://api-ssl.bitly.com/v4/shorten",
                             headers=headers,
                             json=payload)
    if response.ok:
        return (response.json()["link"])
    raise Exception("Некорректная ссылка")


def count_clicks(headers, bitlink):
    bitlink = urlparse(bitlink).netloc + urlparse(bitlink).path
    params = {"unit": "day", "units": -1}
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary".format(
            bitlink),
        headers=headers,
        params=params)
    if response.ok:
        return response.json()["total_clicks"]
    else:
        raise Exception("Некорректная ссылка") 


def is_bitlink(headers, url):
    url = urlparse(url).netloc + urlparse(url).path
    response = requests.get(
        "https://api-ssl.bitly.com/v4/bitlinks/{}".format(url),
        headers=headers
        )
    if response.status_code == 200:
        return True
    elif response.status_code == 403:
        raise Exception("Это чужой битлинк")
    else:
        return False


def check_url(url):
    if urlparse(url).scheme == "":
        url = "https://{}".format(url)
    try:
        response = requests.get(url)
    except:
        raise Exception("Это не ссылка")
    if response.status_code == 404:
        raise Exception("Такой страницы не существует")
    return url


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help="Ссылка для сокращения или проверки")
    link = parser.parse_args().link
    checked_link = check_url(link)
    if is_bitlink(AUTH_HEADERS, checked_link):
        result = count_clicks(AUTH_HEADERS, checked_link)
        print("По вашей ссылке прошли {} раз(а)".format(result))
    else:
        result = shorten_link(AUTH_HEADERS, checked_link)
        print("Битлинк: {}".format(result))
