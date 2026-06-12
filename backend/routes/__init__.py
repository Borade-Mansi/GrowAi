# Routes module
from .students import router as students_router
from .agents import router as agents_router
from .missions import router as missions_router
from .progress import router as progress_router

__all__ = [
    "students_router",
    "agents_router",
    "missions_router",
    "progress_router",
]
