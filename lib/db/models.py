from sqlalchemy import create_engine, func
from sqlalchemy import PrimaryKeyConstraint, ForeignKey, Table, Column, Integer, Float, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy



engine = create_engine('sqlite:///restaurants.db')

Base = declarative_base()

restaurant_menu = Table(
    'restaurant_menus',
    Base.metadata,
    Column('menu_id', ForeignKey('menu_items.id'), primary_key=True),
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True)
)

class MenuItem(Base):
    __tablename__ = 'menu_items'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    food_name = Column(String())
    food_price = Column(Integer())
    restaurant = Column(String())

    restaurants = relationship('Restaurant', secondary=restaurant_menu, back_populates='menu_items')

class Restaurant(Base):
    __tablename__ = 'restaurants'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    name = Column(String())
    cuisine = Column(String())

    menu_items = relationship('MenuItem', secondary=restaurant_menu, back_populates='restaurants')

    def __repr__(self):
        return f'Restaurant(id={self.id}), ' + \
            f'name={self.name}' + \
            f'cuisine={self.cuisine}'

class UserOrder(Base):
    __tablename__ = 'user_orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    menu_item_id = Column(Integer, nullable=False)