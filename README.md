# Simple Web App in Flask and Redis

The application for interaction between Flask and Redis. It has a simple web interface.
Using the interface, you can enter a key-value pair into the Redis DB, request values by key, change values.

The application is launched in two docker containers.

Container 1:
- Alpine Linux 3.17
- Python 3.10
- Flask 3.0.0

Container 2:
- Alpine Linux 3.18
- Redis 7.2

The application available on `127.0.0.1:8080`.

### To start the app you need to enter the command:

    docker compose up -d
