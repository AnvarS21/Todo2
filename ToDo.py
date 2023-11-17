# """ 
# Напишите простое приложение Todo, целью которого является ведение списка дел. Приложение должен состоять из двух классов: Todo и TodoItem:

# Инициализатор Todo ничего не принимает. В классе должен быть метод add_todo, который принимает экземпляр класса TodoItem, и добавляет в список todo_items. Метод list_items должен показывать все элементы в списке todo_items. Метод find должен принимать слово в качестве аргумента и выводить список экземпляров TodoItem, которые содержат это слово в виде кортежа, который будет иметь формат (индекс, экземпляр).

import csv
from create import add_status,add_tasks

class Todo:
    def __init__(self):
        self.todo_items = []

    def add_todo(self, examp):
        if isinstance(examp, TodoItem):
            self.todo_items.append(examp)
        
    def list_items(self):
        count = 1
        print('Cписок дел: ')
        for i in self.todo_items:
            print(f'{count}) {i.task}')
            count += 1
        return '    Конец!'
    
    def find(self, word):
        result = []
        count = 1
        for i in self.todo_items:
            if word.lower() in i.task.lower().strip('()*&^%$#@!:;.,/').split():
                result.append(f'{count}) {i.task}')
                count += 1
        result = (*result,)
        return result

        #""" Сделайте так, чтобы приложение работало с командой строки. Подсказка: в качестве меню может выступать словарь, в котором ключем будет номер, значением -- метод. Для этого можете добавить метод run, в котором будет цикл while принимающий input. """
    
    def run(self):
        choice = {1: self.add_todo, 2: self.list_items, 3: self.find}
        print('Выберите метод: \n1 --> Добавить задачу \n2 --> Посмотреть список задач \n3 --> Искать слово в задаче\n5 --> Для обновления и просмотра статуса задания\n6 --> Выйти')
        while True:
            try:
                vybor = int(input('---menu---->     '))
                print()
            except ValueError:
                print('Вводите только цифры!')
                continue
            if vybor == 2:
                choice[vybor]()
            elif vybor == 1:
                obj_totoitem = input('Для создания экземпляра введите название экземпляра: ')
                attribut_obj = input('Введите атрибут экзмепляра: ')
                obj_totoitem = eval('TodoItem(attribut_obj)')
                a = choice[vybor](obj_totoitem)
                self.add_todo(a)


            elif vybor == 3:
                find_word = input('Введите слово: ')
                print(choice[3](find_word))
            
            elif vybor == 5:
                if len(self.todo_items) > 0:
                    a = input('1 --> Просмотр статуса\n2 --> Изменение статуса\n----status-->    ')
                    if a.strip() == '1':
                        for i in self.todo_items:
                            print(i.task,i.is_done)
                    elif a.strip() == '2':
                        numeration = enumerate(i.task for i in self.todo_items)
                        try:
                            index_task = int(input('Введите индекс задачи(Начинается с 0): '))
                            add_dell = input('Если оно выполено введите "+" иначе "-": ')
                        except ValueError:
                            continue
                            print('Ошибка! Начните заново!')
                        for i in numeration:
                            if index_task == i[0]:
                                for u in self.todo_items:
                                    if u.task == i[1]:
                                        if add_dell == '+':
                                            u.check()
                                        else:
                                            u.uncheck()
                            

                    else:
                        print('Неверная команда!')
                else:
                    print('Задач пока нет! Добавьте их!')

            elif vybor == 6:
                print('Пока!')
                break
            else:
                print('Неверная команда!')

        return self.todo_items
    





#""" Инициализатор TodoItem принимает строковое значение. В нем должна быть переменная, сохраняющая состояние is_done. Также в классе должен быть методы check и uncheck, которые меняют состояние is_done.
# Создайте экземпляр Todo, создайте несколько TodoItem, вызовите их методы.

class TodoItem:
    def __init__(self, task):
        self.task = task
        self.is_done = False

    def check(self):
        self.is_done = True
    
    def uncheck(self):
        self.is_done = False




monday = Todo()
monday.run()


# - Добавить БД в виде файла (Приз 100 баллов)
# - Добавить в гит (Приз 100 баллов) """
with open('ToDo.csv', 'w') as file:
    fieldnames = ['№', 'name_exemplyar', 'title', 'status']
    writer = csv.DictWriter(file, fieldnames)
    writer.writerow({
            '№': '№', 
            'name_exemplyar': 'Name:', 
            'title': 'title',
            'status': 'Status'
        })

    count = 1
    for i in monday.todo_items:
        writer.writerow({
            '№': count, 
            'name_exemplyar': i, 
            'title': i.task,
            'status': i.is_done
        })
        count += 1


# add_status('False')
# add_status('True')
add_tasks(monday.todo_items)

