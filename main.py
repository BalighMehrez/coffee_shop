from typing import Optional

from fastapi import FastAPI
import datamanager
app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Coffee Shop"}


@app.get("/get_machines")
def get_machines(product_type: Optional[str] = None,water_line_compatible: Optional[bool] = None):
    return datamanager.get_machines(product_type,water_line_compatible)

@app.get("/get_pods")
def get_pods(product_type: Optional[str] = None,coffee_flavor: Optional[str] = None, pack_size: str = None):
    return datamanager.get_pods(product_type,coffee_flavor,pack_size)