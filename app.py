from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from passlib.hash import sha256_crypt
from models import createRide, getRides, deleteRide, joinRide, getRide, editRide, createPerson, getPeople, getPerson, getPassengers, getRequests, driveRide, getDriver
app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        newId = createPerson(name, phone)

        date = request.form.get('date')
        time = request.form.get('time')
        destination = request.form.get('destination')
        pickUpSpot = request.form.get('pickUpSpot')
        passengerNum = request.form.get('passengerNum')
        sc = request.form.get('secretCode')
        secretCode = sha256_crypt.encrypt(sc)
        print(secretCode)
        createRide(date, time, destination, pickUpSpot, newId, passengerNum, passengerNum, secretCode)

    rides = getRides()
    ridesWithDrivers = []
    for ride in rides:
        ridesWithDrivers.append((ride, getDriver(ride[5])))
    requests = getRequests()

    return render_template('index.html', rides=ridesWithDrivers, requests=requests)

@app.route('/getRide/<rideId>', methods=['POST'])
def get_Ride(rideId):
    ride = getRide(rideId)
    driver = []
    if(ride[5] != None):
        driver = getDriver(ride[5])
    fullRide = [].append((ride, driver))

    return json.dumps([dumpRide(r) for r in fullRide])

@app.route('/getRides', methods=['POST'])
def get_Rides():
    rides = getRides()
    ridesWithDrivers = []
    for ride in rides:
        ridesWithDrivers.append((ride, getDriver(ride[5])))
    return json.dumps([dumpRide(r) for r in ridesWithDrivers])


@app.route('/getRequests', methods=['POST'])
def get_Requests():
    requests = getRequests()
    return json.dumps([dumpRide(r) for r in requests])

@app.route('/createRequest', methods=['POST'])
def create_request():
    date = request.form.get('date')
    time = request.form.get('time')
    destination = request.form.get('destination')
    pickUpSpot = request.form.get('pickUpSpot')
    rideId = createRide(date, time, destination, pickUpSpot, -1, 0, 0, None)

    rides = getRides()
    drivers = getPeople()
    reqests = getRequests()
    return redirect('/')

@app.route('/driveRide/<rideId>', methods=['POST'])
def drive_ride(rideId):
    ride = getRide(rideId)
    return render_template('driveRide.html', ride=ride)

@app.route('/driveRide/<rideId>/submit', methods=['POST'])
def drive_ride_submit(rideId):
    name = request.form.get('name')
    phone = request.form.get('phone')
    passengerNum = request.form.get('passengerNum')
    sc = request.form.get('secretCode')
    secretCode = sha256_crypt.encrypt(sc)

    driverId = createPerson(name, phone)
    driveRide(rideId, driverId, passengerNum, secretCode)

    rides = getRides()
    return redirect('/')

@app.route('/join/<rideId>', methods=['POST'])
def join_ride(rideId):
    ride = getRide(rideId)
    return render_template('join.html', ride=ride)

@app.route('/join/<rideId>/submit', methods=['POST'])
def join_ride_submit(rideId):
    name = request.form.get('name')
    phone = request.form.get('phone')
    passengerId = createPerson(name, phone)
    joinRide(rideId, passengerId)

    rides = getRides()
    return redirect('/')

@app.route('/addRide', methods=['POST'])
def addRide():
    name = request.form.get('name')
    phone = request.form.get('phone')
    newId = createPerson(name, phone)

    date = request.form.get('date')
    time = request.form.get('time')
    destination = request.form.get('destination')
    pickUpSpot = request.form.get('pickUpSpot')
    passengerNum = request.form.get('passengerNum')
    sc = request.form.get('secretCode')
    secretCode = sha256_crypt.encrypt(sc)
    print(secretCode)
    createRide(date, time, destination, pickUpSpot, newId, passengerNum, passengerNum, secretCode)
    return redirect('/drivers')

@app.route('/details/<rideId>', methods=['POST'])
def ride_details(rideId):
    ride = getRide(rideId)
    passengerLimit = ride[0][6]
    driver = getPerson(ride[0][5])
    passengers = getPassengers(rideId, passengerLimit)

    return render_template('details.html', ride=ride, driver=driver, passengers=passengers)

@app.route('/edit/<rideId>', methods=['POST'])
def edit_ride(rideId):
    secretCode = request.form.get('sc')
    ride = getRide(rideId)
    if sha256_crypt.verify(secretCode, ride[0][8]):
        passengerLimit = ride[0][6]
        passengers = getPassengers(rideId, passengerLimit)
        return render_template('edit.html', ride=ride, passengers=passengers)
    else:
        rides = getRides()
        return redirect('/')

@app.route('/edit/<rideId>/submit', methods=['POST'])
def edit_ride_submit(rideId):
    date = request.form.get('date')
    time = request.form.get('time')
    destination = request.form.get('destination')
    pickUpSpot = request.form.get('pickUpSpot')
    removedPassengers = request.form.getlist('removedPassenger')
    removedPassengerIds = (passenger[0] for passenger in removedPassengers)
    removedPeopleIds = (passenger[1] for passenger in removedPassengers)
    editRide(rideId, date, time, destination, pickUpSpot, removedPassengerIds, removedPeopleIds)

    rides = getRides()
    return redirect('/')

@app.route('/delete/<rideId>', methods=['POST'])
def delete_ride(rideId):
    deleteRide(rideId)
    rides = getRides()
    return redirect('/')

@app.route('/viewRides', methods=['GET'])
def viewRides():
    rides = getRides()
    return render_template('viewRides.html', rides=rides)

@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/faq', methods=['GET'])
def faq():
    return render_template('faq.html')

@app.route('/drivers', methods=['GET', 'POST'])
def drivers():
    return render_template('drivers.html', requests=getRequests())

@app.route('/riders', methods=['GET', 'POST'])
def riders():
    rides=getRides()
    return render_template('riders.html', rides=rides)

@app.route('/nav/<tab>', methods=['GET', 'POST'])
def nav(tab):
    navItems = ['viewRides', 'drivers', 'riders', 'privacy', 'faq']
    navItemNames = ['View Rides', 'Drivers', 'Riders', 'Privacy', 'Faq']
    return render_template('nav.html', selected=tab, navItems=navItems, navItemNames=navItemNames)

def dumpRides(ride):
    return {"ride": {'date':ride[0][1],
                    'time':ride[0][2],
                    'destination':ride[0][3],
                    'pickUpSpot':ride[0][4],
                    'numberOfPassengers': ride[0][6],
                    'spotsOpen':ride[0][7],
                    },
            "driver": {'name':ride[1][0],
                       'phone':ride[1][1]
                    }
            } if ride[0][5] != None else {"ride": {'date':ride[0][1],
                    'time':ride[0][2],
                    'destination':ride[0][3],
                    'pickUpSpot':ride[0][4],
                    'numberOfPassengers': ride[0][6],
                    'spotsOpen':ride[0][7],
                    },
            "driver": {'name':'N/A',
                       'phone':'N/A'
                    }
            }

if __name__ == '__main__':
    app.run(debug=True)
