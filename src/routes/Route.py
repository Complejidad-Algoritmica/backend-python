from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..services.MinimumPath import MinimumPath
from ..helpers.GenerateGraph import *
from ..services.Prim import CPrim

router = APIRouter()

@router.get("/obtain-minimum-path", tags=["Paths"])
async def minimum_path(src: str, dest: str) -> JSONResponse:
    try:
        service = MinimumPath()
        src, dest = service.obtain_id_src_dest(src, dest)
        
        generate_graph_image(service.grafo_limitado) # 500 nodes
        all_paths = service.obtain_all_paths(src, dest)
        paths_with_names = service.obtain_paths_with_names(all_paths)

        return JSONResponse(paths_with_names, 202)
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(500, "An error have ocurred")
    
@router.get("/airlines", tags=["Paths"])
async def obtain_airlines(country: str = None, limit: str = None, destinations: str = None) -> JSONResponse:
    try:
        service = MinimumPath()
        airlines = service.obtain_airlines(country, limit, destinations)
        return JSONResponse(airlines, 200)
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(500, "An error have ocurred")

@router.get("/airlines/{src}", tags=["Paths"])
async def obtain_one_airline(src: str) -> JSONResponse:
    try:
        service = MinimumPath()
        airline = service.obtain_one_airline(src)
        return JSONResponse(airline, 200)
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(500, "An error have ocurred")
    
@router.get("/prim", tags=["Paths"])
async def minimum_cost(src: str, dest: str) -> JSONResponse:
    try:
        service = MinimumPath()
        for k, v in service.grafo.items():
            if v["airport"] == src:
                src = k
            if v["airport"] == dest:
                dest = k

        graph = order_graph_prim(service.grafo)

        prim = CPrim(graph, src, dest)
        prim.prim()
        cost = prim.obtener_costo()
        path = prim.obtener_camino()
        path_names = list()

        if cost > 10000: cost /= 1000

        for node in path:
            path_names.append(service.grafo[node]["airport"])


        return JSONResponse({
            'path': path_names,
            'cost': cost
        }, 200)
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(500, "An error have ocurred")