import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS Entries''')

    cur.execute('''CREATE TABLE Entries (PersonID INTEGER PRIMARY KEY NOT NULL,
                                            PersonName TEXT NOT NULL,
                                            PhoneNumber TEXT NOT NULL )''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
