"""castor_server v1 endpoint"""
from fastapi import APIRouter

from castor_server.web.api.v1 import tasks, jobs, agents, comments

router = APIRouter()

router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
router.include_router(agents.router, prefix="/agents", tags=["agents"])
router.include_router(comments.router, prefix="/comments", tags=["comments"])