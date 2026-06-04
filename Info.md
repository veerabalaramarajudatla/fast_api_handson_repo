## Fast API Repo ##

--- List of Packages Installed ---
-> pip install fastapi uvicorn
-> pip install -r requirements.txt

--- File Architecture ---
fastapi-project/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── employee.py
│   ├── models/
│   │   └── employee.py
│   ├── schemas/
│   │   └── employee.py
│   ├── database/
│   │   └── connection.py
│   └── services/
│       └── employee_service.py
│
├── requirements.txt
└── Dockerfile

--- Run Cmd ---
uvicorn main:app --reload

--- List of API ---
