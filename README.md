# Simple Flask text document analyzer

## Run

1. Make sure that you have working Python 3.8.

2. If you want, create python virtualenv.

3. Install the required packages:

    - `python -m pip install -r ./requirements.txt`

4. Run application server:

    - `python.exe summary_app/app.py`
    
5. Create the sqlite database `db.sqlite` in the `summary_app` directory (`./summary_app/db.sqlite`). The `database_schema.sql` file contains a query to create tables.

## API

After starting the application go to `http://localhost:8888/api/` address there is swagger documentation available.