import mysql.connector
import xlrd

from datetime import datetime
import traceback

# Open the workbook and define the worksheet
book = xlrd.open_workbook("/home/vguggilam/Desktop/assignment-3/data/violations.xlsx")
sheet1 = book.sheet_by_name("violations")

book = xlrd.open_workbook("/home/vguggilam/Desktop/assignment-3/data/inspections.xlsx")
sheet2 = book.sheet_by_name("inspections")

# Establish a MySQL connection
db=mysql.connector.connect(
host="localhost",
user="vguggilam",
passwd="Welcome@123",
database="sheets")

# Get the cursor, which is used to traverse the database, line by line
mycursor1=db.cursor()
mycursor2=db.cursor()

# Create the INSERT INTO sql query
query1="insert into violations(points,serial_number,violation_code,violation_description,violation_status)values(%s,%s,%s,%s,%s)"
for r in range(1, sheet1.nrows):
   points=sheet1.cell(r,0).value
   serial_number=sheet1.cell(r,1).value
   violation_code=sheet1.cell(r,2).value
   violation_description=sheet1.cell(r,3).value
   violation_status=sheet1.cell(r,4).value

# Assign values from each row
   values1=(points,serial_number,violation_code,violation_description,violation_status)

# Execute sql Query   
   mycursor1.execute(query1, values1)

query2 = "insert into inspections(activity_date,employee_id,facility_address,facility_city,facility_id,facility_name,facility_state,facility_zip,grade,owner_id,owner_name,pe_description,program_element_pe,program_name,program_status,record_id,score,serial_number,service_code,service_description) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
for r in range(1, sheet2.nrows):
    activity_date = sheet2.cell(r,0).value
    employee_id = sheet2.cell(r,1).value
    facility_address = sheet2.cell(r,2).value
    facility_city = sheet2.cell(r,3).value
    facility_id = sheet2.cell(r,4).value
    facility_name = sheet2.cell(r,5).value
    facility_state = sheet2.cell(r,6).value                                    
    facility_zip = sheet2.cell(r,7).value
    grade = sheet2.cell(r,8).value
    owner_id = sheet2.cell(r,9).value
    owner_name = sheet2.cell(r,10).value
    pe_description = sheet2.cell(r,11).value
    program_element_pe = sheet2.cell(r,12).value
    program_name =     sheet2.cell(r,13).value
    program_status = sheet2.cell(r,14).value
    record_id = sheet2.cell(r,15).value
    score = sheet2.cell(r,16).value
    serial_number = sheet2.cell(r,17).value
    service_code = sheet2.cell(r,18).value
    service_description = sheet2.cell(r,19).value

# Assign values from each row
    values2 =(activity_date,employee_id,facility_address,facility_city,facility_id,facility_name,facility_state,facility_zip,grade,owner_id,owner_name,pe_description,program_element_pe,program_name,program_status,record_id,score,serial_number,service_code,service_description)

# Execute sql Query   
    mycursor2.execute(query2, values2)

# Close the cursor
mycursor1.close()
mycursor2.close()

# Commit the transaction
db.commit()

# Close the database connection
db.close()

print ("")
print ("Check u r database!")
print ("")

columns = str(sheet1.ncols)
columns = str(sheet2.ncols)

rows = str(sheet1.nrows)
rows = str(sheet2.nrows)