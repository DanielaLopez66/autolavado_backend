"""
Schema para roles del sistema de autolavado.
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    """Base schema para roles."""
    nombre: str
    papellido = str
    sapellido = str
    direccion = str
    telefono = str
    correo = str
    contrasena = str
    estatus = bool
    fecha_creacion = datetime
    fecha_modificacion = datetime


class UserCreate(UserBase):
    """Schema para crear roles."""
    pass


class UserUpdate(UserBase):
    """Schema para actualizar roles."""
    pass


class User(UserBase):
    """Schema completo para roles."""
    id: int

    class Config:
        """Configuración de Pydantic."""
        orm_mode = True

class userLogin(BaseModel):
    """"clase para realizar"""
    telefono: Optional[str] = None
    correo: Optional[str] = None
    contrasena : str 
