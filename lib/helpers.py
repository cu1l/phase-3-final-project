from db.models import Base, restraunt_menus, MenuItem, Restaurant, UserOrder
from alembic.config import Config
from alembic import command

YES = ['y', 'ye', 'yes']
NO = ['n', 'no']

def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_tables(engine):
    Base.metadata.drop_all(engine)

def migrate_database(config):
    command.upgrade(config, "head")

def get_restaurants(session):
    restaurants = session.query(Restaurant).all()
    for r in restaurants:
        print(f"{r.id}. {r.name}")

def get_menu_items(session, restaurant_id):
    menu_items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    for mi in menu_items:
        print(f"{mi.id}. {mi.name}: ${mi.price}")

def add_menu_item_to_order(session, user_id, menu_item_id):
    order = UserOrder(user_id=user_id, menu_item_id=menu_item_id)
    session.add(order)
    session.commit()

def delete_menu_item_from_order(session, user_id, menu_item_id):
    order = session.query(UserOrder).filter_by(user_id=user_id, menu_item_id=menu_item_id).first()
    session.delete(order)
    session.commit()

def get_user_order(session, user_id):
    order = session.query(UserOrder).filter_by(user_id=user_id).all()
    total_price = 0
    for o in order:
        mi = session.query(MenuItem).filter_by(id=o.menu_item_id).first()
        print(f"{mi.name}: ${mi.price}")
        total_price += mi.price
    print(f"Total price: ${total_price}")

def pay_tab(session, user_id):
    order = session.query(UserOrder).filter_by(user_id=user_id).all()
    total_price = 0
    for o in order:
        mi = session.query(MenuItem).filter_by(id=o.menu_item_id).first()
        total_price += mi.price
    print(f"Your tab is: ${total_price}")
    session.query(UserOrder).filter_by(user_id=user_id).delete()
    session.commit()