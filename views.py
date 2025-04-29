from jld import Template
render=Template()


async def home(request):
    print(request.GET)
    return render.render("index.html",{"hi":"2323"})

async def submit(request):
    print(request.POST.getlist('name'))
    return render.render("result.html", {"name": "name"})
