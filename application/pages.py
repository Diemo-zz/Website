from application import templates


async def index_page(request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "my_string": "test", "my_list": [1, 2]}
    )


async def about_me(request):
    return templates.TemplateResponse("aboutme.html", {"request": request})


async def fortran_tutorial_one(request):
    print(dir(request))
    print(request.url)
    print(str(request.url))
    return templates.TemplateResponse(
        "fortran_base_tutorial.html", {"request": request}
    )
