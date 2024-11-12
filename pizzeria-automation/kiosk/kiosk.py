# kiosk/kiosk.py
import random
import time
from queue import Queue
from .order import Order

def kiosk(order_queue: Queue):
    order_id = 1
    while True:
        table_number = random.randint(1, 9)  # Random table number from 1 to 9
        new_order = Order("Margherita", table_number, order_id)
        print(f"Kiosk: Placing order {new_order}")
        order_queue.put(new_order)
        order_id += 1
        time.sleep(random.uniform(2, 5))  # Random interval between orders
