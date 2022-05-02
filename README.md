# XalDigital

## How to start
- Clone the repo and run ```docker-compose up``` on the terminal in the root directory.
- Install the depedencies for Python that are located on AddressBook_API/fastapi_app/requirements.txt
- Open the terminal on AddressBook_API/fastapi_app/ and run ```uvicorn main:app --reload```
- Go to the centos container CLI and create the folder LZ using the command ```mkdir /home/LZ```
- On the local host terminal in the root folder, run ```docker cp Sample.csv xaldigital-centos-1:/home/LZ/Sample.csv```
- Go to the centos containter and run the contents of the import.sh (or copy it from the host machine)
- Open the website http://127.0.0.1:8000/docs#/ to use the API
