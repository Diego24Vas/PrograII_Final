# Definicion de los modelos ORM

from sqlalchemy import Column, Integer, String, Float
from database import Base

class Ingrediente(Base):
    __tablename__ = 'ingredientes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    cantidad = Column(Integer)

    def __init__(self, nombre, cantidad):
        self.nombre = nombre.lower()
        self.cantidad = cantidad

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    cantidad = Column(Integer)
    precio = Column(Float)

    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

        