from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Store, Customer, Part

if __name__ == '__main__':
    engine = create_engine('sqlite:///p3_project.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add code here to query the database or perform other operations
    # using the SQLAlchemy session object.
    
    import ipdb; ipdb.set_trace()
