from fastapi import APIRouter, HTTPException


router = APIRouter( prefix="/products", #prefix establece una direccion predeterminada, no hace falta especificar en @router
                    responses = {404: {"message":"No encontrado"}}, #respuesta default en caso de error
                    tags={"products"}   #tag para agrupar en la documentacion
                    ) 

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    try:
        return products_list[id]
    except:
        raise HTTPException(status_code=404, detail= "no se ha encontrado el producto")