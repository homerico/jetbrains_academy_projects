# Text-Based Browser

O projeto consiste em fazer um **navegador simples** que ignora JavaScript e CSS, assim como não tem *cookies*. Toda a navegação é por meio do ***Command Line Interface(CLI)*** do Sistema Operacional e só são exibidas algumas tags do HTML. O comando no CLI deve ser:

	python browser.py abas_do_navegador

Em `abas_do_navegador`, deve-se colocar o nome da pasta em que será salvo o conteúdo dos sites em que foram requisitados. Há a opção de voltar ao site anterior digitando `back`. O programa fecha quando digita `exit`

## Aprendizado

Foram utilizadas algumas bibliotecas frequentemente usadas para desenvolvimento, como `sys` e `os`, da mesma forma que foram usadas bibliotecas populares para projetos em que se trabalha com HTML e requisições por HTTP, como `requests` e `BeautifulSoup`.

## Tecnologia abordada

 - HTML;
 - HTTP e HTTPS; e 
 - XML

## Exemplo

> Os dois símbolos de maior que é seguido por um espaço (>> ) representa a entrada do usuário no CLI do Sistema Operacional e o símbolo de maior que é seguido por um espaço (> ) representa a entrada do usuário na execução do *script*. 

	>> python browser.py abas

	> https://docs.python.org
	index
	modules
	Python
	Documentation
	Python 3.7.4 documentation
	Welcome! This is the documentation for Python 3.7.4.
	Parts of the documentation:
	What's new in Python 3.7? or all "What's new" documents since 2.0
	Tutorial start here
	Library Reference keep this under your pillow
	Language Reference describes syntax and language elements
	Python Setup and Usage how to use Python on different platforms
	Python HOWTOs in-depth documents on specific topics
	Installing Python Modules installing from the Python Package Index & other sources
	Distributing Python Modules publishing modules for installation by others
	Extending and Embedding tutorial for C/C++ programmers
	Python/C API reference for C/C++ programmers
	FAQs frequently asked questions (with answers!)
	Indices and tables:
	Global Module Index quick access to all modules
	General Index all functions, classes, terms
	Glossary the most important terms explained
	Search page search this documentation
	Complete Table of Contents lists all sections and subsections
	Meta information:
	Reporting bugs
	About the documentation
	History and License of Python
	Copyright

	> youtube.com

	Sobre
	Imprensa
	Direitos autorais
	Entre em contato
	Criadores de conteúdo
	Publicidade
	Desenvolvedores
	Termos
	Privacidade
	Política e segurança
	Como funciona o YouTube
	Testar os novos recursos
	
	> back

	index
	modules
	Python
	Documentation
	Python 3.7.4 documentation
	Welcome! This is the documentation for Python 3.7.4.
	Parts of the documentation:
	What's new in Python 3.7? or all "What's new" documents since 2.0
	Tutorial start here
	Library Reference keep this under your pillow
	Language Reference describes syntax and language elements
	Python Setup and Usage how to use Python on different platforms
	Python HOWTOs in-depth documents on specific topics
	Installing Python Modules installing from the Python Package Index & other sources
	Distributing Python Modules publishing modules for installation by others
	Extending and Embedding tutorial for C/C++ programmers
	Python/C API reference for C/C++ programmers
	FAQs frequently asked questions (with answers!)
	Indices and tables:
	Global Module Index quick access to all modules
	General Index all functions, classes, terms
	Glossary the most important terms explained
	Search page search this documentation
	Complete Table of Contents lists all sections and subsections
	Meta information:
	Reporting bugs
	About the documentation
	History and License of Python
	Copyright

	> exit