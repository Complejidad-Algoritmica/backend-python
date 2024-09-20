from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..services.MinimumPath import MinimumPath

router = APIRouter()

@router.get("/obtain-minimum-path", tags=["Paths"])
async def minimum_path(src: str, dest: str):
    try:
        service = MinimumPath()
        all_paths = service.obtain_all_paths(src, dest)
        paths_with_names = service.obtain_paths_with_names(all_paths)
        return JSONResponse(paths_with_names, 202)
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(500, "An error have ocurred")