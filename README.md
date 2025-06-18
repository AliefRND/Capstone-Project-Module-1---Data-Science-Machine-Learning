# Capstone-Project-Module-1---Data-Science-Machine-Learning
Made for Capstone Project Module 1 for Purwadhika. A python based application that allows users to Create, Read, Update or Delete data related to inventory management of a warehouse. 

# Python CRUD Application for Inventory Management of a Store

A **Python-based CRUD application** with a simple menu-driven interface that allows users to manage inventory using Create, Read, Update, and Delete operations.

---

## Business Understanding

This project caters to the **various industries** that keep track of inventory in a warehouse. It can be used in:

- Supermarkets (e.g., Indomaret, Alfamart)
- Grocery stores (e.g, Primo, HERO, Giant)
- Retail stores (e.g, clothing, electronics)
- E-commerce warehouses for online resellers (e.g, Tokopedia, Shopee)
- Manufacturing plants and factories (e.g, raw mining materials and goods)
- Logistics and distribution centers
- Automotive parts suppliers 

**Stock data** plays an important role in any business that handles physical goods—for example, in supermarkets, most items go through a warehouse system first. This setup enables supermarkets to:

- Buy in bulk (saving cost from distributors)
- Store stock before shelving by accurately tracking supply (allowing restocking at appropriate times)
- Rotate and manage items (especially goods with expiration dates)
- Perform product performance analysis

If a single distribution center may serve multiple branches of supermarkets, having accurate inventory data is **important for operational efficiency.**

### Benefits
- Effective Storage and space management for supermarkets and the warehouse  
- Save on different costs (such as opportunity costs, delivery costs, storage costs, etc)
- Improved data accuracy and consistency when moving items in and out of the warehouse

---
---

## Target Users

This application is designed for multiple roles, including:

- **Inventory Managers** – Monitor stock levels, product data, and restocking needs  
- **Warehouse Staff** – Record incoming and outgoing stock  
- **Procurement Officers** – Track product availability before placing new orders  
- **Store Managers** – Oversee product performance and identify best- or worst-performing products  
- **Logistics Coordinators** – Ensure efficient movement of products between the warehouses, suppliers, and supermarkets  
- **Inventory Analysts** – Analyze supply and demand to report on product performance  
- **Supply Chain Managers** – Coordinate between warehouses, suppliers, and supermarkets

It helps them **buy, ship, and sell** items according to current inventory data.


---

## 🔧 Features

### Create
- Add new **Stock** entries with essential details such as:
  - Item ID
  - Price
  - Expiration Date
- ID validation to avoid duplicate entries.

###  Read
- Search and retrieve inventory records based on:
  - Item ID
  - Item Name
- View all items in a **user-friendly table format** (using tabulate).

###  Update
- Modify existing inventory data, such as:
  - Price updates
  - Stock quantity changes
- User confirmation for each update.

###  Delete
- Remove records (e.g for discontinued products).
- Includes a **Recycle Bin** feature (soft delete).
- Option to restore or permanently delete items.

- ---

##  Inventory Item Data Structure

Each item in the inventory contains the following details:

| Item Detail       | Type     | Description                                   |
|-------------------|----------|-----------------------------------------------|
| item_id           | String   | Unique identifier (SKU-style) for each item   |
| item_name         | String   | Name of the product                          |
| stock_quantity    | Integer  | Quantity currently in stock                  |
| price             | Float    | Selling price per unit                       |
| expiration_date   | Date     | Product expiry date (useful for perishables) |

---

##  How to Run This Program

### Requirements
- Python 3.10 or higher
- Python package: `tabulate`

### Setup Steps
1. Open your terminal or command prompt.
2. Navigate to the folder containing the `.py` file using `cd`.
3. Install the required package:
   pip install tabulate
