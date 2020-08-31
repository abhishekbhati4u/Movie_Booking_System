import sqlite3
Movie=sqlite3.connect('movies.db')
movies_curs=Movie.cursor()
movies_curs.execute('''CREATE TABLE ticket (
    TicketID INTEGER PRIMARY KEY,
    user_name TEXT (40) NOT NULL,
    phone_no TEXT(10) NOT NULL,
    start_hrs INTEGER NOT NULL,
    start_mins INTEGER NOT NULL,
    end_hrs INTEGER NOT NULL,
    end_mins INTEGER NOT NULL,
    status TEXT(10) NOT NULL
    );''')
movies_curs.execute('''CREATE TABLE ticket_status (
    no INTEGER PRIMARY KEY,
    start_hrs INTEGER NOT NULL,
    start_mins INTEGER NOT NULL,
    end_hrs INTEGER NOT NULL,
    end_mins INTEGER NOT NULL
    );''')
Movie.close() 
