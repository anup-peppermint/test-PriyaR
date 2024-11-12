import tkinter as tk
from queue import Queue
import time
import threading

class PizzeriaGUI:
    def __init__(self, root, update_queue):
        self.root = root
        self.update_queue = update_queue
        self.root.title("Pizzeria Automation Simulation")
        
        # Set up the canvas for the pizza scene
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # Draw the counter and tables
        self.counter = self.canvas.create_rectangle(50, 50, 100, 100, fill="blue")
        self.canvas.create_text(75, 75, text="Counter", fill="white")

        self.tables = []
        table_positions = [(200, 100), (400, 100), (600, 100), 
                           (200, 300), (400, 300), (600, 300),
                           (200, 500), (400, 500), (600, 500)]
        for i, pos in enumerate(table_positions, start=1):
            table = self.canvas.create_oval(pos[0], pos[1], pos[0]+40, pos[1]+40, fill="orange")
            self.canvas.create_text(pos[0] + 20, pos[1] + 20, text=f"Table {i}", fill="black")
            self.tables.append((table, pos))

        self.bots = {}
        self.bot_positions = {}
        self.bot_colors = ["red", "green", "purple", "yellow"]

        # Start thread to update bot positions based on the queue
        threading.Thread(target=self.process_updates, daemon=True).start()

    def add_bot(self, bot_id):
        color = self.bot_colors[bot_id % len(self.bot_colors)]
        bot = self.canvas.create_rectangle(60, 60, 90, 90, fill=color)
        self.bots[bot_id] = bot
        self.bot_positions[bot_id] = (75, 75)

    def move_bot_to(self, bot_id, x, y):
        """Move the bot to the specified (x, y) position."""
        current_x, current_y = self.bot_positions[bot_id]
        step_size = 5

        # Move the bot incrementally
        while abs(current_x - x) > step_size or abs(current_y - y) > step_size:
            if current_x < x:
                current_x += step_size
            elif current_x > x:
                current_x -= step_size

            if current_y < y:
                current_y += step_size
            elif current_y > y:
                current_y -= step_size

            self.canvas.coords(self.bots[bot_id], current_x-15, current_y-15, current_x+15, current_y+15)
            self.root.update()
            time.sleep(0.05)  # Delay for smooth movement

        self.bot_positions[bot_id] = (current_x, current_y)

    def process_updates(self):
        while True:
            while not self.update_queue.empty():
                update = self.update_queue.get()
                if len(update) == 3:
                    bot_id, x, y = update
                    self.move_bot_to(bot_id, x, y)
                else:
                    table_number, order_number, bot_id, status = update
                    # Add code for display updates if required
            time.sleep(0.1)
