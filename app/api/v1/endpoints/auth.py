from fastapi import APIRouter , Request , Depends
from app.domain.user.value_objects.Email import Email
from app.domain.user.value_objects.Password import Password

router = APIRouter()



@router.get("/name")
async def register(name:str):
    return {"user_id": name}


@router.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": request.body()}