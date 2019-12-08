import sqlite3
from flask import g

def get_db(database_name):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database_name)
    return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

def query_db(db, query, args=(), one=False):
    cur = db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv