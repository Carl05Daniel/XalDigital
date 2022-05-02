from typing import Optional

from pydantic import BaseModel

class AddressBookBase(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    address: str
    city: str
    state: str
    zip: str
    phone1: str
    phone2: str
    email: str
    department: str

class AddressBookCreate(AddressBookBase):
    pass

class AddressBook(AddressBookBase):
    id: int
    
    class Config:
        orm_mode = True