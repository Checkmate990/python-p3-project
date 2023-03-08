from random import choice as rc
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Store, Customer, Part

engine = create_engine("sqlite:///p3_project.db")
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

part_names = [
    "CPU", "Motherboard", "RAM", "GPU", "Case", "Monitor", "Power Supply", "HDD",
    "Mouse", "Keyboard", "Cooling Fans", "SDD"
]

brands = {
    "Case": {"Asus", "Dell", "MSI", "ASRock", "Razer"},
    "Motherboard": {"ASRock", "Asus", "MSI", "Intel", "Acer"},
    "CPU": {"AMD", "Intel", "Qualcomm", "IBM", "Nvidia"},
    "HDD": {"Toshiba", "Samsung", "Sony", "LG"},
    "SDD": {"Toshiba", "Samsung", "Sony", "LG"},
    "Cooling Fans": {"Corsair", "Samsung", "Sony", "LG"},
    "Monitor": {"Alienware", "Samsung", "Dell", "Sony", "LG"},
    "GPU": {"Asus", "Nvidia", "AMD", "Biostar", "Intel"},
    "Keyboard": {"Amkette", "HyperX", "Razer", "Lenovo", "Dell"},
    "Mouse": {"Corsair", "Alienware", "Razer", "HyperX", "Sony"},
    "Power Supply": {"Corsair", "Foxconn", "Razer", "Thermaltake", "Razer"},
    "RAM": {"Lenovo", "Asus", "IBM", "Toshiba", "HyperX"},
}

store_names = ["Amazon", "Best Buy", "NewEgg", "B&H", "Micro Center", "GameStop"]


def delete_records():
    session.query(Store).delete()
    session.query(Customer).delete()
    session.query(Part).delete()
    session.commit()


def create_records():
    """Create customers, stores, and parts."""
    customers = [
        Customer(
            name=f"{fake.first_name()} {fake.last_name()}",
            budget=f"${rc(range(100, 2501))}",
            preference=rc(part_names),
        )
        for _ in range(50)
    ]
    session.add_all(customers)

    stores = [
        Store(
            store_name=rc(store_names),
            quantity=rc(range(11)),
            customer=rc(customers),
            part=rc(parts),
        )
        for _ in range(50)
    ]
    session.add_all(stores)

    parts = [
      Part(
    part_name=rc(part_names),
    cost=f"${rc(range(100, 1001)) if part_name in part_names[:7] else rc(range(20, 151))}",
    brand=rc(list(brands.keys())),
)
for _ in range(50)
]
session.add_all(parts)

session.commit()
return customers

if name == "main":
delete_records()
create_records()
       
