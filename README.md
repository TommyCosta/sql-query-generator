# SQL Query Generator
This Python CLI tool uses user input command line args to create and display the results of a SQLite query within a simulated database.
It is intended to assist Technical Support agents troubleshoot databases more efficiently, without knowing how to write in SQL. Formatting has been included so the displayed results are easeier to comprehend quickly.

## Technologies
Python 3.x, SQLite, argparse

## Installation
1. Ensure Python 3.x is installed.
2. Clone the repository with:
```bash
git clone https://github.com/TommyCosta/sql-query-generator.git
```

## Usage
1. Generate the database:
```bash
python retailer_db_generator.py
```

2. Run query_generator with arguments:
```bash
python query_generator.py --itemId <ID> --itemState <STATE>
```
Usable arguments:
* --itemId <ID> – Filter by Item ID (integer).
* --itemState <STATE> – Filter by Item State (e.g. "ForSale").
* --stockCount <N> – Filter by available inventory count.
* --orderId <ID> - Filter by order ID (integer).
* --orderState <STATE> - Filter by order state (e.g. "Delivered").
* --start <DATE> - Start date of order placement(e.g. "2025-06-01").
* --end <DATE> - End date of order placement (e.g. "2025-06-30").
* --db <DB> - Database to query (default is retailer_logs.db).
* --help - For additional help and options.


## Output Examples
1. Querying by an item state and stock count. In a real life scenarion, a support agent might use this to find which products are at risk of becoming out of stock:
   
![Alt text](https://github.com/TommyCosta/sql-query-generator/blob/main/example_output_1.png)

2. Querying by order state and date range. In a real life scenario, a support agent could use this to figure out which orders are still eing shipped that were ordered during the specified daterange.
   
![Alt text](https://github.com/TommyCosta/sql-query-generator/blob/main/example_output_2.png)
