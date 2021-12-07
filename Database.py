import psycopg2

def connect():
    return psycopg2.connect(
        user="itqsairb",
        password="WM9zBNLbxiOlMwNRozSINkOLX0c01ppO",
        host="abul.db.elephantsql.com",
        port="5432",
        database="itqsairb"
    )

def close(connect):
    connect.commit()
    connect.close()