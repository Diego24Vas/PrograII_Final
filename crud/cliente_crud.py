from sqlalchemy.orm import Session
from models import Cliente

class ClienteCRUD:
    @staticmethod
    def get_cliente(db: Session, cliente_id: int):
        return db.query(Cliente).filter(Cliente.id == cliente_id).first()

    @staticmethod
    def get_clientes(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Cliente).offset(skip).limit(limit).all()

    @staticmethod
    def create_cliente(db: Session, nombre: str, correo_electronico: str):
        db_cliente = Cliente(nombre=nombre, correo_electronico=correo_electronico)
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)
        return db_cliente

    @staticmethod
    def update_cliente(db: Session, cliente_id: int, nombre: str, correo_electronico: str):
        db_cliente = ClienteCRUD.get_cliente(db, cliente_id)
        if db_cliente:
            db_cliente.nombre = nombre
            db_cliente.correo_electronico = correo_electronico
            db.commit()
            db.refresh(db_cliente)
        return db_cliente

    @staticmethod
    def delete_cliente(db: Session, cliente_id: int):
        db_cliente = ClienteCRUD.get_cliente(db, cliente_id)
        if db_cliente:
            db.delete(db_cliente)
            db.commit()
        return db_cliente