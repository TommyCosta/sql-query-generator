# SQL Query Generator
This program uses user input command line args to create and display the results of a SQL query within a simulated database.
It is inteneded to assist Technical Support agents troubleshoot databases more efficiently, without knowing how to write in SQL.


## Installation
Clone the repo with:
```bash
git clone https://github.com/TommyCosta/sql-query-generator.git
```

## Usage
To create a simulated database with realistic data points, run retailer_db_generator.py with:
```bash
python retailer_db_generator.py
```

To create a SQL query and see the results, run query_generator with arguments. 
```bash
python query_generator.py --itemId=1
```
Usable arguments:
--itemID (Filter by item ID.)
--itemState (Filter by item state.)
--stockCount (Filter by avaiable inventory count.)
--orderId (Filter by order ID)
--orderState (Filter by order state.)
--start (Start date of order placement.)
--end (End date of order placement.)

## Output Examples
![Alt text](https://github.com/TommyCosta/sql-query-generator/blob/main/example_output_1.png)
![Alt text](https://github.com/TommyCosta/sql-query-generator/blob/main/example_output_2.png)
