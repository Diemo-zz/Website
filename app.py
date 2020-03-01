# Originally from https://www.starlette.io/templates/
from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from application.pages import index_page, about_me, fortran_tutorial_one, input_fortran_code, show_fortran_results


def start_up():
	pass

routes = [
    Route("/", endpoint=index_page),
    # Route("/aboutme", endpoint = about_me),
    #Route("/fortran1", endpoint = fortran_tutorial_one),
	Route("/runfortran", endpoint = input_fortran_code, methods = ["GET", "POST"]),
	Route("/show_fortran_results", endpoint = show_fortran_results, methods = ["POST"]),
	Mount("/static", StaticFiles(directory="./static"), name="static"),

]

app = Starlette(routes=routes, debug=True, on_startup = [start_up])

