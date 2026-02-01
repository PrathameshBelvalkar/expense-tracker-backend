web: gunicorn expense_tracker_backend.wsgi:application \
     --bind 0.0.0.0:$PORT \
     --workers 3 \
     --access-logfile - \
     --error-logfile - \
     --timeout 120
