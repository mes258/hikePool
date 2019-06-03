import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_car(date, destination, name, phone, location, passengerNum):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into cars (date, destination, driverName, driverPhone, driverLocation, numberOfPassengers) values(?,?,?,?,?,?)', (date, destination, name, phone, location, passengerNum))
    con.commit()
    con.close()
    #BLOCK SPOTS IF THE USER HAS < 6 SPOTS BY ADDING FAKE USERS WITH NAME: N/A OR SOMETHING

def get_cars():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from cars')
    cars = cur.fetchall()
    return cars

def joinCar(carId, name):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    car = getCar(carId)
    print(car[0][7])
    if car[0][7] == None:
        cur.execute('update cars set passengerOne = ? where id = ?', [name, carId])
    elif car[0][8] == None:
        cur.execute('update cars set passengerTwo = ? where id = ?', [name, carId])
    elif car[0][9] == None:
        cur.execute('update cars set passengerThree = ? where id = ?', [name, carId])
    elif car[0][10] == None:
        cur.execute('update cars set passengerFour = ? where id = ?', [name, carId])
    elif car[0][11] == None:
        cur.execute('update cars set passengerFive = ? where id = ?', [name, carId])
    elif car[0][12] == None:
        cur.execute('update cars set passengerSix = ? where id = ?', [name, carId])
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


