all:
	mysql < TAT.sql

install:
	pip install --user -r requirements.txt
