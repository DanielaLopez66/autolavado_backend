from fastapi import FastAPI 

app = FastAPI(
    title="Sistema de control de autolavado",
    descripcion="Sistema de creacion y almacenamiento de informacion y ventas en un autolavado"
)

app.include_router(rol)