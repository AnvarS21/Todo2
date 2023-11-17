import peewee
from models import Status, Tasks

def add_status(s):
    try:
        data = Status(status=s.title())
        data.save()
        print(f'Сохранили статус {s}')
    except:
        print('Такая категория уже существует!')

def add_tasks(todo_examp):
    for i in todo_examp:
        status_id = Status.get(status=i.is_done)
        data = Tasks(name=i, title=i.task, status_id=status_id)
        data.save()
    print('Все сохранено!')
    
