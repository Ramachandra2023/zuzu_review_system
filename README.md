# zuzu_review_system
ZuZu review system microservice 

1) Setup:

   bash -

   docker build -t review-service .

   docker run --env-file .env review-service

3) Design Desitions :

   Modular architecture

   SQLAlchemy ORM for DB flexibility 

   Logging and idempotency via metadata table (planned)

5) Assumptions :

   Review files are not reprocessed (to be enhanced)

   S3 permissions are set

   One .jl file = 1 day's worth of reviews



