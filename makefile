FEED = $(shell chmod u+rwx ./feedDB.py)

run_project:
	source venv/bin/activate && export FLASK_ENV=development && python3 manage.py run

empty_db:
	echo 'DELETE FROM ingredient;DELETE FROM beverage;DELETE FROM side_order;DELETE FROM "order";DELETE FROM size;' > instructions.sql
	sqlite3 pizza.sqlite < instructions.sql 
	rm instructions.sql

feed_db:
	python feedDB.py

run_lint:
	flake8

run_test:
	pytest