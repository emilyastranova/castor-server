"""Tasks endpoint."""
from fastapi import APIRouter
from castor_server.settings import database
from castor_lib.core.models.job import Job

router = APIRouter()


@router.get("/")
def get_jobs() -> list[Job]:
    """
    Returns all tasks.
    """
    return database.get_collection(Job)
