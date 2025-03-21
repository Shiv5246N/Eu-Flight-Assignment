INSERT INTO Airports (name, iata_code, icao_code, country, city, latitude, longitude) 
VALUES 
('Frankfurt Airport', 'FRA', 'EDDF', 'Germany', 'Frankfurt', 50.0333, 8.5706),
('Munich Airport', 'MUC', 'EDDM', 'Germany', 'Munich', 48.3538, 11.7861);

INSERT INTO Flights (flight_number, origin, destination, departure_time, arrival_time, status)
VALUES 
('LH123', 'FRA', 'LHR', '2025-03-20 10:00:00', '2025-03-20 12:00:00', 'On Time'),
('LH456', 'MUC', 'CDG', '2025-03-20 14:00:00', '2025-03-20 16:30:00', 'Delayed');
