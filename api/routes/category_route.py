from fastapi import APIRouter
from ..controller.category_controller import CategoryController

category = APIRouter()

ctc = CategoryController()


@category.get("/")
def get_category():
    return ctc.category_controller()
