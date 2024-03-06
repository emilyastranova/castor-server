"""Tasks endpoint."""
from fastapi import APIRouter
from castor_server.settings import database
from castor_lib.core.models.comment import Comment

router = APIRouter()


@router.get("/")
def get_comments() -> list[Comment]:
    """
    Returns all comments.
    """
    return database.get_collection(Comment)
