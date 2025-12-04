from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


courses = [
    {"id": 1, "name": "Python  для начинающих", "author": "NEVAS"},
    {"id": 2, "name": "Программирование с нуля", "author": "NEVAS"}     
           ]


users = [
    {"id": 1, "name":"Степан", "username":"Stepko8", },
    {"id": 2, "name":"Максим", "username":"ogyzok", },
    {"id": 3, "name":"Николай", "username":"sigma3000", },
    {"id": 4, "name":"Артём", "username":"ubivator", },
    {"id": 5, "name":"Вика", "username":"vika02103", },
    {"id": 6, "name":"Егор", "username":"levinshytnik", },
    {"id": 7, "name":"Аня", "username":"anyaproffesor", },
    {"id": 8, "name":"Андрей", "username":"ychitelnevasa", },
    {"id": 9, "name":"Ваня", "username":"maincraftlove", },
    {"id": 10, "name":"Сергей", "username":"starostais", }
         ]




class UserSchema(BaseModel):
    id : int
    name : str
    username : str | int
    
    
class CourseSchema(BaseModel):
    id : int
    name : str
    author :str

@app.get("/courses", summary="Все курсы", tags=["Курсы"])
def get_courses() -> list[CourseSchema]:
    return courses



@app.get("/courses/id/{course_id}", summary="Курс по id", tags=["Курсы"])
def get_course(course_id : int) -> CourseSchema :
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404, detail="Курс не найден")



@app.get("/users", summary="Получить всех пользователей", tags=["Пользователи"])
def get_users() -> list[UserSchema]:
    return users



@app.get("/users/id/{user_id}", summary="Получить пользователя по id", tags=["Пользователи"])
def get_user(user_id : int) -> list[UserSchema]:
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")



@app.get("/courses/name/{name_course}", summary="Курс по названию", tags=["Курсы"])
def get_course_name(name_course : str) -> list[CourseSchema]:
    for course in courses:
        if course["name"] == name_course:
            return course
    raise HTTPException(status_code=404, detail="Курс не найден")



@app.get("/users/name/{user_name}", summary="Пользователь по имени", tags=["Пользователи"])
def get_user_name(user_name) -> list[UserSchema]:
    for user in users:
        if user["name"] == user_name:
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")
