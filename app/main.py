
from fastapi import FastAPI, APIRouter
from controller.user import router as user_router

router = APIRouter()
# /user
router.include_router(
    user_router,
    prefix='/user',
    tags=['user']
)

app = FastAPI()
app.include_router(router)