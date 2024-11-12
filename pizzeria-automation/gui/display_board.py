import tkinter as tk
from tkinter import ttk

class DisplayBoard:
    def __init__(self, root, update_queue):
        self.root = root
        self.update_queue = update_queue
        self.root.title("Order Status Board")
        self.tree = ttk.Treeview(root, columns=("Table", "Order", "Bot", "Status"), show="headings")
        self.tree.heading("Table", text="Table Number")
        self.tree.heading("Order", text="Order Number")
        self.tree.heading("Bot", text="Bot Number")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Start listening to the update_queue in the main thread
        self.listen_to_updates()

    def update_order_status(self, table_number, order_number, bot_id, status):
        """Update or insert an order status in the board."""
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[1] == order_number:
                self.tree.item(item, values=(table_number, order_number, bot_id, status))
                return
        # If order not found, insert new row
        self.tree.insert("", tk.END, values=(table_number, order_number, bot_id, status))

    def listen_to_updates(self):
        """Listen to update_queue for new status updates and update the display board."""
        try:
            while not self.update_queue.empty():
                table_number, order_number, bot_id, status = self.update_queue.get_nowait()
                self.update_order_status(table_number, order_number, bot_id, status)
        except:
            pass
        # Schedule next check for updates in the next event loop iteration
        self.root.after(100, self.listen_to_updates)
