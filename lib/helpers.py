from db.models import Base, restaurant_menu, MenuItem, Restaurant, UserOrder
from alembic.config import Config
from alembic import command
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

YES = ['y', 'yes', 'Y']
NO = ['n', 'no', 'N']

def create_restaurants(restaurants):
    table = Table(title = "Restaurants", box=box.ASCII_DOUBLE_HEAD)
    table.add_column("ID", justify="right", style="royal_blue1", no_wrap=True)
    table.add_column("Name", style="royal_blue1")
    for restaurant in restaurants:
        table.add_row(f'{restaurant.id}', f'{restaurant.name}')
    console.print(table)

def create_menu_items(menu_items):
    table = Table(title = "Menu Items", box=box.ASCII_DOUBLE_HEAD)
    table.add_column("ID", justify="center", style="royal_blue1", no_wrap=True)
    table.add_column("Name", style="royal_blue1",)
    table.add_column("Price", justify="left", style="royal_blue1")
    for menu_item in menu_items:
        table.add_row(f'{menu_item.id}', f'{menu_item.food_name}', f'${menu_item.food_price}')
    console.print(table)