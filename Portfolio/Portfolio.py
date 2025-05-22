import reflex as rx
from .views.index import index

app = rx.App()
app.add_page(index)
