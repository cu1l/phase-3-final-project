from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rich.console import Console

from db.models import Restaurant, MenuItem, restaurant_menu
from helpers import (create_restaurants, YES, NO)

console = Console(width=80)

engine = create_engine('sqlite:///restaurants.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    console.print('''[dark_red]
  ___   _  _   _____  _            ___  ___
 / _ \ | || | |_   _|| |           |  \/  |                         
/ /_\ \| || |   | |  | |__    ___  | .  . |  ___  _ __   _   _  ___ 
|  _  || || |   | |  | '_ \  / _ \ | |\/| | / _ \| '_ \ | | | |/ __|
| | | || || |   | |  | | | ||  __/ | |  | ||  __/| | | || |_| |\__ \    
\_| |_/|_||_|   \_/  |_| |_| \___| \_|  |_/ \___||_| |_| \__,_||___/


                    d888P
      d8b d8888P:::P
    d:::888b::::::P
   d:::dP8888b:d8P
  d:::dP 88b  Yb   .d8888b.
 d::::P  88Yb  Yb .P::::::Y8b
 8:::8   88`Yb  YbP::::   :::b
 8:::P   88 `8   8!:::::::::::b
 8:dP    88  Yb d!!!::::::::::8
 8P    ..88   Yb8!!!::::::::::P
  .d8:::::Yb  d888VKb:!:!::!:8
 d::::::  ::dP:::::::::b!!!!8
8!!::::::::P::::::::::::b!8P
8:!!::::::d::::::: ::::::b
8:!:::::::8!:::::::  ::::8
8:!!!:::::8!:::::::::::::8
Yb:!!:::::8!!::::::::::::8
 8b:!!!:!!8!!!:!:::::!!:dP
  `8b:!!!:Yb!!!!:::::!d88
 VK   """  Y88!!!!!!!d8P                   
    ''', justify="default")

    console.print("[bold magenta] | Heres a list of restaurants to order from: ")

    cart = []

    while True:
      restaurants = session.query(Restaurant)
      create_restaurants(restaurants)
      restaurant = None
      while not restaurant:
        restaurant_id = console.input("[bold yellow] | Please enter which restaurant you'd like to order from: ")
        restaurant = session.query(Restaurant).filter(Restaurant.id == restaurant_id).one_or_none()