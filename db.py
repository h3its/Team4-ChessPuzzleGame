#!/usr/bin/python

import psycopg2
import psycopg2.extras
from psycopg2 import pool
import uuid
# from config import config

class ChessDB:
    def __init__(self, dbname, user, password, host, port):
        self.pool = psycopg2.pool.SimpleConnectionPool(1, 2, database=dbname, user=user, password=password, host=host, port=port)
        psycopg2.extras.register_uuid()
        self.__create_tables()

    def __create_tables(self):
        """ create tables in the PostgreSQL database"""
        conn = self.pool.getconn()
        try:
            # read the connection parameters
            # params = config()
            # connect to the PostgreSQL server
            cur = conn.cursor()

            #TODO: add foreign key to score table
            cur.execute("""
                CREATE SCHEMA IF NOT EXISTS chess;               
                CREATE TABLE IF NOT EXISTS chess.user
                (
                    id uuid NOT NULL,
                    email text NOT NULL,
                    password text NOT NULL,
                    CONSTRAINT "user_pkey" PRIMARY KEY (id), 
                    CONSTRAINT "unq_email" UNIQUE (email)
                );
                CREATE TABLE IF NOT EXISTS chess.score
                (
                    user_id uuid NOT NULL,
                    score integer NOT NULL,
                    level integer NOT NULL,
                    ts timestamptz NOT NULL DEFAULT NOW(),
                    CONSTRAINT "scores_pkey" PRIMARY KEY (user_id, ts)
                );
            """        
            )

            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("FAIL!!!")
            print(error)
        finally:
            if conn is not None:
                self.pool.putconn(conn)

    def list_users(self):
        command = """SELECT id, email, password FROM chess.user ORDER BY email"""
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
            cur.execute(command)
            records = cur.fetchall()
            return records # this will be a dict{id: x, email: x, password: x}

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.pool.putconn(conn)

    def add_user(self, email, password):

        command = """INSERT INTO chess.user(id, email, password) VALUES (%s, %s, %s)"""
        print(command)
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor()


            # create table one by one        
            cur.execute(command, (uuid.uuid4(), email, password))
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.pool.putconn(conn)

    def get_user_by_email(self, email):
        # TODO
        # 1. use list_users as guide
        # 2. define SQL statement
        command = """SELECT * FROM chess.user WHERE email = %s"""
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
            cur.execute(command, (email,))
            records = cur.fetchall()
            if records:
                return records[0]
            else:
                return None

        finally:
            self.pool.putconn(conn)
        

    def get_high_score(self, user_id):
        # TODO
        # very similar to get_user_by_email
        command = """SELECT * FROM chess.score 
                     WHERE user_id = %s
                     ORDER BY score DESC 
                     LIMIT 1"""
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor()

            # create table one by one        
            cur.execute(command, (user_id,))
            records = cur.fetchall()
            if records:
                return records[0]
            else:
                return None
        
        finally:
            self.pool.putconn(conn)
        

    def save_score(self, user_id, score, level):
        command = """INSERT INTO chess.score(user_id, score, level) VALUES (%s, %s, %s)"""
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor()


            # create table one by one        
            cur.execute(command, (user_id, score, level))
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.pool.putconn(conn)

if __name__ == '__main__':
    db = ChessDB(dbname="postgres", user="postgres", password="example", host="localhost", port=5432)

    email = str(uuid.uuid4()) + "@bar.com"
    db.add_user(email, "bar")

    saved_user = db.get_user_by_email(email)
    print(saved_user)
    db.save_score(saved_user['id'], 100, 5)
    db.save_score(saved_user['id'], 120, 6)
    db.save_score(saved_user['id'], 90, 4)

    high_score = db.get_high_score(saved_user['id'])
    print(high_score)

    # print(str(high_score))

    # users = db.list_users()

    # db.save_score(user_id, )

    # for user in users:
    #     print("%s", user['id'])
