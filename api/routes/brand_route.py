from fastapi import APIRouter
from ..controller.brand_controller import BrandController

home = APIRouter()

bnc = BrandController()


@home.get("/")
def get_home():
    return bnc.home_controller()
