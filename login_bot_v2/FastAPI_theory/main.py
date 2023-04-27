from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/about")
async def about():
    return {"message": "О сайте"}


@app.get("/about-myself")
async def about_myself():
    data = {
        'first_name': 'Артем',
        'last_name': 'Трошкин',
        'age': 21,
        'educational_institution': 'ITeen Academy',
        'phone_number': '+375291234567'
    }
    return JSONResponse(content=data,
                        media_type="application/json",
                        status_code=200)
