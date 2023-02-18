import sqlite3


def main():
    conn = sqlite3.connect('student_info.db')
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS Majors''')
    cur.execute('''DROP TABLE IF EXISTS Departments''')
    cur.execute('''DROP TABLE IF EXISTS Students''')

    cur.execute('''CREATE TABLE Majors (MajorID INTEGER PRIMARY KEY NOT NULL,
                                        MajorName TEXT NOT NULL)''')
    cur.execute('''CREATE TABLE Departments (DeptID INTEGER PRIMARY KEY NOT NULL,
                                            DeptName TEXT NOT NULL)''')
    cur.execute('''CREATE TABLE Students (StudentID INTEGER PRIMARY KEY NOT NULL,
                                            StudentName TEXT NOT NULL,
                                            MajorID INTEGER,
                                            DeptID INTEGER,
                                            FOREIGN KEY (MajorID) REFERENCES Majors (MajorID),
                                            FOREIGN KEY (DeptID) REFERENCES Departments (DeptID))''')

    conn.commit()
    conn.close()


# enable foreign key enforcement --> cur.execute('PRAGMA foreign_keys=ON')
# for create, update and delete
# existing MajorID and DeptID should be selected when creating new student

if __name__ == '__main__':
    main()
