from fastapi import FastAPI
import uvicorn
from courses import courses_router
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "msg": "2025205145조수현 오픈소스소프트웨어실습 FastAPI 과제 서버입니다"
    }
app.include_router(courses_router)
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)