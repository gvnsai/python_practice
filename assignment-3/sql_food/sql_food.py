'''						"Query the database"
Create a Python script (sql_food.py) to perform the following tasks:
• List the distinctive businesses that have had at least 1 violation ordered alphabetically to the
console and then write their name, address, zip code and city into a new database table called
“Previous violation”.
• Print a count of the violation for each business that has at least 1 violation to the console
along with their name ordered by the number of violation. *SQL Hint: Group By* '''


import mysql.connector
import pandas as pd

db=mysql.connector.connect(
host="localhost",
user="vguggilam",
passwd="Welcome@123",
database="sheets")
mycursor=db.cursor()


sql="select distinct inspection.facility_name as name,inspection.facility_address as address,inspection.facility_zip as zip_code,inspection.facility_city as city from inspection inner join violation on inspection.serial_number=violation.serial_number order by name ASC;"
mycursor.execute(sql)
res =list(mycursor.fetchall())
print(res)



# sql="create table previous_violation as select distinct inspection.facility_name as name,inspection.facility_address as address,inspection.facility_zip as zip_code,inspection.facility_city as city from inspection inner join violation on inspection.serial_number=violation.serial_number order by name ASC;"
# mycursor.execute(sql)
sql1="select * from previous_violation;"
mycursor.execute(sql1)
# res=mycursor.fetchall()
for x in mycursor:
   print(x)





