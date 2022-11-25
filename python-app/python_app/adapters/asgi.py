from starlette.applications import Starlette
from starlette.routing import Route
from . import http

app = Starlette(
    debug=True,
    routes=[
        Route("/hello", http.handle_hello),
    ],
)
