import sqlite3

POP_SORT_ASC = 1  # Display a list of cities sorted by population, in ascending order.
POP_SORT_DESC = 2  # Display a list of cities sorted by population, in descending order.
CITY_SORT_NAME = 3  # Display a list of cities sorted by name.
TOTAL_POP = 4  # Display the total population of all the cities.
AVERAGE_POP = 5  # Display the average population of all the cities.
HIGHEST_POP = 6  # Display the city with the highest population.
LOWEST_POP = 7  # Display the city with the lowest population.
QUIT = 8  # Quit App


def display_menu():
    print('\n------Cities Population Database------')
    print('1: Display a list of cities sorted by population, in ascending order.')
    print('2: Display a list of cities sorted by population, in descending order.')
    print('3: Display a list of cities sorted by name.')
    print('4: Display the total population of all the cities.')
    print('5: Display the average population of all the cities.')
    print('6: Display the city with the highest population.')
    print('7: Display the city with the lowest population.')
    print('8: Quit App.')


def get_menu_choice():
    choice = int(input('What do you want to query? Enter your selection: '))

    while choice < POP_SORT_ASC or choice > QUIT:
        print(f'Invalid selection. Please select number from {POP_SORT_ASC} to {QUIT} only.')
        choice = int(input('What do you want to query? Enter your selection: '))

    return choice


def population_sort_ascending():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('''SELECT CityName, Population
                        FROM Cities
                        ORDER BY Population''')
        results = cur.fetchall()

        print('The cities sorted by population in ascending order:')
        print('----------------------------------------------------')
        for row in results:
            print(f'{row[0]:<3}: {int(row[1]):,d}')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def population_sort_descending():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('''SELECT CityName, Population
                            FROM Cities
                            ORDER BY Population DESC''')
        results = cur.fetchall()

        print('The cities sorted by population in descending order:')
        print('----------------------------------------------------')
        for row in results:
            print(f'{row[0]:<3}: {int(row[1]):,d}')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def cities_sort_name():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('''SELECT CityName, Population
                                FROM Cities
                                ORDER BY CityName''')
        results = cur.fetchall()

        print('The cities sorted by name:')
        print('---------------------------')
        for row in results:
            print(f'{row[0]:<3}: {int(row[1]):,d}')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def total_population():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('''SELECT sum(Population)
                                    FROM Cities''')
        results = cur.fetchone()[0]

        print(f'The total population of all cities: {int(results):,d}')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def average_population():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('''SELECT avg(Population)
                                        FROM Cities''')
        results = cur.fetchone()[0]

        print(f'The average population of all cities: {int(results):,d}')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def highest_population():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('''SELECT CityName, max(Population)
                                            FROM Cities''')
        results = cur.fetchall()

        print('The highest population of all cities:')
        for row in results:
            print(f'{row[0]:<3}: {int(row[1]):,d}')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def lowest_population():
    conn = None
    results = []
    try:
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        cur.execute('''SELECT CityName, min(Population)
                                                    FROM Cities''')
        results = cur.fetchall()

        print('The lowest population of all cities:')
        for row in results:
            print(f'{row[0]:<3}: {int(row[1]):,d}')

    except sqlite3.Error as err:
        print(f'Database Error: {err}')
    finally:
        if conn is not None:
            conn.close()


def main():
    choice = 0
    while choice != QUIT:
        display_menu()
        choice = get_menu_choice()

        if choice == POP_SORT_ASC:
            population_sort_ascending()
        elif choice == POP_SORT_DESC:
            population_sort_descending()
        elif choice == CITY_SORT_NAME:
            cities_sort_name()
        elif choice == TOTAL_POP:
            total_population()
        elif choice == AVERAGE_POP:
            average_population()
        elif choice == HIGHEST_POP:
            highest_population()
        elif choice == LOWEST_POP:
            lowest_population()


if __name__ == '__main__':
    main()
