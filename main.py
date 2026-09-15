# # import module1 as m
# # import module2 as m2
# from module2 import my_int
# # from module1 import (Hero, kirito)
# from module1 import *
#
# print(random.randint(1, 100))
#
# # print(kirito.name)
# # person = Hero("Ardager", 1, 1)
# # print(person.name)
# # print(my_int)
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('TEXT')
# print('back to normal now')




# from my_package.module1 import Hero, kirito
# from my_package.module2 import my_int
from my_package import Hero, kirito, my_int


import random

# import requests
#
# data = requests.get('https://unitrans.kg/api/v1/banners/')
#
# print(data)

from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def main_def():
    return {"Hello": "world"}
