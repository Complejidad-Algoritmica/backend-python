from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..services.MinimumPath import MinimumPath
from ..helpers.GenerateGraph import generate_graph_image

router = APIRouter()

@router.get("/obtain-minimum-path", tags=["Paths"])
async def minimum_path(src: str, dest: str) -> JSONResponse:
    try:
        service = MinimumPath()
        src, dest = service.obtain_id_src_dest(src, dest)
        
        generate_graph_image(service.grafo_limitado) # 1500 nodes
        all_paths = service.obtain_all_paths(src, dest)
        paths_with_names = service.obtain_paths_with_names(all_paths)

        return JSONResponse(paths_with_names, 202)
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(500, "An error have ocurred")
    
   