drop table if exists cars;
drop table if exists rides;
	create table rides (
		id integer primary key autoincrement,
		date date not null,
        time time,
        destination text not null,
        pickUpSpot text not null,
        driverId references people(id),
        numberOfPassengers int default 6,
        spotsOpen int default 6,
        secretCode text
);
drop table if exists people;
    create table people (
        id integer primary key autoincrement,
        name text not null,
        phone text not null
);
drop table if exists passengers;
    create table passengers (
        id integer primary key autoincrement, 
        rideId references rides(id),
        passengerId references people(id)
);