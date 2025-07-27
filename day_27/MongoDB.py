from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template
uri = 'mongodb+srv://benchong0248:txGjtjYEcjde4LBm@bencluster0248.2ntwz7t.mongodb.net/?retryWrites=true&w=majority&appName=BenCluster0248'
client = MongoClient(uri)
db = client.BenCluster0248
db.students.insert_one({'name':'Benjamin', 'country':'USA', 'city':'Sacramento', 'age': 20})
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

person = db.students.find_one({'_id':ObjectId('68853740d0e159757fa61598')}) #find one 
print(person)

students = db.students.find() #find and print all of the people in the database
for student in students:
    print(student)

students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)

query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query).limit(5).sort('age') #adding a to the amount found and sort
 
for student in students:
    print(student)

db.students.drop()
print(client.list_database_names())