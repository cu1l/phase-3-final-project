from db.models import Base, restaurant_menu, MenuItem, Restaurant, UserOrder
from alembic.config import Config
from alembic import command
from rich.console import Console

console = Console()

YES = ['y', 'yes', 'Y']
NO = ['n', 'no', 'N']

def create_restaurants(restaurants):
    console.print(f'[bold royal_blue1] | [light_salmon1]ID[royal_blue1]| [light_salmon1]Name{" " * 12}[royal_blue1]| ')
    for restaurant in restaurants:
        idspace = 2 - len(str(restaurant.id))
        namespace = 16 - len(restaurant.name)
        console.print(f' [bold royal_blue1]|[light_salmon1] {restaurant.id}{" " * idspace}[royal_blue1]| [light_salmon1]{restaurant.name}{" " * namespace}[royal_blue1]|')

def create_menu_items(menu_items):
    console.print(f'[bold royal_blue1] | [light_salmon1]ID[royal_blue1]| [light_salmon1]Name{" " * 19}[royal_blue1]| [light_salmon1]Price  [royal_blue1]| ')
    for menu_item in menu_items:
        foodidspace = 2 - len(str(menu_item.id))
        foodnamespace = 23 - len(menu_item.food_name)
        pricespace = 6 - len(str(menu_item.food_price))
        console.print(f'[bold royal_blue1] |[light_salmon1] {menu_item.id}{" " * foodidspace}[royal_blue1]| [light_salmon1]{menu_item.food_name}{" " * foodnamespace}[royal_blue1]|[light_salmon1] ${menu_item.food_price:.2f}{" " * pricespace}[royal_blue1]|')