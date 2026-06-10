## Fast API Repo ##


--- List of Packages Installed ---

-> pip install fastapi uvicorn

-> pip install -r requirements.txt

-> pip install sqlalchemy pymysql

-> pip install pymysql

-> pip install psycopg2-binary / pip install psycopg


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