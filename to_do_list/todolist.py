from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, create_engine
from datetime import datetime, timedelta

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Nothing')
    deadline = Column(Date, default=datetime.now())

    def __repr__(self):
        return self.task


def add_task(task, deadline):
    global session
    new_row = Table(task=task, deadline=datetime.strptime(deadline, '%Y-%m-%d'))
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def print_this_day(rows):
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        for i, row in enumerate(rows, start=1):
            print(f"{i}. {row}")


def filter_by_date(date):
    rows = session.query(Table).filter(Table.deadline == date.date())
    rows = rows.order_by(Table.deadline).all()
    return rows


def show_all_tasks(period="all"):
    global session
    if period == "all":
        rows = session.query(Table).order_by(Table.deadline).all()
        for i, row in enumerate(rows, start=1):
            print(f"{i}. {row}. {row.deadline.strftime('%-d %b')}")
        return rows
    elif period == "today":
        today = datetime.today()
        rows = filter_by_date(today)
        print(f"Today {today.strftime('%-d %b')}:")
        print_this_day(rows)
    elif period == "week":
        today = datetime.today()
        for i in range(7):
            date = today + timedelta(days=i)
            rows = filter_by_date(date)
            print()
            print(date.strftime("%A %-d %b:"))
            print_this_day(rows)


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

while True:
    user_input = int(input("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit\n"""))
    if user_input == 0:
        break
    elif user_input == 1:
        show_all_tasks("today")
    elif user_input == 2:
        show_all_tasks("week")
    elif user_input == 3:
        print("All tasks:")
        show_all_tasks()
    elif user_input == 4:
        print("Missed tasks:")
        outer_rows = session.query(Table).filter(Table.deadline < datetime.today().date())
        outer_rows = outer_rows.order_by(Table.deadline).all()
        if len(outer_rows) == 0:
            print("Nothing is missed!")
        else:
            for j, outer_row in enumerate(outer_rows, start=1):
                print(f"{j}. {outer_row}. {outer_row.deadline.strftime('%-d %b')}")
        print()
    elif user_input == 5:
        outer_task = input("Enter task\n")
        outer_deadline = input("Enter deadline\n")
        add_task(outer_task, outer_deadline)
    elif user_input == 6:
        print("Choose the number of the task you want to delete:")
        outer_rows = show_all_tasks()
        user_input = int(input())
        session.delete(outer_rows[user_input - 1])
        session.commit()
        print("The task has been deleted!")

print("Bye!")