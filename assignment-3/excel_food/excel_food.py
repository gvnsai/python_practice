'''						"Excel via Python" 
Create a Python script (excel_food.py) to perform the following tasks:
• Create a new workbook named “ViolationTypes.xlsx”.•
• Create a sheet named “Violations Types”.
Query the database and calculate the number of each type of violation based on violation code.
• Write the relevant data into the worksheet you created. This should show the total number of
violations, then list how that is broken down by violation code, including the description of the
violation code. For example:

code | description | count 

foo1 | dirtyfloors | 300
foo2 | rotten food | 135
===========================
  Total_voliations : 435 '''



import xlsxwriter
import mysql
import pandas as pd
import mysql.connector

workbook=xlsxwriter.Workbook("ViolationTypes.xlsx")
worksheet=workbook.add_worksheet("Violation_Types")

database = mysql.connector.connect(host='localhost',
                                  user='vguggilam',
                                  password='Welcome@123',
                                  database='sheets')

mycursor = database.cursor()

mycursor.execute("select violation_code,violation_description,COUNT(*) as count from violations GROUP BY violation_code,violation_description;")

myresult = list(mycursor.fetchall())
#print (myresult)
row=1
col=0
worksheet.write(0,0,'code')
worksheet.write(0,1,'description')
worksheet.write(0,2,'count')
for code,desc,count in myresult:
   worksheet.write(row,col,code)
   worksheet.write(row,col+1,desc)
   worksheet.write(row,col+2,count)
   row +=1
    

df=pd.read_excel('ViolationTypes.xlsx')
print(df)
tot=df['count'].sum()
#row= len(myresult)
worksheet.write(len(myresult)+2,1,'total count:')
worksheet.write(len(myresult)+2,2,tot)

workbook.close()







# import mysql.connector
# import pandas as pd


# try:
# 	sheet_name = "Violation_Types"
# 	file_name = "violation_types.xlsx"
# 	db=mysql.connector.connect(
# 	host="localhost",
# 	user="vguggilam",
# 	passwd="Welcome@123",
# 	database="sheets")
# 	print("connected to database")

# 	mycursor=db.cursor()
# 	mycursor.execute("select violation_code,violation_description,COUNT(*) as count from violations GROUP BY violation_code,violation_description;")

# 	pdlist = []
# 	for row in mycursor:
# 		templist = []
# 		print("code : ", row[0])
# 		print("description : ", row[1])
# 		print("count : ", row[2])

# 		templist.append(row[0])
# 		templist.append(row[1])
# 		templist.append(row[2])
# 		pdlist.append(templist)

# 	column = ["code", "description", "count"]
# 	df=pd.DataFrame(pdlist,columns=column)
# 	total=df["count"].sum()

# 	df2 = pd.DataFrame([["Total_voliations,total"]],columns=["Total_voliations","sum"])
# 	print(df2)
# 	try:
# 		writer = pd.ExcelWriter(violation_types, engine = 'xlsxwriter')
# 		df.to_excel(writer, sheet_name=sheet_name, index=False)
# 		df2.to_excel(writer, sheet_name=sheet_name, startcol=1, startrow=2, header=False,index=False)
# 		writer.save()
# 	except Exception as e:
# 		print(e)
	
# except Exception as e:
# 	print(e)
# 	db.close()

