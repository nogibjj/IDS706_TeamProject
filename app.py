"""FastAPI microservice for ICU data"""
from fastapi import FastAPI
import uvicorn
from dblib.dbquery import DB

app = FastAPI()
db = DB()

@app.get("/")
async def root():
    """Welcome message on homepage"""
    return "Welcome to the ICU data service!"

@app.get("/icu_info/{MMSA}")
async def get_icu_info(MMSA: str):
    """Return ICU-related info for a specified MMSA"""
    return db.get_icu_info(MMSA)

@app.get("/hospitals_info")
async def get_hospitals_info():
    """Return summary info about hospitals"""
    return db.get_hospitals_info()

# Add additional endpoints as needed

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
