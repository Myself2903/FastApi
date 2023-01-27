from fastapi import FastAPI
from routers import products, users, jwt_auth_users, basic_auth_users
from fastapi.staticfiles import StaticFiles

#API: Application Programming Interfaces 
app = FastAPI()

#Routers -> permiten conectar el main con los "routers", otras instancias de la API
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_users.router)

#Recursos estaticos (imgs, docs, etc)
app.mount("/static" , StaticFiles(directory="static"), name="static")

@app.get("/")               #decorador: indica que la funcion de abajo pertenece a la respuesta a una peticion get en la ruta /
async def root():
    return "hello world"

@app.get("/hidden")
async def hidden():
    return {"hidden_message":"mensaje oculto"} #enviar archivos json es la convención (no hagas lo anterior)

#iniciar el server:   uvicorn main:app --reload
#el anterior no me funciona así que usa: python -m uvicorn main:app --reload

#documentación Swagger: /docs
#documentación Redocly: /redoc

#postman para realizar peticiones get o thunder client (Extension de VsCode)