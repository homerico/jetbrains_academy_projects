from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, create_engine
from datetime import datetime

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Nothing')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


def add_task(task):
    global session
    new_row = Table(task=task)
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def show_all_tasks():
    global session
    rows = session.query(Table).all()
    print("Today:")
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        for i, row in enumerate(rows, start=1):
            print(f"{i}. {row}")


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

while True:
    user_input = int(input("""1) Today's tasks
2) Add task
0) Exit\n"""))
    if user_input == 0:
        break
    elif user_input == 1:
        show_all_tasks()
    elif user_input == 2:
        user_input = input("Enter task\n")
        add_task(user_input)

print("Bye!")

