# Liwwa Assessment

simple flask api/webapp 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Prerequisites
* [PYTHON 3.6+](https://python.org)
* [Mariadb](https://mariadb.org/download/) 

### Virtual Environments
Example:
```
python -m venv liwwaenv
liwwaenv\Scripts\activate.bat
pip install -r requirements.txt
```

### Start webapp
```
liwwaenv\Scripts\activate.bat
python run.py
```


## Run
__init__.py
```
database_username ="root"
database_password ="root"
#config your password and your username
```

### API
example:
```
*[POST] http://127.0.0.1:5000/api/registration 
request body -- > {"name":"ashrf s alroomi" , "birth_date":"8-15-1996" ,"year_of_exp":5 ,"dep":it , "cv":file }
response --> {"success":True}



*[GET]  http://127.0.0.1:5000/api/admin?skip=1&limit=5
request args -- > skip = 0 , limit = 2
request header --> {.. , "X-ADMIN":1}
response --> {
    "users": [
        {
            "Birthday": "2018-09-09",
            "Department": "IT",
            "Experience": 0,
            "Full Name": "ashraf alroomi ss"
        },
        {
            "Birthday": "2018-09-09",
            "Department": "IT",
            "Experience": 0,
            "Full Name": "ashraf alroomi ss"
        }
    ]
}



*[GET]  http://127.0.0.1:5000/api/download/6
request header --> {.. , "X-ADMIN":1}
response --> file

```

### Website
example:
```
*[GET] http://127.0.0.1:5000/
*[GET] http://127.0.0.1:5000/admin
```
![alt text](https://github.com/AshrafAlroomi/liwwa/blob/main/admin.jpg?raw=true)


## Notes 

* the files are uploaded localy in cvs file , i could uploaded to s3 bucket but puting aws credentials in public repository are not safe todo.
* the /download/userid request can be invoked with postman.

