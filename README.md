This microservice ingests hotel review data from AWS S3, processes it asynchronously using RabbitMQ, stores it in a relational database, and caches recent data in Redis for fast access.

Features

1) Fetches daily .jl review files from AWS S3.

2) Validates and parses JSON Lines review data.

3) Uses RabbitMQ for asynchronous, scalable processing.

4) Stores reviews in PostgreSQL/MySQL using SQLAlchemy ORM.

5) Caches recent reviews in Redis for quick retrieval.

6) Tracks processed files to ensure idempotency.

7) Dockerized setup with multi-service orchestration via Docker Compose.

8) Unit tests included for core components.

Setup Instructions

Prerequisites

1) Docker & Docker Compose installed

2) AWS credentials with S3 read access

3) PostgreSQL or MySQL database accessible

4) Redis server accessible

Created .env

