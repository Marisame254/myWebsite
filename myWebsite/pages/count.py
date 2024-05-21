import reflex as rx

class CountState(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def count():
    return rx.center(
    rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                on_click=CountState.decrement,
            ),
            rx.heading(CountState.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                on_click=CountState.increment,
            ),
            spacing="4",
        )
    )