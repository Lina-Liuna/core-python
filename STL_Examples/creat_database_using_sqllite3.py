import sqlite3

header = ['name', 'age', 'title', 'department', 'paygrade']
data = [['Betty', '58', 'CEO', 'IT', '20'],
        ['Morgan', '68', 'CTO', 'IT', '19']
        ]



def create_db_sqllite3():
        conn = sqlite3.connect('companydata')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS employees
                     ([name] TEXT PRIMARY KEY, [age] TEXT, [title] TEXT,[department] TEXT,[paygrade] TEXT)

        ''')
        c.execute('''INSERT INTO employees (name, age, title, department, paygrade)
                        VALUES
                        ('Betty', '58', 'CEO', 'IT', '20')

        ''')
        conn.commit()

