from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rich.console import Console

from db.models import Restaurant, MenuItem, restaurant_menu
from helpers import (create_restaurants, create_menu_items, YES, NO)

console = Console(width=80)

engine = create_engine('sqlite:///db/restaurants.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    console.print(f'''[cyan]
  ___   _  _   _____  _            ___  ___                                                         
 / _ \ | || | |_   _|| |           |  \/  |
/ /_\ \| || |   | |  | |__    ___  | .  . |  ___  _ __   _   _  ___ 
|  _  || || |   | |  | '_ \  / _ \ | |\/| | / _ \| '_ \ | | | |/ __|
| | | || || |   | |  | | | ||  __/ | |  | ||  __/| | | || |_| |\__ \    
\_| |_/|_||_|   \_/  |_| |_| \___| \_|  |_/ \___||_| |_| \__,_||___/

[dark_red]
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
      """  Y88!!!!!!!d8P                   
    ''', justify="full")

    console.print("[bold turquoise4] Heres a list of restaurants to order from: ")

    cart = []
    rest_input = "Please enter the restaurant's ID: "

    while True:
      restaurants = session.query(Restaurant)
      create_restaurants(restaurants)
      restaurant = None
      while not restaurant:
        restaurant_id = console.input(f"[bold royal_blue1] > [cyan]{rest_input}")
        restaurant = session.query(Restaurant).filter(Restaurant.id == restaurant_id).one_or_none()

      console.print(f'[bold royal_blue1] [turquoise4]Here is the menu at {restaurant.name}: ')
      foods = session.query(MenuItem).filter_by(restaurant=restaurant_id).all()
      create_menu_items(foods)

      food = None
      while not food:
        menu_id = console.input("[bold royal_blue1] > [cyan]Please enter the food's ID: ")
        if menu_id == 0:
          break
        food = session.query(MenuItem).filter(MenuItem.id == menu_id).one_or_none()
      
      console.print(f'[bold royal_blue1] [turquoise4]You chose {food.food_name}!')
      cart.append(food)

      more = console.input(f'[bold royal_blue1] > [cyan]Would you like to order more food? (Y/N): ').lower()

      if more in YES:
        rest_input = "Please select another restaurant's ID: "

      if more in NO:
        console.input(f'[bold royal_blue1] > [cyan]Please input the address for your order: ')
        subtotal = sum(food.food_price for food in cart)
        tax = subtotal * 0.065
        total = subtotal + tax

        console.print(f'[bold turquoise4]Your total today is [red]{total:.2f}!')
        answer = console.input(f'[bold royal_blue1] > [cyan]Would you like to place a new order? (Y/N): ')
        if answer in YES:
          cart.pop()
        if answer in NO:
          console.print(f'[bold turquoise4]Thank you for using all the menus!')
          break
