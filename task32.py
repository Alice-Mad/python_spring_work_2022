# # todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# # Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# # В задании использовать библиотеку psycopg
#
#
# Ссылка на документацию
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# Для подключения использовать пользователя и базу отличную от postgres

import psycopg
with psycopg.connect("dbname=postgres_32 user=user_32") as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE group (
                  id_group serial PRIMARY KEY,
                  group_name varchar(10) not null,
            """)
        cur.execute("""
            CREATE TABLE student (
                id_student serial PRIMARY KEY,
                id_group integer not null,
                surname varchar(40) not null,
                name varchar(30) not null,
                second name varchar(30) not null,
                age integer not null
            """)
# Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO group (group_name) VALUES (%s)", "1510")
# Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM group")
        cur.fetchone()
# Try to create a constraint
        cur.execute("""
            ALTER TABLE "student"
            ADD CONSTRAINT "group_student_constraint"
            FOREIGN KEY("id_group")
            REFERENCES "User" ("id_group")
            ON DELETE RESTRICT
            """)
