from fastapi import APIRouter, HTTPException
from model import Course
import json

courses_router = APIRouter()

def load_data() ->list:
    try:
        with open("courses.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"파일 로드 중 예외 발생: {e}")
        return []

@courses_router.get("/courses")
async def get_courses() -> list:
    current_data = load_data()
    return current_data

@courses_router.post("/courses")
async def add_courses(courses : Course) -> dict:
    current_data = load_data()
    current_data.append(courses.model_dump())    

    try:
        with open("courses.json", "w", encoding="utf-8") as f:
            json.dump(current_data, f, ensure_ascii=False, indent=2)

        return {"msg": "추가완료", "added_course": courses.model_dump()}
    
    except Exception as e:
        print(f"오류 발생: {e}")
        return {"msg": "파일 저장 중 오류가 발생했습니다."}
