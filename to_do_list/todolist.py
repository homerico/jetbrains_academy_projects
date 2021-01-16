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
        print("All tasks:")
        for i, row in enumerate(rows, start=1):
            print(f"{i}. {row}. {row.deadline.strftime('%-d %b')}")
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
4) Add task
0) Exit\n"""))
    if user_input == 0:
        break
    elif user_input == 1:
        show_all_tasks("today")
    elif user_input == 2:
        show_all_tasks("week")
    elif user_input == 3:
        show_all_tasks()
    elif user_input == 4:
        task_outer = input("Enter task\n")
        deadline_outer = input("Enter deadline\n")
        add_task(task_outer, deadline_outer)

print("Bye!")
