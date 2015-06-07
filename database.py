import sqlite3 as lite
import pandas as pd

cities = (('Las Vegas', 'NV'),('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 80),
                     ('Atlanta', 2013, 'July', 'January', 72))

con = lite.connect('L3.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS cities")
cur.execute("DROP TABLE IF EXISTS weather")
cur.execute("CREATE table cities (name text, state text)")
cur.execute("CREATE table weather(city text, year integer, warm_month text, cold_month text, average_high integer)")


df = pd.read_csv('cities.csv')
df.to_sql('cities', con, if_exists='append', index=False)

df = pd.read_csv('weather.csv')
df.to_sql('weather', con, if_exists='append', index=False)

cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)	
cur.execute("SELECT name, state, year FROM cities INNER JOIN weather ON name = city WHERE warm_month='July';")

result=cur.fetchall()

df=pd.DataFrame(result)

print ("The cities where July is the warmest month of the year are ") + df.to_string(columns=[0,1],index=False, header=False,)



#print df.values
#print df[[0,1]]

# makeTxt= df.iat[0,0]
# txt=str(makeTxt)
# print ("Some text" + txt)
# print df.iat[0,1]
#print df[[0,1]]
# print ("The cities where July is the warmest month of the year are ") 
# warmJuly=df.iat[0,0]
# warmJuly=str(warmJuly)
# print warmJuly

# with open('cities.csv', 'rb') as added:
# 	ds1=csv.reader(added)
# 	to_db = [(i['name'], i['state']) for i in ds1]

# cur.executemany("INSERT INTO cities (name, state) VALUES (?, ?);", to_db)
# con.commit()