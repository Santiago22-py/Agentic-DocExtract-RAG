from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["health"])

@router.get("/health")
def health_check():
    return {"status": "ok"}