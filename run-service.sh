docker network rm proxy || true

docker network create proxy

touch acme.json && chmod 600 acme.json

docker-compose up --build -d

docker-compose exec sustainability python manage.py migrate --noinput