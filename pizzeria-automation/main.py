# main.py

from queue import Queue
import threading
from tkinter import Tk
from gui.pizzeria_gui import PizzeriaGUI
from gui.display_board import DisplayBoard
from kiosk.kiosk import kiosk
from order_management.order_manager import order_manager
from cooking.cooking_robot import cooking_robot
from delivery.delivery_robot import delivery_robot

def main():
    # Create a queue for communication
    update_queue = Queue()

    # Initialize GUI components
    root = Tk()
    # Pass the update_queue to PizzeriaGUI
    pizzeria_gui = PizzeriaGUI(root, update_queue)

    # Create the display board, passing the update_queue
    display_root = Tk()
    display_board = DisplayBoard(display_root, update_queue)

    # Order queues
    order_queue = Queue()
    cooking_queue = Queue()
    delivery_queue = Queue()

    # Start the kiosk to simulate order generation
    threading.Thread(target=kiosk, args=(order_queue,), daemon=True).start()

    # Start order manager to move orders from order_queue to cooking_queue
    threading.Thread(target=order_manager, args=(order_queue, cooking_queue, update_queue), daemon=True).start()

    # Start the cooking robot
    threading.Thread(target=cooking_robot, args=(cooking_queue, delivery_queue, update_queue), daemon=True).start()

    # Start multiple delivery robots
    for bot_id in range(3):  # Example with 3 bots
        threading.Thread(target=delivery_robot, args=(delivery_queue, bot_id, update_queue), daemon=True).start()
        pizzeria_gui.add_bot(bot_id)

    # Start processing updates for bot movements
    pizzeria_gui.process_updates()  # Start the periodic update checking

    root.mainloop()

if __name__ == "__main__":
    main()
