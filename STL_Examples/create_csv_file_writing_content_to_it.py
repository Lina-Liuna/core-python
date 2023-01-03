import csv

header = ['name', 'age', 'title', 'department', 'paygrade']
data = [['Betty', '58', 'CEO', 'IT', '20'],
        ['Morgan', '68', 'CTO', 'IT', '19']
        ]

def create_and_write(csv_name, h, datas):
    with open(csv_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(h)
        for d in datas:
            writer.writerow(d)

create_and_write('employees.csv', header, data)
