format:
	cd backend;	poetry run black .
unit-test:
	cd backend; poetry run pytest -v
start-db:
	cd backend; docker-compose up -d --build
stop-db:
	cd backend; docker-compose down