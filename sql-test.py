import time
import sqlite3
from world_time import WorldTime
from season_temp import get_season
from season_temp import get_temperature
from season_temp import get_weather

# Create a connection to the SQLite database
conn = sqlite3.connect('event_log2.db')
c = conn.cursor()

# Create a table to store the time and weather
c.execute('''CREATE TABLE IF NOT EXISTS environmental_stats
             (id INTEGER PRIMARY KEY, 
             year INTEGER,
             day INTEGER,
             time TEXT,
             weather INTEGER,
             temperature REAL,
             season INTEGER)''')

# Create a new WorldTime object and set the start time
current_time = WorldTime()

# Loop forever, updating the time and weather in the database every second
while True:
    # random weather condition and temperature as of now

    weather = get_weather(current_time)
    season = get_season(current_time)
    temperature = get_temperature(current_time)

    # Format the time as a string and insert it into the database
    time_str = f"{current_time.hours:02d}:{current_time.minutes:02d}:{current_time.seconds:02d}"
    c.execute('''INSERT INTO environmental_stats (year, day, time, weather, temperature, season)
                 VALUES (?, ?, ?, ?, ?, ?)''', (current_time.year, current_time.days, time_str, weather, temperature, season))
    conn.commit()

    # Time modifiers
    time_mod = 20

    # Update the time, this is a really dumb way??
    current_time.seconds += 1 * time_mod

    if current_time.seconds == 60:
        current_time.seconds = 0
        current_time.minutes += 1

    if current_time.minutes == 60:
        current_time.minutes = 0
        current_time.hours += 1

    if current_time.hours == 24:
        current_time.hours = 0
        current_time.days += 1 * time_mod

        # Increment year if 80 days have elapsed
        if current_time.days >= current_time.DAYS_PER_YEAR:
            current_time.year += current_time.days // current_time.DAYS_PER_YEAR
            current_time.days = current_time.days % current_time.DAYS_PER_YEAR

    print(f'{season=}, {weather=}, {temperature=}')
    print(current_time)
    
    #time.sleep(1)