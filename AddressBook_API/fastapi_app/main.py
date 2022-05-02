from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/AddressBook/", response_model=list[schemas.AddressBook])
def read_AddressBook(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addbook = crud.get_addressbook(db, skip=skip, limit=limit)
    return addbook

@app.get("/AddressBook/{addressbook_id}", response_model=schemas.AddressBook)
def read_Address(addressbook_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, addressbook_id=addressbook_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@app.post("/AddressBook/", response_model=schemas.AddressBook)
def create_Address(address: schemas.AddressBookCreate, db: Session = Depends(get_db)):
    return crud.create_address(db=db, address=address)