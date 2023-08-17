import reflex as rx
from .components.navbar import navbar


def index():
    return rx.container(
        navbar(),
    )


def about():
    return rx.text(
        "conoce mas acerca de nosotros  .....",
        font_size="40px",
        color="red",
        bg="black",
        _hover={"color": "white", "bg": "red"},
    )


app = rx.App()
app.add_page(index)
app.add_page(about, route="/about")
app.compile()
