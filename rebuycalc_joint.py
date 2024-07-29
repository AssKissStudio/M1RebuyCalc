import requests
from colorama import init, Fore
init(autoreset=True)

print(Fore.LIGHTWHITE_EX + 'RebuyCalc. Made by AssKiss Studio https://github.com/AssKissStudio/M1RebuyCalc')
try:
    while True:
        proto = input(Fore.MAGENTA + 'Введите id прототипа:')
        price = requests.get(f'https://monopoly-one.com/api/market.getBestPrice?thing_prototype_id={proto}').json()['data']['price']
        yourprice = float(price) / 85 * 100 + 0.01
        print(Fore.GREEN + f'Цена на маркете {price}₽. Чтобы окупиться, вам следует продавать по {round(yourprice,2)}₽')
except:
    print('Ошибка')
    input()
    exit()