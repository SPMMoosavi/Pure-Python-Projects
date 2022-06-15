import requests
from unicodedata import lookup


def extract_ip(proxy):
    return proxy.split('@')[1].split(':')[0]


def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "country": response.get("country"),
        "country_name": response.get("country_name")
    }
    return location_data


if __name__ == '__main__':
    with open('shadowsocks.txt', 'r') as source:
        for p in source.readlines():
            before_sharp = p.split('#')[0]
            info = get_location(extract_ip(p))
            flag = ''
            for a in info.get('country'):
                flag += lookup(f'REGIONAL INDICATOR SYMBOL LETTER {a}')
            print(f'{before_sharp}#{flag}{info.get("country_name")}')
            with open('shadowsocks_country.txt', 'a', encoding="utf-8") as destination:
                destination.writelines(f'{before_sharp}#{flag}{info.get("country_name")}\n')
