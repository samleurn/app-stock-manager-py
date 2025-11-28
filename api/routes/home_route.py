from fastapi import APIRouter
from ..controller.home_controller import HomeController

home = APIRouter()

hc = HomeController()


@home.get("/")
def get_home():
    return hc.getHome()
