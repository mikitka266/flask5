from fastapi import APIRouter

from db import orders

router = APIRouter()



@router.post('/order', response_model = OrderIn)
async def create_order(order: OrderIn):
    orders.insert().values(id_product=order.id_product,
                          date_order=order.date_order,
                          status=order.status)
    return order


@router.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    for i in await database.fetch_all(query):
        print(i)
    return await database.fetch_all(query)



@router.put('/orders/', response_model=Order)
async def edit_order(id: int, new_order: OrderIn, orders=None):
    for i in range(0, len(orders)):
        if orders[i].id == id:
            current_order = orders[id - 1]
    if current_order:
        current_order.id = new_order.id
        current_order.date_order = new_order.date_order
        current_order.status= new_order.status
    else:
        raise HTTPException(status_code=404, detail='Order not found')
    return current_product


@router.delete('/orders/', response_model=Order)
async def delete_order(id: int, orders=None):
    for i in range(0, len(orders)):
        if orders[i].id == id:
            orders.remove(orders[i])
            return {"message": "Order was deleted successfully"}
        raise HTTPException(status_code=404, detail='Order not found')