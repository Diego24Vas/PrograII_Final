from sqlalchemy.orm import Session
from models import Pedido

class PedidoCRUD:
    @staticmethod
    def get_pedido(db: Session, pedido_id: int):
        return db.query(Pedido).filter(Pedido.id == pedido_id).first()

    @staticmethod
    def get_pedidos(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Pedido).offset(skip).limit(limit).all()

    @staticmethod
    def create_pedido(db: Session, nombre: str, cantidad: int, precio: float):
        db_pedido = Pedido(nombre=nombre, cantidad=cantidad, precio=precio)
        db.add(db_pedido)
        db.commit()
        db.refresh(db_pedido)
        return db_pedido

    @staticmethod
    def update_pedido(db: Session, pedido_id: int, nombre: str, cantidad: int, precio: float):
        db_pedido = PedidoCRUD.get_pedido(db, pedido_id)
        if db_pedido:
            db_pedido.nombre = nombre
            db_pedido.cantidad = cantidad
            db_pedido.precio = precio
            db.commit()
            db.refresh(db_pedido)
        return db_pedido

    @staticmethod
    def delete_pedido(db: Session, pedido_id: int):
        db_pedido = PedidoCRUD.get_pedido(db, pedido_id)
        if db_pedido:
            db.delete(db_pedido)
            db.commit()
        return db_pedido