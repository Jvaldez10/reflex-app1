import reflex as rx


def navbar():
    return rx.flex(
        rx.box(
            rx.image(src="/market.png"),
            width="60px",
        ),
        rx.center(
            rx.menu(
                rx.menu_button("MENU"),
                rx.menu_list(rx.menu_item("top productos"), rx.menu_item("categorias")),
            ),
        ),
        justify_content="space-between",
    )
