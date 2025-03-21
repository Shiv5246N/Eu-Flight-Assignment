CREATE TABLE Airports (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    iata_code VARCHAR(3) UNIQUE,
    icao_code VARCHAR(4) UNIQUE,
    country VARCHAR(100),
    city VARCHAR(100),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

CREATE TABLE Flights (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR(10) UNIQUE,
    origin VARCHAR(3),
    destination VARCHAR(3),
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    status VARCHAR(20)
);
