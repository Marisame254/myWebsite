"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from myWebsite import pages, api

# Add to FrontEnd
app = rx.App()
app.add_page(pages.index)
app.add_page(pages.count)


# Add to BackEnd
app.api.add_api_route(
    path="/",
    endpoint=api.hello
)
