until python manage.py migrate; do
echo "Migrations failed, retrying in 3 seconds..."
sleep 3
done

daphne --bind=0.0.0.0 --port=8000 core.asgi:application