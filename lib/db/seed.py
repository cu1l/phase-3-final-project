from models import Restaurant, MenuItem

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rich.console import Console

console = Console()

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

console.print(f"[bold blue] | Purging databases...")

session.query(Restaurant).delete()
session.query(MenuItem).delete()
session.commit()

console.print(f"[bold green] | Purged Databases.")

console.print(f"[bold blue] | Building databases...")
console.print(f"[bold blue] | Creating Restaurants...")

restaurant1 = Restaurant(name="Sushi Hut", cuisine="sushi")
restaurant2 = Restaurant(name="Pizza Den", cuisine="pizza")
restaurant3 = Restaurant(name="Thai Garden", cuisine="Thai")
restaurant4 = Restaurant(name="Burger Palace", cuisine="American")

console.print(f"[bold green] | Finished building restraunts.")
console.print(f"[bold blue] | Creating Sessions...")

session.add(restaurant1)
session.add(restaurant2)
session.add(restaurant3)
session.add(restaurant4)
session.commit()

console.print(f"[bold green] | Created Sessions")
console.print(f"[bold blue] | Creating menu items...")

item1 = MenuItem(food_name="Avocado Roll", food_price=8.99, restaurant=f'{restaurant1.name}')
item2 = MenuItem(food_name="California Roll", food_price=10.99, restaurant=f'{restaurant1.name}')
item3 = MenuItem(food_name="Margherita Pizza", food_price=12.99, restaurant=f'{restaurant2.name}')
item4 = MenuItem(food_name="Pepperoni Pizza", restaurant=f'{restaurant2.name}')
item5 = MenuItem(food_name="Green Curry", food_price=10.00, restaurant=f'{restaurant3.name}')
item6 = MenuItem(food_name="Pad Thai", food_price=12.99, restaurant=f'{restaurant3.name}')
item7 = MenuItem(food_name="Salmon Nigiri", food_price=7.99, restaurant=f'{restaurant1.name}')
item8 = MenuItem(food_name="Supreme Pizza", food_price=14.99, restaurant=f'{restaurant2.name}')
item9 = MenuItem(food_name="Drunken Noodle", food_price=15.99, restaurant=f'{restaurant3.name}')
item10 = MenuItem(food_name="Classic Cheeseburger", food_price=12.00, restaurant=f'{restaurant4.name}')
item11 = MenuItem(food_name="Impossible Burger", food_price=11.00, restaurant=f'{restaurant4.name}')
item12 = MenuItem(food_name="Chicken Tenders", food_price=13.00, restaurant=f'{restaurant4.name}')

console.print(f"[bold green] | Finished creating menu items...")
console.print(f"[bold blue] | Creating Sessions...")

session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.add(item5)
session.add(item6)
session.add(item7)
session.add(item8)
session.add(item9)
session.add(item10)
session.add(item11)
session.add(item12)
session.commit()
console.print(f"[bold green] | Created Sessions")
console.print(f"[bold green] | Finished building databases.")