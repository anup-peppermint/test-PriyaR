# cooking/cooking_robot.py
import time
from queue import Queue

def cooking_robot(cooking_queue: Queue, delivery_queue: Queue, update_queue: Queue):
    while True:
        if not cooking_queue.empty():
            order = cooking_queue.get()
            order.status = "Cooking"
            print(f"Cooking Robot: Cooking {order}")
            update_queue.put((order.table_number, order.order_number, None, "Cooking"))  # Update status to Cooking
            time.sleep(5)  # Simulate cooking time
            order.status = "Ready"
            print(f"Cooking Robot: {order} is ready")
            update_queue.put((order.table_number, order.order_number, None, "Ready"))  # Update status to Ready
            delivery_queue.put(order)
