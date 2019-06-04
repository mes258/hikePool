import sqlite3 as sql
from datetime import datetime, time, timedelta
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_car(date, time, destination, name, phone, location, passengerNum):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    print(passengerNum)
    if passengerNum == '0':
        cur.execute('insert into cars (date, time, destination, driverName, driverPhone, driverLocation, numberOfPassengers, passengerOneName, passengerTwoName, passengerThreeName, passengerFourName, passengerFiveName, passengerSixName, passengerOnePhone, passengerTwoPhone, passengerThreePhone, passengerFourPhone, passengerFivePhone, passengerSixPhone) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (date, time, destination, name, phone, location, passengerNum, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', ' ',' ',' ',' ',' ',' '))
    elif passengerNum == '1':
        cur.execute('insert into cars (date, time, destination, driverName, driverPhone, driverLocation, numberOfPassengers, passengerTwoName, passengerThreeName, passengerFourName, passengerFiveName, passengerSixName, passengerTwoPhone, passengerThreePhone, passengerFourPhone, passengerFivePhone, passengerSixPhone) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (date, time, destination, name, phone, location, passengerNum, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', '', '', '', '', ''))
    elif passengerNum == '2':
        cur.execute('insert into cars (date, time, destination, driverName, driverPhone, driverLocation, numberOfPassengers, passengerThreeName, passengerFourName, passengerFiveName, passengerSixName, passengerThreePhone, passengerFourPhone, passengerFivePhone, passengerSixPhone) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (date, time, destination, name, phone, location, passengerNum, 'N/A', 'N/A', 'N/A', 'N/A','','','',''))
    elif passengerNum == '3':
        cur.execute('insert into cars (date, time, destination, driverName, driverPhone, driverLocation, numberOfPassengers, passengerFourName, passengerFiveName, passengerSixName, passengerFourPhone, passengerFivePhone, passengerSixPhone) values(?,?,?,?,?,?,?,?,?,?,?,?,?)', (date, time, destination, name, phone, location, passengerNum, 'N/A', 'N/A', 'N/A','','',''))
    elif passengerNum == '4':
        cur.execute('insert into cars (date, time, destination, driverName, driverPhone, driverLocation, numberOfPassengers, passengerFiveName, passengerSixName, passengerFivePhone, passengerSixPhone) values(?,?,?,?,?,?,?,?,?,?,?)', (date, time, destination, name, phone, location, passengerNum, 'N/A', 'N/A','',''))
    elif passengerNum == '5':
        cur.execute('insert into cars (date, time, destination, driverName, driverPhone, driverLocation, numberOfPassengers, passengerSixName, passengerSixPhone) values(?,?,?,?,?,?,?,?,?)', (date, time, destination, name, phone, location, passengerNum, 'N/A',''))
    else:
        cur.execute('insert into cars (date, time, destination, driverName, driverPhone, driverLocation, numberOfPassengers) values(?,?,?,?,?,?,?)', (date, time, destination, name, phone, location, passengerNum))
    con.commit()
    con.close()

def get_cars():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from cars ORDER BY date, destination;')
    cars = cur.fetchall()
    firstTripDate = datetime.strptime(cars[0][1], "%Y-%m-%d")
    print(firstTripDate)
    if firstTripDate < datetime.now() - timedelta(days=1):
        deleteCar(cars[0][0])
    #updateTable()
    return cars

def joinCar(carId, name, phone):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    car = getCar(carId)
    print(car[0][7])
    if car[0][7] == None:
        cur.execute('update cars set passengerOneName = ? where id = ?', [name, carId])
        cur.execute('update cars set passengerOnePhone = ? where id = ?', [phone, carId])
    elif car[0][8] == None:
        cur.execute('update cars set passengerTwoName = ? where id = ?', [name, carId])
        cur.execute('update cars set passengerTwoPhone = ? where id = ?', [phone, carId])
    elif car[0][9] == None:
        cur.execute('update cars set passengerThreeName = ? where id = ?', [name, carId])
        cur.execute('update cars set passengerThreePhone = ? where id = ?', [phone, carId])
    elif car[0][10] == None:
        cur.execute('update cars set passengerFourName = ? where id = ?', [name, carId])
        cur.execute('update cars set passengerFourPhone = ? where id = ?', [phone, carId])
    elif car[0][11] == None:
        cur.execute('update cars set passengerFiveName = ? where id = ?', [name, carId])
        cur.execute('update cars set passengerFivePhone = ? where id = ?', [phone, carId])
    elif car[0][12] == None:
        cur.execute('update cars set passengerSixName = ? where id = ?', [name, carId])
        cur.execute('update cars set passengerSixPhone = ? where id = ?', [phone, carId])
    con.commit()
    con.close()

def getCar(carId):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from cars where id = ?', [carId])
    car = cur.fetchall()
    return car

def deleteCar(carId):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('delete from cars WHERE id = ?', [carId])
    con.commit()
    con.close()

def updateTable():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    # cur.execute('ALTER TABLE cars RENAME COLUMN passengerOne TO passengerOneName')
    # cur.execute('ALTER TABLE cars RENAME COLUMN passengerTwo TO passengerTwoName')
    # cur.execute('ALTER TABLE cars RENAME COLUMN passengerThree TO passengerThreeName')
    # cur.execute('ALTER TABLE cars RENAME COLUMN passengerFour TO passengerFourName')
    # cur.execute('ALTER TABLE cars RENAME COLUMN passengerFive TO passengerFiveName')
    # cur.execute('ALTER TABLE cars RENAME COLUMN passengerSix TO passengerSixName')
    con.commit()
    con.close()
    addPhone()

def addPhone():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    # cur.execute('alter table cars add column passengerOnePhone text;')
    # cur.execute('alter table cars add column passengerTwoPhone text;')
    # cur.execute('alter table cars add column passengerThreePhone text;')
    # cur.execute('alter table cars add column passengerFourPhone text;')
    # cur.execute('alter table cars add column passengerFivePhone text;')
    # cur.execute('alter table cars add column passengerSixPhone text;')
    #cur.execute('alter table cars add column time time;')
    con.commit()
    con.close()
