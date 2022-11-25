from starlette.requests import Request
from starlette.responses import Response, PlainTextResponse


async def handle_hello(request: Request) -> Response:
    return PlainTextResponse("hello")
