import sqlite3
import pandas as pd

conn = sqlite3.connect("lockdown1.db")
c = conn.cursor()

data = pd.read_sql("SELECT tweet_id FROM GEO", conn)