from fastapi import FastAPI, APIRouter
from controller.user import router as userRouter

router = APIRouter()
router.include_router(
    userRouter,
    prefix='/users',
    tags=['users']
)

app = FastAPI()
app.include_router(router)