# Simple Banking System

O objetivo é desenvolver uma ferramenta de criação de cartões de crédito, armazenando-los em um banco de dados relacional. Com a criação de um cartão de crédito há a possibilidade de fazer *log in* na conta do cartão e creditar, depositar ou transferir dinheiro. Há a possibilidade de **deletar** a conta, tanto no programa quanto no banco de dados, respeitando a [Lei Geral de Proteção de Dados Pessoais (LGPD)](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) 😉.

## Aprendizado

O objetivo faz com que o projeto seja robusto com a utilização de bastante recursos do Python, como classes e instâncias, biblioteca `random` e SQLite.

## Tecnologia abordada

 - SQL

## Exemplo

> O símbolo de maior que é seguido por um espaço (> ) representa a entrada do usuário. 

	1. Create an account
	2. Log into account
	0. Exit
	>1

	Your card has been created
	Your card number:
	4000009455296122
	Your card PIN:
	1961

	1. Create an account
	2. Log into account
	0. Exit
	>1

	Your card has been created
	Your card number:
	4000003305160034
	Your card PIN:
	5639

	1. Create an account
	2. Log into account
	0. Exit
	>2

	Enter your card number:
	>4000009455296122
	Enter your PIN:
	>1961

	You have successfully logged in!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>2

	Enter income:
	>10000
	Income was added!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>1

	Balance: 10000

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305160035
	Probably you made a mistake in the card number. Please try again!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305061034
	Such a card does not exist.

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305160034
	Enter how much money you want to transfer:
	>15000
	Not enough money!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>3

	Transfer
	Enter card number:
	>4000003305160034
	Enter how much money you want to transfer:
	>5000
	Success!

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit
	>1

	Balance: 5000

	1. Balance
	2. Add income
	3. Do transfer
	4. Close account
	5. Log out
	0. Exit

	>0
	Bye!


