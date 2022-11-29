#!/usr/bin/python

import psycopg2
import psycopg2.extras
from psycopg2 import pool
import uuid

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
                    email text NOT NULL,
                    password text NOT NULL,
                    CONSTRAINT "user_pkey" PRIMARY KEY (email)                    
                );
                CREATE TABLE IF NOT EXISTS chess.score
                (
                    user_email text NOT NULL,
                    score integer NOT NULL,
                    level integer NOT NULL,
                    ts timestamptz NOT NULL DEFAULT NOW(),
                    CONSTRAINT "scores_pkey" PRIMARY KEY (user_email, ts),
                    CONSTRAINT fk_scores_user
                        FOREIGN KEY(user_email) 
	                    REFERENCES chess.user(email)
                        ON DELETE CASCADE                    
                );
            """        
            )

            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
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

        finally:
            self.pool.putconn(conn)

    def add_user(self, email, password):

        command = """
            INSERT INTO chess.user(email, password)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING;"""
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor()

            # create table one by one        
            cur.execute(command, (email, password))
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
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
        

    def get_high_score(self, user_email):
        # TODO
        # very similar to get_user_by_email
        command = """SELECT * FROM chess.score 
                     WHERE user_email = %s
                     ORDER BY score DESC 
                     LIMIT 1"""
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

            # create table one by one        
            cur.execute(command, (user_email,))
            records = cur.fetchall()
            if records:
                return records[0]
            else:
                return None
        
        finally:
            self.pool.putconn(conn)
        

    def save_score(self, user_email, score, level):
        command = """INSERT INTO chess.score(user_email, score, level) VALUES (%s, %s, %s)"""
        conn = self.pool.getconn()
        try:
           # read the connection parameters
           # params = config()
           # connect to the PostgreSQL server
            cur = conn.cursor()

            # create table one by one        
            cur.execute(command, (user_email, score, level))
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            self.pool.putconn(conn)

