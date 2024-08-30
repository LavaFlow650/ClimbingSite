import csv
from datetime import datetime
from datetime import date
from routesetting.models import Route

def import_routes(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if Route.objects.filter(name=row['name']).exists():
                continue
            
            grade = row['grade']
            if grade[:2] == "5.":
                grade = grade[2:]
                num = 0
                for char in grade:
                    if char.isdigit():
                        num = num * 10 + int(char) * 10
                    if char == "+":
                        num += 1
                    elif char == "-":
                        num -= 1
                grade = num

            date = row['date']
            if date == 'summer':
                date = '08/19/24'

            Route.objects.create(
                grade_num=grade,
                location=row['location'],
                color=row['color'],
                name=row['name'],
                setter=row['setter'],
                date_set=datetime.strptime(date, '%m/%d/%y').date(),
                type=row['type'],
                date_logged = datetime.now(),
                archived = False
            )