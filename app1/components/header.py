import reflex as rx
import requests
import random


class myState(rx.State):
    quote = ""
    author = ""

    def get_quote(self):
        url = "https://type.fit/api/quotes"
        res = requests.get(url)
        data = res.json()
        random_num = random.randrange(0, len(data))
        self.quote = data[random_num]["text"]
        self.author = data[random_num]["author"]


def header():
    return rx.responsive_grid(
        rx.center(
            rx.box(
                rx.heading("Hola trabajo con reflex.", size="xl"),
                rx.heading("Soy developer python", size="sm"),
                rx.button(
                    "click me!.",
                    margin_top="1rem",
                    margin_bottom="0.5rem",
                    on_click=myState.get_quote,
                ),
                quote(),
            )
        ),
        rx.center(rx.image(src="/supermercado.jpeg")),
        columns=[1, 2],
    )


def quote():
    return rx.box(
        rx.text(myState.quote, as_="b", size="20px"),
        rx.box(
            rx.text(myState.author, as_="i"),
        ),
    )
    # return rx.box(rx.text("----quote."), rx.text("author"))
