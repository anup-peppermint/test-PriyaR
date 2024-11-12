Here is a combined `README.md` file for anup-peppermint/test-PriyaR  GitHub repository that includes all four questions:

```markdown
# Project: C, C++, Python, and Pizzeria Automation System

This repository contains solutions to various programming tasks, demonstrating concepts in C, C++, Python, and system design. It includes a union with bitfields in C, abstract classes and polymorphism in C++, email domain replacement in Python, and a pizzeria automation system.

## Table of Contents
- [Question 1: C - Union with Bitfields](#question-1-c---union-with-bitfields)
- [Question 2: C++ - Shape Drawing Example](#question-2-cpp---shape-drawing-example)
- [Question 3: Python - Email Domain Replacement](#question-3-python---email-domain-replacement)
- [Question 4: Pizzeria Automation System](#question-4-pizzeria-automation-system)

---

## Question 1: C - Union with Bitfields

This C program demonstrates the use of unions with bitfields. The program defines a structure with bitfields and shows how unions allow you to access the same memory in different formats.

### Key Concepts:
- **Bitfields**: Allocating a specific number of bits for each field in a structure.
- **Union**: A data structure where all members share the same memory.

### How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/anup-peppermint/test-PriyaR.git
   cd repository
   ```
2. Compile using GCC:
   ```bash
   gcc -o union_bitfields union_bitfields.c
   ```
3. Run the program:
   ```bash
   ./union_bitfields
   ```

---

## Question 2: C++ - Shape Drawing Example

This C++ program demonstrates the use of abstract classes, inheritance, and polymorphism. It defines an abstract class `Shape` with a pure virtual function `draw()`. The derived classes `Line` and `Circle` implement the `draw()` function.

### Features:
- **Abstract Class**: `Shape` contains a pure virtual function `draw()`.
- **Polymorphism**: `Line` and `Circle` override the `draw()` function.

### How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/anup-peppermint/test-PriyaR.git
   cd repository
   ```
2. Compile the code:
   ```bash
   g++ -o shapes shapes.cpp
   ```
3. Run the executable:
   ```bash
   ./shapes
   ```

---

## Question 3: Python - Email Domain Replacement

This Python script updates a list of email addresses by replacing the domain name `@zap.com` with `@ezap.org` for specific email IDs.

### How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/anup-peppermint/test-PriyaR.git
   cd repository
   ```
2. Run the Python script:
   ```bash
   python email_domain_replacement.py
   ```

### Example Output:
```
Updated email list:
john@ezap.org
jane@ezap.org
mike@ezap.org
sara@ezap.org
anna@ezap.org
```

---

## Question 4: Pizzeria Automation System

This project is a simulation of a pizzeria automation system where customers place orders through a kiosk, and delivery robots handle the preparation and delivery of orders.

### Features:
- **Kiosk for Order Placement**: Customers select a pizza, make payment, and are assigned a table number.
- **Order Management**: Handles the order flow from the order queue to cooking and delivery.
- **Cooking Robots**: Simulates pizza preparation.
- **Delivery Robots**: Delivers orders to customers' assigned tables.
- **GUI Visualization**: Displays real-time updates of bot movements and customer status.

### How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/anup-peppermint/test-PriyaR.git
   cd repository
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the simulation:
   ```bash
   python main.py
   ```

### Project Structure:
```bash
pizzeria-automation/
│
├── main.py                    # Entry point for the simulation
│
├── gui/                       
│   ├── pizzeria_gui.py        # GUI layout and handling of customer/robot movements
│   ├── display_board.py       # Display board for showing order statuses
│
├── kiosk/
│   ├── kiosk.py               # Simulates kiosk for order placement
│   ├── order.py               # Order class definition
│
├── navigation/
│   ├── navigator.py              
│
├── utils/
│   ├── logger.py               
│
├── order_management/
│   ├── order_manager.py       # Manages orders and their flow
│
├── cooking/
│   ├── cooking_robot.py       # Simulates the cooking process
│
└── delivery/
    ├── delivery_robot.py      # Handles delivery of orders by robots
```

---

## Troubleshooting:
- **GUI doesn’t open or crashes**: Ensure that `tkinter` is installed correctly.
- **Customer or bot movement issues**: Verify that the `move_customer_to_table` and `move_bot_to` methods are functioning.

---

```

This is combined `README.md` file organizes the four questions clearly with sections on how to run the respective programs.