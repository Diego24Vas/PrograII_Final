from sqlalchemy.orm import Session
from models import Ingrediente

class IngredientesCRUD:
    @staticmethod
    def get_ingrediente(db: Session, ingrediente_id: int):
        return db.query(Ingrediente).filter(Ingrediente.id == ingrediente_id).first()

    @staticmethod
    def get_ingredientes(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Ingrediente).offset(skip).limit(limit).all()

    @staticmethod
    def create_ingrediente(db: Session, nombre: str, cantidad: int):
        db_ingrediente = Ingrediente(nombre=nombre, cantidad=cantidad)
        db.add(db_ingrediente)
        db.commit()
        db.refresh(db_ingrediente)
        return db_ingrediente

    @staticmethod
    def update_ingrediente(db: Session, ingrediente_id: int, nombre: str, cantidad: int):
        db_ingrediente = IngredientesCRUD.get_ingrediente(db, ingrediente_id)
        if db_ingrediente:
            db_ingrediente.nombre = nombre
            db_ingrediente.cantidad = cantidad
            db.commit()
            db.refresh(db_ingrediente)
        return db_ingrediente

    @staticmethod
    def delete_ingrediente(db: Session, ingrediente_id: int):
        db_ingrediente = IngredientesCRUD.get_ingrediente(db, ingrediente_id)
        if db_ingrediente:
            db.delete(db_ingrediente)
            db.commit()
        return db_ingrediente