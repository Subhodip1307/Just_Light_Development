from jld import Template
from jld import APP
from jld.responce import JSONResponse,HTTPResponse

render=Template()


app=APP()

@app.route("/", methods=["GET"])
async def home(request):
    # return await render.render("index.html",{"hi":"2323"})
    return JSONResponse({"hexi":"hello"})

@app.route("/haha", methods=["GET"])
async def submit(request):
    print(request.method)
    return await render.render("result.html", {"name": "name"})
