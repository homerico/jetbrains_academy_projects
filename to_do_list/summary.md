# To-Do List

Fazer uma lista de tarefas básica e intuitiva com armazenamento em banco de dados. Deve-se inserir a data da seguinte forma:
`{ANO}-{MES}-{DIA}`

## Aprendizado

Os tópicos abordados do projeto tiveram bastante teoria, principalmente sobre **SQL** e ***Object-Relational Mapping (ORM)***. Foi utilizado a biblioteca `SQLAlchemy`, que é um *toolkit* e ORM do SQLite, e o `datetime`.

## Tecnologia abordada

 - SQL

## Exemplos

> O símbolo de maior que é seguido por um espaço (> ) representa a entrada do usuário. 

### Exemplo 1

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 1

	Today 26 Apr:
	Nothing to do!

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 5

	Enter task
	>Meet my friends
	Enter deadline
	>2020-04-28
	The task has been added!

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 2

	Sunday 26 Apr:
	Nothing to do!

	Monday 27 Apr:
	Nothing to do!

	Tuesday 28 Apr:
	1. Meet my friends

	Wednesday 29 Apr:
	Nothing to do!

	Thursday 30 Apr:
	1. Math homework
	2. Call my mom

	Friday 1 May:
	1. Order a new keyboard 

	Saturday 2 May:
	Nothing to do!

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	>3

	All tasks:
	1. Meet my friends. 28 Apr
	2. Math homework. 30 Apr
	3. Call my mom. 30 Apr
	4. Order a new keyboard. 1 May

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 0

	Bye!

### Exemplo 2

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 4

	Missed tasks:
	1. Learn the for-loop. 19 Apr

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 6

	Choose the number of the task you want to delete:
	1. Learn the for-loop. 19 Apr
	2. Learn the basics of SQL. 29 Apr
	> 1
	The task has been deleted!

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 4

	Missed tasks:
	Nothing is missed!

	1) Today's tasks
	2) Week's tasks
	3) All tasks
	4) Missed tasks
	5) Add task
	6) Delete task
	0) Exit
	> 0

	Bye!