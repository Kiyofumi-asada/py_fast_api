
from fastapi import FastAPI, APIRouter
from controller.task import router as task_router

router = APIRouter()
# /task
router.include_router(
    task_router,
    prefix='/task',
    tags=['task']
)

app = FastAPI()
app.include_router(router)