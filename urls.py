from views import *
from jld import app

app=app()
routes={
    "/":home,
}
app.routes=routes