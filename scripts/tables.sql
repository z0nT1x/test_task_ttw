use wwt_test_db;
CREATE TABLE users (
    user_id INT unsigned auto_increment PRIMARY KEY,                   
    email VARCHAR(150) UNIQUE NOT NULL,      
    registration_date DATE NOT NULL,         
    country VARCHAR(50),                     
    device_type VARCHAR(20),                   
    referral_source VARCHAR(50)            
);

create table requests(
	request_id int unsigned auto_increment primary key,
	user_id int unsigned,
	people_amount integer,
	animals_amount integer,
	kids integer,
	highest_price integer,
	request_date timestamp,
	is_ai_used boolean,
	CONSTRAINT fk_requests_user 
        FOREIGN KEY (user_id) 
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

create table hotel(
hotel_id int unsigned auto_increment primary key,
country varchar(50),
city varchar(50),
street varchar(50),
house integer,
email varchar(50),
phone_number varchar(20),
rating decimal(2, 1)
);

create table room(
room_id int unsigned auto_increment primary key,
hotel_id int unsigned,
beds integer,
animals_places integer,
price_day decimal(5,2),
is_extra_beds boolean,
size decimal(5,2),
constraint fk_hotel_room
foreign key (hotel_id)
references hotel(hotel_id)
on delete cascade
);

create  table activities(
activity_id int unsigned auto_increment primary key,
request_id int unsigned,
room_id int unsigned,
is_liked boolean,
constraint fk_request_activity
foreign key (request_id)
references requests(request_id)
on delete cascade,
constraint fk_room_activity
foreign key (room_id)
references room(room_id)
on delete cascade
);

create table orders(
order_id int unsigned auto_increment primary key,
request_id int unsigned,
room_id int unsigned,
total_price decimal(8,2),
order_date timestamp,
constraint fk_request_order
foreign key (request_id)
references requests(request_id)
on delete cascade,
constraint fk_room_order
foreign key (room_id)
references room(room_id)
on delete cascade
);

