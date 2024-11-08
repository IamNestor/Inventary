# main.py
from controllers.productController import ProductController
import os, time


def mostrar_menu():
    time.sleep(4)
    os.system('cls')
    print("")
    print("---------------------------------")
    print("=== Sistema de Inventario ===")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("---------------------------------")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            name = input("Nombre del producto: ")
            quantity = int(input("Cantidad: "))
            price = float(input("Precio: "))
            ProductController.createProduct(name, quantity, price)
            print("Producto agregado.")
        
        elif opcion == '2':
            products = ProductController.getProducts()
            print("Productos en inventario:")
            for product in products:
                print(f"ID: {product.id}, Nombre: {product.name}, Cantidad: {product.quantity}, Precio: {product.price}")
        
        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            name = input("Nuevo nombre del producto: ")
            quantity = int(input("Nueva cantidad: "))
            price = float(input("Nuevo precio: "))
            ProductController.updateProduct(id, name, quantity, price)
            print("Producto actualizado.")
        
        elif opcion == '4':
            id = int(input("ID del producto a eliminar: "))
            ProductController.deleteProduct(id)
            print("Producto eliminado.")
        
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
