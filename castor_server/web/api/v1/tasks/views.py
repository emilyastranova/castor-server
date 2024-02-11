from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def hello_world() -> None:
    """
    Returns "Hello world" message.
    """

    return "Hello, world!"
