# Originally from https://www.starlette.io/templates/
from starlette.responses import HTMLResponse
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from application.pages import (
    index_page,
    about_me,
    fortran_tutorial_one,
    input_fortran_code,
    show_fortran_results,
	test_endpoint,
)
from application.error_pages import (
    four_oh_four_not_found,
    server_error,
    four_oh_five_not_found,
)


def start_up():
    pass


exception_handlers = {
    404: four_oh_four_not_found,
    405: four_oh_five_not_found,
    500: server_error,
}


routes = [
    Route("/index", endpoint=index_page),
    Route("/about_me", endpoint=about_me),
	Route("/test", endpoint = test_endpoint),
    # Route("/fortran1", endpoint = fortran_tutorial_one),
    Route("/runfortran", endpoint=input_fortran_code, methods=["GET", "POST"]),
    Route("/show_fortran_results", endpoint=show_fortran_results, methods=["POST"]),
    Mount("/static", StaticFiles(directory="./static"), name="static"),
]

app = Starlette(
    routes=routes,
    debug=True,
    on_startup=[start_up],
    exception_handlers=exception_handlers,
)
