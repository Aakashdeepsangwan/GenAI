
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from pydantic.type_adapter import R

app = FastAPI()
# EndPoint - One End of the communication channel

"""  
EndPoints :
1) Get - get an information
2) Post - creating something new
3) Put - update the data
4) Delete - delete the data from database
"""


students = {
    1 : {
        "name" : "John",  "age" : 17, "class" : "12th"
    }
}

# As the basemodel is imported, we will create a new class
class Student(BaseModel) :
    name : str
    age : int
    year : str


class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None 

# create a new API - /= homepage

@app.get("/")
def index() :
    return {"name" : "First Data"} # returns the Json data


# Conditions can be implemented : gt, lt
@app.get("/get-student/{student_id}")
def get_student(student_id : int = Path(..., description="Provide the ID of the student", gt= 0, lt=3)) :
    # if student_id not in students:
    #     return {"error": f"Student with ID {student_id} not found"}
    return students[student_id]



# EndPoint Parameter 



# Query Parameter - 

""" 
In Path Parameter we need to add the parameter in the endpoint
However for query parameter we don't need to add anything in the endpoint

we can make query parameter optional
str = None > give you option to not input anything -> return directly data not found
Optinal[str]=None

test = int, name : Optional[str]= None
Python doesn't allow optional parameters to be in the starting

"""

@app.get("/get-by-name")
def get_student(*,name : Optional[str] = None, test : int ):
    for student_id in students :
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Data not found"}



# Request Body and the post method - create a new object




@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student) :
    if (student_id in students) :
        return {"Error" : "Student Exist"}

    students[student_id] = student
    return students[student_id]




#  Put METHOD - updates the data that already exists
@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : UpdateStudent) :
    if student_id not in students :
        return {"Error" : "student_id doesn't exist"}
    
    if student.name !=None :
        students[student_id].name = student.name

    if student.age != None :
        students[student_id].age = student.age
    
    if student.year!= None :
        students[student_id].year = student.year
    return students[student_id]



@app.delete("/delete-student/ student_id}")
def delete_student(student_id : int):
    if student_id not in students :
        return {"Error" : "Student doesn't Exist"}
    
    del students[student_id]
    return {"Message" : "Student deleted successfully"}

