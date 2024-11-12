# order_management/order_manager.py
import time
from queue import Queue

def order_manager(order_queue: Queue, cooking_queue: Queue, update_queue: Queue):
    while True:
        if not order_queue.empty():
            order = order_queue.get()
            order.status = "Received"
            print(f"Order Management: Processing {order}")
            update_queue.put((order.table_number, order.order_number, None, "Received"))  # Update status to Received
            time.sleep(1)  # Processing delay
            cooking_queue.put(order)
