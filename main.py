# Script para inicializar las tablas 

from database import get_session, engine, Base
from crud.cliente_crud import ClienteCRUD
from crud.pedido_crud import PedidoCRUD
from crud.ingredientes_crud import IngredientesCRUD
from database import Base
# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Función principal para el uso del CRUD
def main():
    # Crear una sesión
    db = next(get_session())

    # Intentar crear un cliente
    cliente = ClienteCRUD.create_cliente(db, "Carlos", "carlos@example.com")
    if cliente:
        print(f"Cliente creado: {cliente.nombre} - {cliente.correo_electronico}")
    else:
        print("El cliente ya existe con ese correo electrónico.")

    # Intentar crear un pedido para el cliente existente
    pedido = PedidoCRUD.create_pedido(db, cliente.id, "Pedido de muebles", 100.0)
    if pedido:
        print(f"Pedido creado: {pedido.nombre} para el cliente {cliente.nombre}")
    else:
        print("No se pudo crear el pedido.")

    # Intentar crear un ingrediente
    ingrediente = IngredientesCRUD.create_ingrediente(db, "Madera", 100)
    if ingrediente:
        print(f"Ingrediente creado: {ingrediente.nombre} - {ingrediente.cantidad}")
    else:
        print("No se pudo crear el ingrediente.")

    # Leer todos los clientes en la base de datos
    print("\nClientes en la base de datos:")
    clientes = ClienteCRUD.get_clientes(db)
    for c in clientes:
        print(f"- {c.nombre} ({c.correo_electronico})")

    # Actualizar el nombre del cliente
    cliente_actualizado = ClienteCRUD.update_cliente(db, cliente.id, "Carlos Gómez", "carlos@example.com")
    if cliente_actualizado:
        print(f"\nCliente actualizado: {cliente_actualizado.nombre} - {cliente_actualizado.correo_electronico}")
    else:
        print("No se pudo actualizar el cliente (posiblemente el email ya está en uso).")

    # Borrar un pedido
    pedido_eliminado = PedidoCRUD.delete_pedido(db, pedido.id)
    if pedido_eliminado:
        print(f"Pedido con ID {pedido.id} eliminado")

    # Borrar un ingrediente
    ingrediente_eliminado = IngredientesCRUD.delete_ingrediente(db, ingrediente.id)
    if ingrediente_eliminado:
        print(f"Ingrediente con ID {ingrediente.id} eliminado")

if __name__ == "__main__":
    main()
