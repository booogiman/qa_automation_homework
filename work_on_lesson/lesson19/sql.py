import sqlite3

connect = sqlite3.connect('passengers.sql')

cursor = connect.cursor()
with open('passqers.sql','r') as file:
    cursor.execute(file.read())

data = ('Иван', 'Тестовый', '9031456783', '12557')
ins_str = f"INSERT INTO 'passenger_info' (name, surname,phone, flight_num) VALUES {data}"
