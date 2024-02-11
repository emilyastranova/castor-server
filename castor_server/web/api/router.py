from fastapi.routing import APIRouter

from castor_server.web.api import docs, echo, monitoring, v1

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(v1.router, prefix="/v1", tags=["v1"])
