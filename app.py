#pip install flask


from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Store, Customer, Part

app = Flask(__name__)

engine = create_engine("sqlite:///p3_project.db")
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def list_customers():
    customers = session.query(Customer).all()
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        budget = int(request.form['budget'])
        preference = request.form['preference']
        customer = Customer(name=name, budget=budget, preference=preference)
        session.add(customer)
        session.commit()
        return render_template('add_customer.html', success=True)
    else:
        return render_template('add_customer.html', success=False)

@app.route('/stores')
def list_stores():
    stores = session.query(Store).all()
    return render_template('stores.html', stores=stores)

@app.route('/add_store', methods=['GET', 'POST'])
def add_store():
    if request.method == 'POST':
        store_name = request.form['store_name']
        quantity = int(request.form['quantity'])
        customer_id = int(request.form['customer_id'])
        parts_id = int(request.form['parts_id'])
        store = Store(store_name=store_name, quantity=quantity, customer_id=customer_id, parts_id=parts_id)
        session.add(store)
        session.commit()
        return render_template('add_store.html', success=True)
    else:
        customers = session.query(Customer).all()
        parts = session.query(Part).all()
        return render_template('add_store.html', success=False, customers=customers, parts=parts)

@app.route('/parts')
def list_parts():
    parts = session.query(Part).all()
    return render_template('parts.html', parts=parts)

@app.route('/add_part', methods=['GET', 'POST'])
def add_part():
    if request.method == 'POST':
        part_name = request.form['part_name']
        cost = int(request.form['cost'])
        brand = request.form['brand']
        part = Part(part_name=part_name, cost=cost, brand=brand)
        session.add(part)
        session.commit()
        return render_template('add_part.html', success=True)
    else:
        return render_template('add_part.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
