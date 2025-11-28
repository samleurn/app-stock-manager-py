from .index_controller import ProductControllerBase


class ProductController(ProductControllerBase):
    def __init__(self):
        super().__init__()

    def getProducts(self):
        return {"msg": "Products Route"}
