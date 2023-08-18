import reflex as rx
from .components.navbar import navbar


def index():
    return rx.container(navbar(), rx.divider())


def about():
    return rx.container(navbar(), rx.divider())


app = rx.App()
app.add_page(index)
app.add_page(about, route="/about")
app.compile()
