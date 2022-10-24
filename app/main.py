
from fastapi import FastAPI, APIRouter
from controller.user import router as user_router
from controller.task import router as task_router

router = APIRouter()
# /user
router.include_router(
    user_router,
    prefix='/user',
    tags=['user']
)
# /task
router.include_router(
    task_router,
    prefix='/task',
    tags=['task']
)

app = FastAPI()
app.include_router(router)