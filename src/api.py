from fastapi import FastAPI
import matplotlib.pyplot as plt
from . import koch_snowflake as koch

app = FastAPI()

@app.get("/koch/{order}")
async def draw_snowflake(order:int):
    '''Draw snowflake and save it as png.'''
    x,y = koch.koch_snowflake(order)
    plt.figure(figsize=(8,8))
    plt.axis('equal')
    plt.fill(x,y)
    
    fname='../artifacts/koch-snowflake.png'
    format='png'
    plt.savefig(fname=fname,format=format)
    