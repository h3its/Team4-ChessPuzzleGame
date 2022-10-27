#!/usr/bin/python

import psycopg2
# from config import config

def show_vendors():
    command = """SELECT * FROM vendors"""
    conn = None
    try:
        # read the connection parameters
        # params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="example", host="localhost", port=5432)
        cur = conn.cursor()


        # create table one by one        
        cur.execute(command)

        records = cur.fetchall()

        for record in records:
            print(record)
            #for r in record:
            #    print(r)

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        # conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()  

def add_vendor():
    command = """INSERT INTO vendors(vendor_name) VALUES ('Shane')"""
    conn = None
    try:
        # read the connection parameters
        # params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="example", host="localhost", port=5432)
        cur = conn.cursor()


        # create table one by one        
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()    

def create_tables():
    """ create tables in the PostgreSQL database"""
    conn = None
    try:
        # read the connection parameters
        # params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="example", host="localhost", port=5432)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS vendors (
                vendor_id SERIAL PRIMARY KEY,
                vendor_name VARCHAR(255) NOT NULL
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
            conn.close()


if __name__ == '__main__':
    create_tables()
    add_vendor()
    show_vendors()