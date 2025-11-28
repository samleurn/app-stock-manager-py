from fastapi import APIRouter
from ..controller.product_controller import ProductController

product = APIRouter(prefix="/products")

pc = ProductController()


@product.get("/")
def get_products():
    return pc.getProducts()


@product.get("/{uuid}")
def get_product(uuid):
    return pc.getProductByUuid(uuid)


@product.post("/")
def post_product():
    return pc.postProduct()


@product.put("/{uuid}")
def put_product(uuid):
    return pc.putProduct(uuid)


@product.delete("/{uuid}")
def delete_product(uuid):
    return pc.deleteProduct(uuid)
