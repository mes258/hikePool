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
        passengerOnePhone text,
        passengerOneLocation text,
		passengerTwoName text,
        passengerTwoPhone text,
        passengerTwoLocation text,
		passengerThreeName text, 
        passengerThreePhone text,
        passengerThreeLocation text,
		passengerFourName text, 
        passengerFourPhone text,
        passengerFourLocation text,
		passengerFiveName text, 
        passengerFivePhone text,
        passengerFiveLocation text,
		passengerSixName text,
        passengerSixPhone text,
        passengerSixLocation text
);
		
