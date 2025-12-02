from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


courses = [
    {"id" : 1, "Название курса" : "Python  для начинающих", "Автор" : "NEVAS"},
    {"id" : 2, "Название курса" : "Программирование с нуля", "Автор" : "NEVAS"}     
           ]


users = [
    {"id" : 1, "Имя" : "Степан", "Username" : "Stepko8", },
    {"id" : 2, "Имя" : "Максим", "Username" : "ogyzok", },
    {"id" : 3, "Имя" : "Николай", "Username" : "sigma3000", },
    {"id" : 4, "Имя" : "Артём", "Username" : "ubivator", },
    {"id" : 5, "Имя" : "Вика", "Username" : "vika02103", },
    {"id" : 6, "Имя" : "Егор", "Username" : "levinshytnik", },
    {"id" : 7, "Имя" : "Аня", "Username" : "anyaproffesor", },
    {"id" : 8, "Имя" : "Андрей", "Username" : "ychitelnevasa", },
    {"id" : 9, "Имя" : "Ваня", "Username" : "maincraftlove", },
    {"id" : 10, "Имя" : "Сергей", "Username" : "starostais", }
         ]



@app.get("/courses", summary="Все курсы", tags=["Курсы"])
def get_courses():
    return courses



@app.get("/courses/id/{course_id}", summary="Курс по id", tags=["Курсы"])
def get_course(course_id : int):
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=404, detail="Курс не найден")



@app.get("/users", summary="Получить всех пользователей", tags=["Пользователи"])
def get_users():
    return users



@app.get("/users/id/{user_id}", summary="Получить пользователя по id", tags=["Пользователи"])
def get_user(user_id : int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")



@app.get("/courses/name/{name_course}", summary="Курс по названию", tags=["Курсы"])
def get_course_name(name_course : str):
    for course in courses:
        if course["Название курса"] == name_course:
            return course
    raise HTTPException(status_code=404, detail="Курс не найден")



@app.get("/users/name/{user_name}", summary="Пользователь по имени", tags=["Пользователи"])
def get_user_name(user_name):
    for user in users:
        if user["Имя"] == user_name:
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")
