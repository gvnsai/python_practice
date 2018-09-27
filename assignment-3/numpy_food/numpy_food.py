'''							# Numpy in Python #

Create a Python script (numpy_food.py) to perform the following tasks:
• Query the database and retrieve data to calculate the average violations for every month
between July 2015 and December 2017 for each postcode.
• Use MatPlotLib to plot the follow data over time:
o The violations per month for the postcode(s) with the highest total violations o The
violations per month for the postcode(s) with the greatest variance (difference) between
the lowest and highest number of violations for all months.
o
The average violations per month for ALL of California (all postcodes combined) o The
violations per month for all McDonalds and Burger Kings. This will require a new query as
it is not grouped by postal code.'''

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

pdlist=[]
pd1list=[]
mclist=[]
burlist=[]
try:
	conn = sqlite3.connect('food_violations.db')
	print ("Database co0nnected successfully");

	#selecting distinct bussiness with atlest one violation sql query

	sql = """SELECT \
    	VIOLATIONS.serial_number as v_code, \
    	INSPECTIONS.activity_date as date,\
	INSPECTIONS.facility_zip  as postcode\
    	FROM INSPECTIONS\
    	INNER JOIN VIOLATIONS ON INSPECTIONS.serial_number=VIOLATIONS.serial_number WHERE INSPECTIONS.activity_date BETWEEN "2015-07-01" AND 		"2017-12-01";"""

#select inspections.activity_date,violations.violation_description from inspections,violations where inspections.serial_number=violations.serial_number WHERE INSPECTIONS.activity_date BETWEEN "2015-07-01" AND "2017-12-01";
	cursor = conn.execute(sql)

	
	#appending to a list inside the for 
	for row in cursor:
   		templist=[]   
   		templist.append(row[0])
   		templist.append(row[1])
   		templist.append(row[2])
   		pdlist.append(templist)
	print ("Operation done successfully");



	sql_mc = """  SELECT    facility_name,  violations.serial_number as v_code,      inspections.activity_date as date     FROM inspections     INNER JOIN violations ON inspections.serial_number=violations.serial_number WHERE inspections.facility_name like '%McDonalds%' OR  '%BURGER KING%';"""
	
	cursor = conn.execute(sql_mc)
	#appending to a list inside the for 
	for row in cursor:
   		templist=[]   
   		templist.append(row[0])
   		templist.append(row[1])
   		templist.append(row[2])
   		mclist.append(templist)
	print ("mcd Operation done successfully");

	sql_bur = """ SELECT    facility_name,  violations.serial_number as v_code,      inspections.activity_date as date     FROM inspections     INNER JOIN violations ON inspections.serial_number=violations.serial_number WHERE inspections.facility_name like  '%BURGER KING%';"""
	
	cursor = conn.execute(sql_bur)
	#appending to a list inside the for 
	for row in cursor:
   		templist=[]   
   		templist.append(row[0])
   		templist.append(row[1])
   		templist.append(row[2])
   		burlist.append(templist)
	print ("burger Operation done successfully");
	
	
except Exception as e:
	print(e)

clos=["v_code","date","postcodes"]
df=pd.DataFrame(pdlist,columns=clos)
df3=pd.DataFrame()
df4=pd.DataFrame()
y1=pd.DataFrame()

df['date'] = pd.to_datetime(df['date'])
df2=df.groupby(['v_code', 'date']).size().reset_index(name='counts')
df3['avg_counts']=df2.groupby(df['date'].dt.strftime('%B'))['counts'].mean().sort_values()
df3['month']=df3.index
#avg on month bases
print(df3.head())
print(df.head())
#df to plot highest violations
df4=df.groupby(['postcodes','date']).size().reset_index(name='post_counts')
df4['count_max'] = df4.groupby(df4['date'].dt.strftime('%B'))['post_counts'].transform(max)
df4['count_min'] = df4.groupby(df4['date'].dt.strftime('%B'))['post_counts'].transform(min)
df4['diff_count'] = df4['count_max']-df4['count_min']




# bk dfs 
mcclos=["name","v_code","date"]
mc=pd.DataFrame(mclist,columns=mcclos)

print(mc.head())


# bk dfs 
bkclos=["name","v_code","date"]
bkdf=pd.DataFrame(burlist,columns=bkclos)

print(bkdf.head())
framelist=[mc,bkdf]
mcbkdf = pd.concat(framelist)
print(mcbkdf.head(30))

mcbkdf=mcbkdf.groupby(['name', 'date']).size().reset_index(name='counts')
#print(mcbkdf.head())
y1['avg_counts']=mcbkdf.groupby(df['date'].dt.strftime('%B'))['counts'].mean()
print(type(y1))

y1['month']=y1.index
print(y1.head())
#graphs

x=df4['date'].dt.strftime('%B').head(30)
y=df4['diff_count'].head(30)

plt.bar(x,y,color = "red" )
plt.title("violations difference")
plt.xlabel("dates")
plt.ylabel("differences of max and min postcodes")
plt.legend()
plt.show() 
x2=df4['date'].dt.strftime('%B')
y3=df3['avg_counts']=df2.groupby(df['date'].dt.strftime('%B'))['counts'].mean().sort_values()
plt.plot(y3)
plt.title("averages")
plt.xlabel("dates")
plt.ylabel("monthely avreage violations")
plt.show()
y2=mcbkdf.groupby(df['date'].dt.strftime('%B'))['counts'].mean()
plt.plot(y2)
plt.title("McD and BK average per month")
plt.xlabel("months")
plt.ylabel("averages per month")
plt.show()
y4=df4['count_max']
plt.plot(y4)
plt.title("max number of violation based on postcodes")
plt.xlabel("month")
plt.ylabel("max violations")
plt.show()



