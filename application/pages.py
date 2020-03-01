from application import templates
from application.run_fortran import get_fortran_code_result
from urllib.parse import parse_qs, urlparse
from urllib.parse import unquote, quote


async def index_page(request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "my_string": "test", "my_list": [1, 2]}
    )


async def about_me(request):
    return templates.TemplateResponse("aboutme.html", {"request": request})


async def fortran_tutorial_one(request):
    return templates.TemplateResponse(
        "fortran_base_tutorial.html", {"request": request}
    )


async def input_fortran_code(request):
    code = request.query_params.get("code", "")
    name = request.query_params.get("pname", "")
    if name:
        name = unquote(name)
    if code:
        code = unquote(code)
    return templates.TemplateResponse(
        "input_fortran_code.html", {"request": request, "name": name, "code": code},
    )


async def show_fortran_results(request):
    body = await request.body()
    options = parse_qs(body)
    code = options.get(b"code", [None])[0]
    name = options.get(b"pname", [None])[0]
    if name:
        name = unquote(name)
    if code:
        code = unquote(code)
    else:
        return templates.TemplateResponse(
            "input_fortran_code.html", {"request": request, "name": name, "code": code}
        )
    results, errors = get_fortran_code_result(code_in=code)
    quoted_code = quote(code)
    return templates.TemplateResponse(
        "show-fortran-results.html",
        {
            "request": request,
            "code": code,
            "quoted_code": quoted_code,
            "results": results,
            "errors": errors,
        },
    )
