from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from .layout.pages import Pages

app = FastAPI()

layout = Pages()


@component
def App():
    return layout.renderHome()


configure(app, App)

