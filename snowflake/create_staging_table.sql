/*--

Helpful Snowflake Documentation:
    1. Bulk Loading from Amazon S3 - https://docs.snowflake.com/en/user-guide/data-load-s3
    2. Bulk Loading from Microsoft Azure - https://docs.snowflake.com/en/user-guide/data-load-azure
    3. Bulk Loading from Google Cloud Storage - https://docs.snowflake.com/en/user-guide/data-load-gcs
--*/


-- Step 1: To start, let's set the Role and Warehouse context
    -- USE ROLE: https://docs.snowflake.com/en/sql-reference/sql/use-role
    -- USE WAREHOUSE: https://docs.snowflake.com/en/sql-reference/sql/use-warehouse

-- set role context
USE ROLE accountadmin;

-- set warehouse context
USE WAREHOUSE compute_wh;

-- SET allowed_storage_path = ('azure://myaccount.blob.core.windows.net/mycontainer1/mypath1/');

-- Step 2: Create Database
    -- CREATE DATABASE: https://docs.snowflake.com/en/sql-reference/sql/create-database
-- create database
CREATE DATABASE IF NOT EXISTS dev_spotify_data;

-- Step 3: Create Schema
    -- CREATE SCHEMA: https://docs.snowflake.com/en/sql-reference/sql/create-schema
-- create the schema
CREATE SCHEMA IF NOT EXISTS dev_spotify_data.test;

-- Step 4: Create Table
    -- CREATE TABLE: https://docs.snowflake.com/en/sql-reference/sql/create-table
-- create the table
CREATE TABLE IF NOT EXISTS dev_spotify_data.test.staging_events (
    first_name  VARCHAR(255) NOT NULL,
  last_name   VARCHAR(255) NOT NULL,
  gender      VARCHAR(20) NOT NULL,
  city        VARCHAR(255) NOT NULL,
  state       VARCHAR(50) NOT NULL,
  country     VARCHAR(30) NOT NULL,
  latitude    DECIMAL(5,3) NOT NULL,
  longitude   DECIMAL(5,3) NOT NULL,
  listen_timestamp BIGINT NOT NULL,
  song_id     VARCHAR(255) NOT NULL,
  artist_name  VARCHAR(255) NOT NULL,
  artist_id   VARCHAR(255) NOT NULL,
  song_title  VARCHAR(255) NOT NULL,
  album_name  VARCHAR(255) NOT NULL,
  release_date DATE NOT NULL,
  duration_ms  BIGINT NOT NULL,
  danceability  DECIMAL(10,3) NOT NULL,
  energy       DECIMAL(10,3) NOT NULL,
  key          INT NOT NULL,
  loudness    DECIMAL(10,3) NOT NULL,
  mode         INT NOT NULL,
  speechiness   DECIMAL(10,3) NOT NULL,
  acousticness  DECIMAL(10,3) NOT NULL,
  instrumentalness DECIMAL(10,3) NOT NULL,
  liveness     DECIMAL(10,3)NOT NULL,
  valence      DECIMAL(10,3) NOT NULL,
  tempo        DECIMAL(10,3) NOT NULL,
  year         INT NOT NULL,
  month        INT NOT NULL,
  hour         INT NOT NULL,
  day          INT NOT NULL,
  duration_minutes DECIMAL(20,3) NOT NULL,
  full_name    VARCHAR(255) NOT NULL
    )
    COMMENT = 'staging table for storing raw spotify stream events';

-- query the empty table
SELECT * FROM dev_spotify_data.test.staging_events;

-- Step 6: Create Roles to manage access
    -- CREATE ROLE: https://docs.snowflake.com/en/sql-reference/sql/create-role 
CREATE OR REPLACE ROLE dev_role;
GRANT ROLE dev_role TO USER abdkumar;
GRANT USAGE ON WAREHOUSE compute_wh TO ROLE dev_role;
GRANT USAGE ON DATABASE dev_spotify_data TO ROLE dev_role;
GRANT USAGE ON SCHEMA dev_spotify_data.test TO ROLE dev_role;
GRANT ALL ON ALL TABLES IN SCHEMA dev_spotify_data.test  TO ROLE dev_role;
GRANT ALL ON FUTURE TABLES IN SCHEMA dev_spotify_data.test  TO ROLE dev_role;



CREATE ROLE stagingrole;
GRANT ROLE stagingrole TO USER abdkumar;
GRANT USAGE ON WAREHOUSE compute_wh TO ROLE stagingrole;
GRANT USAGE ON DATABASE dev_spotify_data TO ROLE stagingrole;
GRANT USAGE ON SCHEMA dev_spotify_data.test to ROLE stagingrole;
GRANT SELECT, INSERT ON TABLE dev_spotify_data.test.staging_events TO ROLE  stagingrole;
GRANT SELECT ON ALL TABLES IN SCHEMA dev_spotify_data.test TO ROLE stagingrole;
GRANT CREATE STAGE ON SCHEMA dev_spotify_data.test TO ROLE stagingrole;


-- Step 7: Testing Roles
-- use role stagingrole;
-- SELECT * FROM dev_spotify_data.test.staging_events;


SELECT COUNT(*) FROM dev_spotify_data.test.staging_events;

SELECT COUNT(*) FROM dev_spotify_data.test.staging_events;

-- DELETE FROM dev_spotify_data.test.staging_events;