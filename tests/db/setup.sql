drop database if exists test_pandas_rs_db;
drop role if exists test_pandas_rs;
create database test_pandas_rs_db;
create role test_pandas_rs superuser;
alter role test_pandas_rs with login;