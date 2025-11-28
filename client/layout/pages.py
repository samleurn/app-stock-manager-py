from reactpy import component, html
from .home import Home
from .not_found import NotFound


class Pages:
    def __init__(self): ...
    def renderHome(self):
        return Home()

    def renderForm(): ...
    def renderDashboard(): ...
    def renderNotFound():
        return NotFound()
