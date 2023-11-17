import peewee
from main import db

class Status(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    status = peewee.CharField(max_length=5, unique=True)

    class Meta:
        database = db
        dt_table = 'Statuses'

class Tasks(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    name = peewee.CharField(max_length=50, unique=True)
    title = peewee.TextField(null=False)
    status_id = peewee.ForeignKeyField(Status, to_field='status')
    
    class Meta:
        database = db
        dt_table = 'ToDo'


# print(db.connect()),k
# Status.create_table()
# Tasks.create_table()
