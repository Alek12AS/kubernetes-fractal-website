from fastapi import FastAPI
from fastapi.responses import FileResponse
from koch_snowflake import draw_snowflake

app = FastAPI()

@app.get("/koch/{order}")
async def provide_page(order:int):
    '''Draw snowflake and provide html page with the image.'''
    draw_snowflake(order)
    return FileResponse('koch_snowflake.png')
