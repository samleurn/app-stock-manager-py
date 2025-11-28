from .index_controller import HomeControllerBase


class HomeController(HomeControllerBase):
    def __init__(self):
        super().__init__()

    def getHome(self):
        return {"msg": "Home Route"}
