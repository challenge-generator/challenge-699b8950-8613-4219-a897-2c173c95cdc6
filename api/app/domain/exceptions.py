class ProductNotFoundError(Exception):
    """Excepción lanzada cuando un producto no es encontrado."""
    def __init__(self, product_id: int):
        self.product_id = product_id
        super().__init__(f"Product with id {product_id} not found")

class ProductAlreadyExistsError(Exception):
    """Excepción lanzada cuando se intenta crear un producto con un nombre que ya existe."""
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Product with name {name} already exists")

class InvalidProductDataError(Exception):
    """Excepción lanzada cuando los datos del producto son inválidos."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class DatabaseError(Exception):
    """Excepción lanzada cuando ocurre un error en la base de datos."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)