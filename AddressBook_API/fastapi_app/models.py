from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from database import Base
 
 
class AddressBook(Base):
 
    __tablename__ = "tbl_addressbook"
 
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    company_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    phone1 = Column(String)
    phone2 = Column(String)
    email = Column(String)
    department = Column(String)