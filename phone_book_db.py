import sqlite3

# CRUD
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
QUIT = 5


def display_menu():
    print('\n-----Select from Menu-----')
    print('1: Add a new entry')
    print('2: Lookup a phone number')
    print('3: Change a phone number')
    print('4: Delete an entry')
    print('5: Quit app')


def get_menu_choice():
    choice = int(input('Enter your selection: '))
    while choice < CREATE or choice > QUIT:
        print(f'Invalid selection. Enter selection from {CREATE} to {QUIT} only.')
        choice = int(input('Enter your selection: '))
    return choice


def insert_entry(name, phone):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Entries (PersonName, PhoneNumber)
                        VALUES (?, ?)''',
                    (name, phone))
        conn.commit()
    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def create_entry():
    print('Add a new entry to phonebook')
    name = input('Name: ')
    phone = input('Phone Number: ')
    insert_entry(name, phone)


def display_entry(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''SELECT PersonID, PersonName, PhoneNumber
                        FROM Entries
                        WHERE PersonName = ?''',
                    (name,))
        results = cur.fetchall()

        print(f'The results of your query for the name: {name}')
        for row in results:
            print(f'ID: {row[0]}\nName: {row[1]}\nPhone Number: {row[2]}')
            print('------------------------------------------------------')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def read_entry():
    name = input('Enter the name you are searching for: ')
    display_entry(name)


def update_entry_row(id, name, phone):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Entries
                        SET PersonName = ?, PhoneNumber = ?
                        WHERE PersonID = ?''',
                    (name, phone, id))
        conn.commit()
        print(f'{cur.rowcount} row(s) updated.')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def update_entry():
    read_entry()
    id = int(input('Enter the ID to update: '))
    name = input('Enter the NEW name: ')
    phone = input('Enter the NEW phone number: ')
    update_entry_row(id, name, phone)


def delete_entry_row(id):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Entries
                        WHERE PersonID = ?''',
                    (id,))
        conn.commit()
        print(f'{cur.rowcount} row(s) deleted.')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def delete_entry():
    read_entry()
    id = int(input('Enter the ID to delete: '))
    sure = input('Are you sure you want to delete this item? (y/n): ')
    if sure.lower() == 'y':
        delete_entry_row(id)


def main():
    choice = 0
    while choice != QUIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create_entry()
        elif choice == READ:
            read_entry()
        elif choice == UPDATE:
            update_entry()
        elif choice == DELETE:
            delete_entry()


if __name__ == '__main__':
    main()
