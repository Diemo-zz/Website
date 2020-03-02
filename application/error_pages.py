from starlette.responses import HTMLResponse
from application import templates

HTML_404_PAGE = """$=$ NOT FOUND"""
HTML_405_PAGE = """405 Not Found"""
HTML_500_PAGE = """500 Page not found"""


async def not_found(request, exc):
    return templates.TemplateResponse("404_not_found.html", {"request": request, "code": exc})

async def server_error(request, exc):
    return HTMLResponse(content=HTML_500_PAGE, status_code=exc.status_code)


async def four_oh_four_not_found(request, exc):

    return templates.TemplateResponse("NotFound/404_not_found.html", {"request": request, "code": exc,
                                                                      "url": request.url, "return_page": "/index",
                                                                      "return_message": "Return to index page?"})


async def four_oh_five_not_found(request, exc):
    return HTMLResponse(content=HTML_404_PAGE, status_code=exc.status_code)

