# kiosk/order.py
import itertools
import time

class Order:
    def __init__(self, item, table_number, order_number):
        self.item = item
        self.table_number = table_number
        self.order_number = order_number  # Added order_number attribute
        self.status = "Pending"  # Default status
    
    def __repr__(self):
        return f"Order({self.item}, Table: {self.table_number}, Order#: {self.order_number}, Status: {self.status})"

