from models import Restaurant, MenuItem

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rich.console import Console

console = Console()

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

console.print(f"[bold red] | Purging databases...")

session.query(Restaurant).delete()
session.query(MenuItem).delete()
session.commit()

console.print(f"[bold green] | Purged Databases.")

console.print(f"[bold red] | Building databases...")
console.print(f"[bold red] | Creating Restaurants...")

restaurant1 = Restaurant(name="Sushi Hut", cuisine="Sushi")
restaurant2 = Restaurant(name="Pizza Den", cuisine="Pizza")
restaurant3 = Restaurant(name="Thai Garden", cuisine="Thai")
restaurant4 = Restaurant(name="Burger Palace", cuisine="American")
session.add_all([restaurant1, restaurant2, restaurant3, restaurant4])
session.commit()

console.print(f"[bold green] | Finished building restraunts.")
console.print(f"[bold red] | Creating menu items...")

session.add_all([MenuItem(food_name="Avocado Roll", food_price=8.99, restaurant=f'{restaurant1.id}'),
MenuItem(food_name="California Roll", food_price=10.99, restaurant=f'{restaurant1.id}'),
MenuItem(food_name="Margherita Pizza", food_price=12.99, restaurant=f'{restaurant2.id}'),
MenuItem(food_name="Pepperoni Pizza", food_price=13.25, restaurant=f'{restaurant2.id}'),
MenuItem(food_name="Green Curry", food_price=10.00, restaurant=f'{restaurant3.id}'),
MenuItem(food_name="Pad Thai", food_price=12.99, restaurant=f'{restaurant3.id}'),
MenuItem(food_name="Salmon Nigiri", food_price=7.99, restaurant=f'{restaurant1.id}'),
MenuItem(food_name="Supreme Pizza", food_price=14.99, restaurant=f'{restaurant2.id}'),
MenuItem(food_name="Drunken Noodle", food_price=15.99, restaurant=f'{restaurant3.id}'),
MenuItem(food_name="Classic Cheeseburger", food_price=12.00, restaurant=f'{restaurant4.id}'),
MenuItem(food_name="Impossible Burger", food_price=11.00, restaurant=f'{restaurant4.id}'),
MenuItem(food_name="Chicken Tenders", food_price=13.00, restaurant=f'{restaurant4.id}')])
session.commit()

console.print(f"[bold green] | Finished creating menu items...")
console.print(f"[bold green] | Finished building databases.")