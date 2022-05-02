from sqlalchemy.orm import Session

import models, schemas

def get_address(db: Session, addressbook_id: int):
    return db.query(models.AddressBook).filter(models.AddressBook.id == addressbook_id).first()

def get_addressbook(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AddressBook).offset(skip).limit(limit).all()

def create_address(db: Session, address: schemas.AddressBookCreate):
    db_address = models.AddressBook(
        first_name = address.first_name,
        last_name = address.last_name,
        company_name = address.company_name,
        address =  address.address,
        city = address.city,
        state = address.state,
        zip = address.zip,
        phone1 = address.phone1,
        phone2 = address.phone2,
        email = address.email,
        department = address.department)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address