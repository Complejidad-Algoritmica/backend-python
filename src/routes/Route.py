from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..services.MinimumPath import MinimumPath

router = APIRouter()

@router.get("/obtain-minimum-path", tags=["Paths"])
async def minimum_path(src: str, dest: str):
    try:
        service = MinimumPath()
        path = service.bfs(src, dest)

        return JSONResponse({"path": path}, 202)
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(500, "An error have ocurred")