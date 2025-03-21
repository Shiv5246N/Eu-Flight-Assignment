import psycopg2
import requests

# ✅ Step 1: PostgreSQL Database Connection
conn = psycopg2.connect(
    dbname="flightdatabase",  # Apna database name
    user="postgres",          # PostgreSQL username
    password="1234",          # Apna password
    host="localhost",         # Local machine pe run ho raha hai
    port="5432"               # PostgreSQL default port
)
cursor = conn.cursor()

# ✅ Step 2: Fetch Real-time Flight Data from OpenSky API
url = "https://opensky-network.org/api/states/all"
response = requests.get(url)
data = response.json()

# ✅ Step 3: Insert/Update Data into PostgreSQL
if 'states' in data:
    for flight in data['states']:
        icao24 = flight[0] or "UNKNOWN"  # Unique aircraft ID
        callsign = flight[1] or "UNKNOWN"
        origin_country = flight[2] or "UNKNOWN"
        longitude = flight[5] or None
        latitude = flight[6] or None
        baro_altitude = flight[7] or None
        velocity = flight[9] or None

        cursor.execute("""
            INSERT INTO Flights (icao24, callsign, origin_country, longitude, latitude, baro_altitude, velocity)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (icao24) DO UPDATE 
            SET callsign = EXCLUDED.callsign,
                origin_country = EXCLUDED.origin_country,
                longitude = EXCLUDED.longitude,
                latitude = EXCLUDED.latitude,
                baro_altitude = EXCLUDED.baro_altitude,
                velocity = EXCLUDED.velocity;
        """, (icao24, callsign, origin_country, longitude, latitude, baro_altitude, velocity))

# ✅ Step 4: Save & Close Connection
conn.commit()
cursor.close()
conn.close()
print("✅ Data Inserted Successfully!")
