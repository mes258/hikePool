drop table if exists cars;
	create table cars (
		id integer primary key autoincrement,
		date date not null,
		destination text not null,
		driverName text not null,
		driverPhone text not null,
		driverLocation text not null,
		numberOfPassengers int not null,
		passengerOneName text, 
		passengerTwoName text,
		passengerThreeName text, 
		passengerFourName text, 
		passengerFiveName text, 
		passengerSixName text,
        passengerOnePhone text,
        passengerTwoPhone text,
        passengerThreePhone text,
        passengerFourPhone text,
        passengerFivePhone text,
        passengerSixPhone text,
        time time
);
		
