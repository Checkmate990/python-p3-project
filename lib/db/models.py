from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///p3_project.db")

Base = declarative_base()


class Store(Base):
    """A store that sells parts to customers."""

    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    store_name = Column(String)
    quantity = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    parts_id = Column(Integer, ForeignKey("parts.id"))

    customer = relationship("Customer", back_populates="stores")
    part = relationship("Part", back_populates="stores")

    def __repr__(self):
        return f"Store {self.id}: {self.store_name}, {self.quantity}"


class Customer(Base):
    """A customer who buys parts from stores."""

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    budget = Column(Integer)
    preference = Column(String)

    stores = relationship("Store", back_populates="customer")

    def __repr__(self):
        return f"Customer {self.id}: {self.name}, Budget: {self.budget}, Preference: {self.preference}"


class Part(Base):
    """A part that can be sold by a store to a customer."""

    __tablename__ = "parts"

    id = Column(Integer, primary_key=True)
    part_name = Column(String)
    cost = Column(Integer)
    brand = Column(String)

    stores = relationship("Store", back_populates="part")

    def __repr__(self):
        return f"Part {self.id}: {self.part_name}, Cost: {self.cost}, Brand: {self.brand}"


