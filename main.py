from jld import Template
from jld import app
render=Template()


app=app()
@app.route("/", methods=["GET"])
async def home(request):
    return render.render("index.html",{"hi":"2323"})

@app.route("/submit", methods=["POST"])
async def submit(request):
    print(request.method)
    name = request.POST.get("name", "Stranger")
    return render.render("result.html", {"name": "name"})
