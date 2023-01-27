from fastapi import APIRouter, HTTPException
from pydantic import BaseModel      #permite trabajar el objeto como un json

router = APIRouter(tags={"users"})

#url: http://127.0.0.1:8000

#entidad user

class User(BaseModel):
    id: int
    nickname: str
    age: int
    email: str



user_list = [
                User(id=1, nickname="Nico", age=19, email="nico@gmail.com"), 
                User(id=2, nickname="Juan", age=20, email="juan@gmail.com"), 
                User(id=3, nickname="Abuelo", age=20, email="abuelo@gmail.com")
            ]

#definición de buscador
def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}


@router.get("/users_json")
async def users_json():
    return [
        {"name":"Nico", "age": 19},
        {"name":"Juan", "age": 20},
        {"name":"Abuelo", "age":20}
    ]   

@router.get("/users")
async def users():
    return user_list


#parametros pasados por path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#parametros pasados por query con el signo "?"
#para añadir parametros usa el signo "&"
@router.get("/user/")
async def user(id: int):
    return search_user(id)


#post para publicar nuevos datos
@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=405, detail="El usuario ya existe") #rise para lanzar la excepción
    
    user_list.append(user)
    return user



#put para actualizar datos
@router.put("/user/",status_code=202)
async def user(user: User):
    for index, saved_user in enumerate(user_list):
        if(saved_user.id == user.id):
            user_list[index] = user
            return user    

    raise HTTPException(status_code=404, detail = "Usuario no encontrado")


#delete para eliminar datos
@router.delete("/user/{id}", status_code=202)
async def user(id: int):
    for index, saved_user in enumerate(user_list):
        if(saved_user.id == id):
            del user_list[index]
            return {"success":"Usuario eliminado"}

    raise HTTPException(status_code=404, detail = "Usuario no encontrado")
