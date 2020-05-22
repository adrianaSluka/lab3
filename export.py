import cx_Oracle
import csv
username = 'system'
password = '1q2w3e4r5t'
database = 'localhost:1522/orcl'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

query="""SELECT comment_id, comment_text, duration_sec, datetime, shape, event_id, latitude, longitude, location_city_name, country_name
FROM comment3 
JOIN event3
ON event_event_id=event_id
JOIN place3
ON place_latitude=latitude AND place_longitude=longitude"""
cursor.execute(query)
with open("ufo.csv", "w", newline="\n") as ufo_records:
    writer = csv.writer(ufo_records, delimiter=',')
    writer.writerow(
        'comment id, comment text, duration(sec), datetime, shape, event id, latitude, longitude, city name, country name'.split(","))
    for (comment_id, comment_text,
         duration_sec, datetime,
         shape, event_id, latitude,
         longitude, location_city_name,
         country_name) in cursor:
        writer.writerow(
        [comment_id, comment_text, duration_sec,
         datetime, shape, event_id, latitude,
         longitude, location_city_name, country_name])

cursor.close()
connection.close()
ufo_records.close()
