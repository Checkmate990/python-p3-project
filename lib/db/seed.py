from random import choice as rc
import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




from models import Store, Customer, Part
from models import Base

from sqlalchemy import create_engine
from models import Customer


engine = create_engine('sqlite:///p3_project.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()



part_names = ['CPU', 'Motherboard', 'RAM', 'GPU', 'Case', 'Monitor', 'Power Supply', 'HDD', 
               'Mouse', 'Keyboard', 'Cooling Fans', 'SDD']

brands = {
    'Case': {'Asus', 'Dell', 'MSI', 'ASRock', 'Razer'},
    'Motherboard': {'ASRock', 'Asus', 'MSI', 'Intel', 'Acer'},
    'CPU': {'AMD', 'Intel', 'Qualcomm', 'IBM', 'Nvidia'},
    'HDD': {'Toshiba', 'Samsung', 'Sony', 'LG'},
    'SDD': {'Toshiba', 'Samsung', 'Sony', 'LG'},
    'Cooling Fans': {'Corsair', 'Samsung', 'Sony', 'LG'},
    'Monitor': {'Alienwarew', 'Samsung', 'Dell', 'Sony', 'LG'},
    'GPU': {'Asus', 'Nvidia', 'AMD', 'Biostar', 'Intel'},
    'Keyboard': {'Amkette', 'HyperX', 'Razer', 'Lenovo', 'Dell'},
    'Mouse': {'Corsair', 'Alienware', 'Razer', 'HyperX', 'Sony'},
    'Power Supply': {'Corsair', 'Foxconn', 'Razer', 'Thermaltake'},
    'RAM': {'Lenovo', 'Asus', 'IBM', 'Toshiba', 'HyperX'},
}

for key in brands:
    brands[key] = list(set(brands[key]))


stores = ['Amazon', 'Best Buy', 'NewEgg', 'B&H', 'Micro Center', 'GameStop']

def delete_records():
    session.query(Store).delete()
    session.query(Customer).delete()
    session.query(Part).delete()
    session.commit()

def create_records():
    name = input('Customer name: ')
    budget = int(input('Customer budget: '))
    preference = input(f'Customer preference {part_names}: ')
    while preference not in part_names:
        preference = input(f'Invalid preference. Please choose from {part_names}: ')
    customer = Customer(
        name=name,
        budget=budget,
        preference=preference,
    )
    
    store_name = input(f"Store name {stores}: ")
    while store_name not in stores:
        store_name = input(f'Invalid store. Please choose from {stores}: ')
    quantity = int(input('Input quantity: '))
    customer_id = int(input("Enter customer ID: "))
    parts_id = int(input("Enter part ID: "))
    store = Store(
                    store_name=store_name,
                    quantity=quantity,
                    customer_id=customer_id,
                    parts_id=parts_id
                )
    part_name = input(f"Part name: {part_names}: ")
    while part_name not in part_names:
        part_name = input(f'Invalid part name. Please choose from {part_names}: ')
    cost = int(input('Part Cost: '))
    brand = input(f"Part brand: {brands}: ")
    while brand not in brands[part_name]:
        brand = input(f'Invalid brand for {part_name}. Please choose from {brands[part_name]}: ')
    part = Part(
        part_name=part_name,
        cost=cost,
        brand=brand,
    )
    session.add_all([customer, store, part])
    session.commit()
    return customer, store, part

if __name__ == '__main__':
    # delete_records()
    create_records()