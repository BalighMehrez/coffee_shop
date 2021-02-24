from pydantic import BaseModel
class Machine(BaseModel):
    sku:str
    product_type:str
    water_line_compatible:bool

class Pod(BaseModel):
    sku:str
    product_type:str
    coffee_flavor:str
    pack_size:str