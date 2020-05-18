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

query2 = """SELECT country_name, (COUNT(event_id)*100/(SELECT COUNT(*) FROM TablesJoined))
FROM TablesJoined
GROUP BY country_name"""
cursor.execute(query2)
print("\nSecond Query: countries and UFO events that happened there (as percentage from whole)")
print('country', x * 10, 'percentage')
x2=[]
y2=[]
for rec1 in cursor.fetchall():
    print(rec1[0], rec1[1], '%')
    x2.append(rec1[0])
    y2.append(rec1[1])
colors = ['gold', 'mediumturquoise', 'lightgreen']
fig2 = go.Figure(data=[go.Pie(labels=x2,
                             values=y2)])
fig2.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)))
py.plot(fig2, auto_open=True, filename='graph2')

query3 = """SELECT longitude, COUNT(*)
FROM TablesJoined
GROUP BY longitude
ORDER BY longitude
"""
cursor.execute(query3)
print("\nThird Query: dependency between longitude and concentration events")
print("longitude", x * 5, "events")
x3=[]
y3=[]
for rec in cursor.fetchall():
    print(rec[0], x * 5, rec[1])
    x3.append(rec[0])
    y3.append(rec[1])

fig3= go.Figure(data=go.Scatter(x=x3, y=y3, mode='markers'))
fig3.update_layout(xaxis_title='WEST       longitude       EAST',)
py.plot(fig3, auto_open=True, filename='graph3')


cursor.close()
connection.close()
