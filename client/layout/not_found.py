from reactpy import component, html


@component
def NotFound():
    return html.h1("404 Not Found")
