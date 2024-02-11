"""castor_server v1 endpoint"""
from fastapi import APIRouter

from castor_server.web.api.v1 import tasks

router = APIRouter()

router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])