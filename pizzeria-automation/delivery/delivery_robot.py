import time
import random
from queue import Queue

def move_bot(bot_id, update_queue):
    """Simulate bot movement and update the display board"""
    bot_position = (0, 0)  # Initial position of the bot
    while True:
        # Simulate bot movement (moving randomly for this example)
        bot_position = (bot_position[0] + random.randint(-1, 1), bot_position[1] + random.randint(-1, 1))
        
        # Update the bot's status and position
        status = f"Bot {bot_id} at {bot_position}"
        print(status)
        
        # Update the display board (this can be adapted to reflect the actual status)
        update_queue.put((None, None, bot_id, status))  # Assuming bot_id and status are relevant
        
        # Sleep to simulate time between movements
        time.sleep(1)


def delivery_robot(delivery_queue: Queue, bot_id: int, update_queue: Queue):
    while True:
        if not delivery_queue.empty():
            order = delivery_queue.get()  # Get the next order for delivery
            order.status = "Delivering"
            print(f"Delivery Robot {bot_id}: Delivering {order} to Table {order.table_number}")
            update_queue.put((order.table_number, order.order_number, bot_id, "Delivering"))

            # Move to the table where the order needs to be delivered
            destination = order.table_number
            table_positions = {
                1: (200, 100), 2: (400, 100), 3: (600, 100),
                4: (200, 300), 5: (400, 300), 6: (600, 300),
                7: (200, 500), 8: (400, 500), 9: (600, 500)
            }
            x, y = table_positions[destination]

            # Move bot to destination table coordinates
            update_queue.put((bot_id, x, y))  # Update GUI with bot movement
            time.sleep(3)  # Simulate travel time

            # Mark the order as delivered
            order.status = "Delivered"
            print(f"Delivery Robot {bot_id}: {order} has been delivered")
            update_queue.put((order.table_number, order.order_number, bot_id, "Delivered"))