DROP database DenverPassbook;

CREATE Database IF NOT EXISTS DenverPassbook;
Use DenverPassbook;

CREATE TABLE IF NOT EXISTS Businesses (
    id int NOT NULL AUTO_INCREMENT ,
    name varchar(500),
    description varchar(1000),
    price_level int,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS Locations (
    id int NOT NULL AUTO_INCREMENT ,
    bus_id int NOT NULL,
    lat float,
    lon float,
    address varchar(1000),
    loc_city varchar(100),
    loc_state varchar(100),
    neighborhood varchar(100),
    phone varchar(20),
    google_rating varchar(3),
    active bit,
    website varchar(1000),
    perm_closed bit,
    primary key(id)
);

CREATE TABLE IF NOT EXISTS Hours (
    id int NOT NULL AUTO_INCREMENT ,
    location_id int NOT NULL,
    weekday varchar(50),
    open_time varchar(4),
    close_time varchar(4),
    primary key(id)
);

CREATE TABLE IF NOT EXISTS Coupons (
    id int NOT NULL AUTO_INCREMENT ,
    bus_id int NOT NULL,
    description varchar(500),
    restrictions varchar(500),
    coup_type varchar(100),
    primary key(id)
);
