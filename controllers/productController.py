# controllers/productController.py
from database.dbConnection import get_db_connection
from models.product import Product

class ProductController:
    
    @staticmethod
    def createProduct(name, quantity, price):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO product (name, quantity, price) VALUES (?, ?, ?)",
            (name, quantity, price)
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def getProducts():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        conn.close()
        return products

    
#    def obtener_productos():
#        conn = get_db_connection()
#        cursor = conn.cursor()
#        cursor.execute("SELECT * FROM productos")
#        productos = cursor.fetchall()
#        conn.close()
        
#        # Convertimos cada fila en una instancia de Producto
#        return [Producto(id=row[0], nombre=row[1], cantidad=row[2], precio=row[3]) for row in productos]


    @staticmethod
    def updateProduct(id, name, quantity, price):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE product SET name = ?, quantity = ?, price = ? WHERE id = ?",
            (name, quantity, price, id)
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def deleteProduct(id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM product WHERE id = ?", (id,))
        conn.commit()
        conn.close()
