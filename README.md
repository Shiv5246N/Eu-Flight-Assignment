EU Flight Project

Project Overview

This project aims to develop a comprehensive database of all European airports and track detailed flight information. The primary objective is to monitor flights and identify delays exceeding two hours to assist passengers in filing refund claims. Future enhancements will include an API to provide daily flight data across Europe.

Features

Database schema for storing airport and flight data

Real-time flight monitoring

Delay detection and claim identification

API design for future scalability

Data collection from multiple sources

Installation

Prerequisites

Python 3.x

MySQL or PostgreSQL database

Required Python libraries:

pip install requests pandas sqlalchemy

Database Schema

The database consists of the following tables:

Airports: Stores information about European airports (IATA, ICAO, country, etc.).

Flights: Stores flight details, including departure, arrival, and status.

Airlines: Maintains airline information.

FlightStatus: Logs delays and updates flight status in real-time.

Data Collection Strategy

Use third-party APIs (e.g., FlightAware, AviationStack) to fetch real-time flight data.

Scrape airport details using web sources or open datasets.

Handle missing or inconsistent data through validation and error handling.

Usage

Setting Up the Database

Create the required database and tables using the provided SQL script.

Insert mock data for testing using predefined queries.

Querying Data

Retrieve flights from a specific airport:

SELECT * FROM Flights WHERE departure_airport = 'XYZ';

Identify flights delayed by more than 2 hours:

SELECT * FROM FlightStatus WHERE delay_time > 120;

Fetch flight details by flight number:

SELECT * FROM Flights WHERE flight_number = 'AB123';

API Simulation

A sample script to simulate API calls for real-time flight data collection is included. Modify API credentials before use.

Future Enhancements

Implement a scalable API for flight data retrieval.

Ensure API security, availability, and performance.

Automate data ingestion and updates.
