from models import db, Restaurant, MenuItem

restaurant1 = Restaurant(name="Sushi Hut", cuisine="sushi")
restaurant2 = Restaurant(name="Pizza Den", cuisine="pizza")
restaurant3 = Restaurant(name="Thai Garden", cuisine="Thai")
restaurant4 = Restaurant(name="Burger Palace", cuisine="American")

db.session.add(restaurant1)
db.session.add(restaurant2)
db.session.add(restaurant3)
db.session.add(restaurant4)
db.session.commit()

item1 = MenuItem(name="Avocado Roll", price=8.99, restaurant=restaurant1)
item2 = MenuItem(name="California Roll", price=10.99, restaurant=restaurant1)
item3 = MenuItem(name="Margherita Pizza", price=12.99, restaurant=restaurant2)
item4 = MenuItem(name="Pepperoni Pizza", restaurant=restaurant2)
item5 = MenuItem(name="Green Curry", price=10.00, restaurant=restaurant3)
item6 = MenuItem(name="Pad Thai", price=12.99, restaurant=restaurant3)
item7 = MenuItem(name="Salmon Nigiri", price=7.99, restaurant=restaurant1)
item8 = MenuItem(name="Supreme Pizza", price=14.99, restaurant=restaurant2)
item9 = MenuItem(name="Drunken Noodle", price=15.99, restaurant=restaurant3)
item10 = MenuItem(name="Classic Cheeseburger", price=12.00, restaurant=restaurant4)
item11 = MenuItem(name="Impossible Burger", price=11.00, restaurant=restaurant4)
item12 = MenuItem(name="Chicken Tenders", price=13.00, restaurant=restaurant4)

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.add(item4)
db.session.add(item5)
db.session.add(item6)
db.session.add(item7)
db.session.add(item8)
db.session.add(item9)
db.session.add(item10)
db.session.add(item11)
db.session.add(item12)
db.session.commit()