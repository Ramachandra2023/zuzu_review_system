# zuzu_review_system
ZuZu review system microservice 

This microservice ingests hotel review data (in .jl format) from an AWS S3 bucket, processes and validates it, and stores it into a relational database (PostgreSQL or MySQL). Designed with modularity, error handling, and scalability in mind.

   Features:

   ✅ Connects to AWS S3 and downloads .jl review files

   ✅ Parses JSON Lines and validates review data

   ✅ Stores reviews in a relational database using SQLAlchemy ORM

   ✅ Tracks processed files for idempotency (no duplicate processing)

   ✅ Dockerized setup

   ✅ Command-line or cron-job compatible

   ✅ Logs errors and activity to console

  Setup Intructions:

  Clone Project :
  
  git clone https://github.com/your-username/zuzu_review_system.git
  
  cd zuzu_review_system

  Configure Environment Variables:
   
  Create .env file:

   AWS_ACCESS_KEY=your_aws_access_key
   AWS_SECRET_KEY=your_aws_secret_key
   AWS_BUCKET_NAME=zuzu-review-bucket
   S3_PREFIX=reviews/
   DB_URI=postgresql://user:password@db/review_db

  Build and run using docker :

   docker build -t review-service .
   docker run --env-file .env review-service

   Runnning Tests:

   pip install -r requirements.txt
   pytest tests/

  Design Decisions:

   Idempotency: Implemented using a processed_files DB table to track completed files.

   ORM: SQLAlchemy ensures flexibility between PostgreSQL and MySQL.

   Extensibility: Designed to add multilingual support, rating systems, and new platforms easily.

   Assumptions:

   Each .jl file represents one full day’s reviews from one platform.

   The comment block is required and must include rating, reviewDate, and reviewComments.

   Duplicate file processing is prevented via tracked filenames in DB.

   



