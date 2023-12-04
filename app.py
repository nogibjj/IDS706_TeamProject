"""FastAPI microservice"""
from fastapi import FastAPI
import uvicorn
from dblib.dbquery import DB


app = FastAPI()
db = DB()


@app.get("/")
async def root():
    """Welcome message on homepage"""
    return "Welcome to our movie database!"


@app.get("/director/{director_name}")
async def get_by_director(director_name: str):
    """Return all movies directed by a specified director"""
    return db.query1(director_name)


@app.get("/goodrating")
async def get_by_rating():
    """Return all movies that have ratings higher than 9"""
    return db.query2()


@app.get("/longest")
async def get_by_runtime():
    """Return the top 10 longest movies"""
    return db.query3()


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
