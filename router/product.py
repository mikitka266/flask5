from fastapi import APIRouter

from db import products

router = APIRouter()



@router.post('/product', response_model = ProductIn)
async def create_product(product: ProductIn):
    product.insert().values(id=product.id,
                          name_product=product.name_product,
                          properties=product.properties,
                          price=product.price)
    return product


@router.get('/products/', response_model=List[Product])
async def read_product():
    query = products.select()
    for i in await database.fetch_all(query):
        print(i)
    return await database.fetch_all(query)


@router.put('/products/', response_model=Product)
async def edit_product(id: int, new_product: ProductIn, products=None):
    for i in range(0, len(products)):
        if products[i].id == id:
            current_product = product[id - 1]
    if current_product:
        current_product.id = new_product.id
        current_product.name = new_product.name
        current_product.properties = new_product.properties
        current_product.price = new_product.price
    else:
        raise HTTPException(status_code=404, detail='Product not found')
    return current_product


@router.delete('/products/', response_model=Product)
async def delete_product(id: int, products=None):
    for i in range(0, len(products)):
        if products[i].id == id:
            products.remove(products[i])
            return {"message": "Product was deleted successfully"}
        raise HTTPException(status_code=404, detail='Product not found')