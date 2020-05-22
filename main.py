import chart_studio
import plotly.graph_objects as go
chart_studio.tools.set_credentials_file(username='asluka', api_key='IcXrgX66CiHeMKQxmvqI')
import chart_studio.plotly as py
import cx_Oracle

username = 'system'
password = '1q2w3e4r5t'
database = 'localhost:1522/orcl'

connection = cx_Oracle.connect(username, password, database)

query1 = """SELECT shape, MAX(duration_sec/60.0)AS max_dur_min
FROM TablesJoined
GROUP BY shape
ORDER BY max_dur_min DESC"""

cursor = connection.cursor()
cursor.execute(query1)
attributes = cursor.description

x = " "

print("First query: shape of contact and the maximum time it was visible (in minutes)")
print(attributes[0][0], x * 20, attributes[1][0])
x1=[]
y1=[]
for rec in cursor.fetchall():
    print(rec[0], rec[1])
    x1.append(rec[0])
    y1.append(rec[1])
fig = go.Figure([go.Bar(x=x1, y=y1)])
py.plot(fig, auto_open=True, filename='graph1')



query2 = """SELECT country_name, COUNT(event_id), (COUNT(event_id)*100/(SELECT COUNT(*) FROM TablesJoined))
FROM TablesJoined
WHERE country_name!='undefined'
GROUP BY country_name"""
cursor.execute(query2)
print("\nSecond Query: countries and UFO events that happened there (as percentage from whole)")
print('country', x * 10, 'percentage')
x2=[]
y2=[]
for rec1 in cursor.fetchall():
    print(rec1[0], rec1[1], rec1[2], '%')
    x2.append(rec1[0])
    y2.append(rec1[1])
colors = ['gold', 'mediumturquoise', 'lightgreen']
fig2 = go.Figure(data=[go.Pie(labels=x2,
                             values=y2)])
fig2.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)))
py.plot(fig2, auto_open=True, filename='graph2')



query3="""SELECT longitude, COUNT(*) AS counting
FROM TablesJoined
WHERE longitude != 0
GROUP BY longitude
ORDER BY counting DESC
"""
cursor.execute(query3)
longitude=[]
counting=[]
print("\nThird Query: dependency between longitude and concentration events")
print("longitude", x * 5, "events")
for rec in cursor.fetchall():
    print(rec[0], x * 5, rec[1])
    longitude.append(rec[0])
    counting.append(rec[1])

fig3= go.Figure(data=go.Scatter(x=longitude, y=counting, mode='markers'))
fig3.update_layout(xaxis_title='WEST       longitude       EAST',)
py.plot(fig3, auto_open=True, filename='graph3')



query4 = """SELECT latitude, longitude, city_name
FROM TablesJoined
WHERE longitude != 0 AND country_name!='us' AND country_name!='undefined' 
"""
cursor.execute(query4)
print("\nThird Query: dependency between longitude and concentration events")
print("longitude", x * 5, "events")
lat=[]
lon=[]
text=[]
print("longitude", x * 5, "events", x*5, "city_name")
for rec in cursor.fetchall():
    print(rec[0], x * 5, rec[1], x*5, rec[2])
    lat.append(rec[0])
    lon.append(rec[1])
    text.append(rec[2])

fig = go.Figure(data=go.Scattergeo(
        lon = lon,
        lat = lat,
        mode = 'markers',
        text = text,
        ))
fig.update_layout(
        title = 'UFO reports from different countries (except USA)',
        geo_scope='world',
    )
py.plot(fig, auto_open=True, filename='graph4')


cursor.close()
connection.close()
