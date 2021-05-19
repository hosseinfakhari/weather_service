#!/bin/bash
python manage.py compilemessages
daphne -b 0.0.0.0 -p 8000 weatherservice.asgi:application