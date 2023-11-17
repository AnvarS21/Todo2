from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database='todo_db',
    user='anvar',
    password='1',
    host='localhost',
    port=5432
)

# print(db.connect())