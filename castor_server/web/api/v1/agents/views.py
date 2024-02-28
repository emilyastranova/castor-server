"""Tasks endpoint."""
from fastapi import APIRouter
from castor_server.settings import database
from castor_lib.core.models.agent import Agent

router = APIRouter()


@router.get("/")
def get_agents() -> list[Agent]:
    """
    Returns all tasks.
    """
    return database.get_collection(Agent)
