import csv
import cx_Oracle
username = 'system'
password = '1q2w3e4r5t'
database = 'localhost:1522/orcl'
connection = cx_Oracle.connect(username, password, database)

file=open('complete.csv', 'r')
str=list(csv.reader(file, delimiter=','))

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

strings_new=[]
for row in str:
    date=[row[0], row[1], row[3], row[4], row[5], row[7], row[9], row[10]]
    strings_new.append(date)

cursor = connection.cursor()
query1="""INSERT  /*+ IGNORE_ROW_ON_DUPKEY_INDEX(country3(country_name)) */  INTO country3 (country_name)
VALUES (:country_name)"""

query2="""INSERT /*+ IGNORE_ROW_ON_DUPKEY_INDEX(location3(city_name, country_country_name)) */  INTO location3 (city_name, country_country_name)
VALUES (:city_name , :country_name)"""

cursor.execute("""BEGIN dbms_errlog.create_error_log( 'place3' ); END;""")
query3="""
INSERT INTO place3 (latitude, longitude, location_city_name, country_name)
VALUES (:latitude , :longitude , :city_name , :country_name)
LOG ERRORS REJECT LIMIT 50"""
cursor.execute("""BEGIN dbms_errlog.create_error_log( 'event3' ); END;""")
query4="""INSERT INTO event3 (event_id, place_longitude, place_latitude) VALUES (:id, :longitude, :latitude)
LOG ERRORS REJECT LIMIT 50"""
cursor.execute("""BEGIN dbms_errlog.create_error_log( 'comment3' ); END;""")
query5="""INSERT INTO comment3 (comment_id, comment_text, duration_sec, datetime, shape, event_event_id)
       VALUES (:id1,  :comment_text, :duration_sec, TO_TIMESTAMP(:datetime, 'MM/DD/YYYY HH24:MI'), :shape, :id2)
       LOG ERRORS REJECT LIMIT 50"""
connection.commit()
for i in range(1, len(strings_new)):
    cursor.execute(query1, country_name='undefined')
    country_name = strings_new[i][2]
    city_name = strings_new[i][1]
    duration_sec=strings_new[i][4]
    datetime=strings_new[i][0]
    shape=strings_new[i][3]
    id=i
    comment_text=strings_new[i][5]
    if (isfloat(strings_new[i][6]) & isfloat(strings_new[i][7])):
        latitude=round(float(strings_new[i][6]), 3)
        longitude=round(float(strings_new[i][7]), 3)
        if (country_name==''):
            cursor.execute(query1, country_name='undefined')
        else:
            cursor.execute(query1, country_name=country_name)
        connection.commit()
        if (city_name==''):
            pass
        else:
            if (country_name==''):
                cursor.execute(query2, city_name=city_name, country_name='undefined')
            else:
                cursor.execute(query2, city_name=city_name, country_name=country_name)
            connection.commit()
        if (city_name == ''):
            cursor.execute(query3, latitude=latitude, longitude=longitude, city_name='undefined',
                           country_name=country_name)
            connection.commit()
        elif (country_name == ''):
            cursor.execute(query3, latitude=latitude, longitude=longitude, city_name=city_name,
                           country_name='undefined')
            connection.commit()
        else:
            cursor.execute(query3, latitude=latitude, longitude=longitude, city_name=city_name,
                           country_name=country_name)
            connection.commit()
        cursor.execute(query4, id=id, longitude=longitude, latitude=latitude)
        cursor.execute(query5, id1=id, comment_text=comment_text, duration_sec=duration_sec, datetime=datetime, shape=shape, id2=id)

print(1)
cursor.close()
connection.close()
file.close()
