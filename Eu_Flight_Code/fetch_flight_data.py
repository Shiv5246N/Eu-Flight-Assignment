import psycopg2
import requests

# ✅ Step 1: Database Connection
try:
    conn = psycopg2.connect(
        dbname="flightdatabase",
        user="postgres",
        password="1234",  # 🔹 Change this to your actual password
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # ✅ Ensure correct schema is set
    cursor.execute("SET search_path TO public;")  # 🔹 Fixed search_path
    print("✅ Connected to Database Successfully!")

    # ✅ Step 2: Check if the 'flights' table exists
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'flights'
        );
    """)
    table_exists = cursor.fetchone()[0]

    if not table_exists:
        print("❌ Error: Table 'flights' does not exist! Please create it first.")
        exit()

except Exception as e:
    print("❌ Database Connection Error:", e)
    exit()

# ✅ Step 3: Fetch Real-time Flight Data
API_URL = "https://opensky-network.org/api/states/all"

try:
    response = requests.get(API_URL, timeout=10)  # ✅ Timeout added
    response.raise_for_status()  # ✅ Prevents inserting bad API data
    data = response.json()

    if 'states' in data and isinstance(data['states'], list):
        print(f"✅ Received {len(data['states'])} flight records. Processing...")

        for flight in data['states'][:10]:  # ✅ Limiting to 10 for testing
            try:
                icao24 = flight[0] if flight[0] else "Unknown"
                callsign = flight[1].strip() if flight[1] else "Unknown"
                origin_country = flight[2] if flight[2] else "Unknown"
                longitude = flight[5] if flight[5] is not None else 0.0
                latitude = flight[6] if flight[6] is not None else 0.0
                baro_altitude = flight[7] if flight[7] is not None else 0.0
                velocity = flight[9] if flight[9] is not None else 0.0

                cursor.execute("""
                    INSERT INTO flights (icao24, callsign, origin_country, longitude, latitude, baro_altitude, velocity)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (icao24) DO UPDATE SET 
                    callsign = EXCLUDED.callsign, 
                    origin_country = EXCLUDED.origin_country, 
                    longitude = EXCLUDED.longitude, 
                    latitude = EXCLUDED.latitude, 
                    baro_altitude = EXCLUDED.baro_altitude, 
                    velocity = EXCLUDED.velocity;
                """, (icao24, callsign, origin_country, longitude, latitude, baro_altitude, velocity))

                print(f"✅ Inserted: {icao24} - {callsign}")

            except Exception as e:
                print(f"❌ Error inserting flight {icao24}: {e}")

    else:
        print("❌ API response does not contain expected 'states' data.")

except requests.exceptions.RequestException as api_error:
    print(f"❌ Failed to fetch data from API: {api_error}")
    exit()

# ✅ Step 4: Close Database Connection
cursor.close()
conn.close()
print("✅ Database Connection Closed.")
