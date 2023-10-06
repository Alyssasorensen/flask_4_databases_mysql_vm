from flask import Flask, render_template
from sqlalchemy import create_engine
from pandas import read_sql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect

app = Flask(__name__)

load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")


# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    "?charset=utf8mb4"
)

# Database connection settings
db_engine = create_engine(conn_string, echo=False)

@app.route('/')
def index():
    # Example SQL query (modify as needed)
    sql_query = "SELECT * FROM medications"
    df = read_sql(sql_query, db_engine)
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
