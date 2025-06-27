import sqlite3, random, datetime

itemStates = ["NotForSale", "InReview", "ForSale", "Ordered", "Fulfilled", "Delivered"]
orderStates = ["Cart", "Paid", "Processed", "InTransit", "Delivered"]

connection = sqlite3.connect("retailer_logs.db")
cursor = connection.cursor()
# Optional lines to clear existing retailer_logs.db
cursor.execute("DROP TABLE IF EXISTS orders;")
cursor.execute("DROP TABLE IF EXISTS items;")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        itemId INTEGER PRIMARY KEY AUTOINCREMENT,
        itemState TEXT,
        stockCount INTEGER)
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        orderId INTEGER PRIMARY KEY AUTOINCREMENT,
        itemId INTEGER,
        orderState TEXT,
        orderTime DATETIME,
        FOREIGN KEY(itemId) REFERENCES items(itemId))
""")

for i in range(5000):
    stockCount = random.randint(0, 25)
    if stockCount == 0:
        itemState = "OutOfStock"
    else:
        itemState = random.choice(itemStates)
    cursor.execute("INSERT INTO items (itemState, stockCount) VALUES (?, ?)", (itemState, stockCount))
    itemId = cursor.lastrowid

    if itemState in ("Ordered", "Fulfilled", "Delivered"):
        orderState = random.choice(orderStates)
        orderDatetime = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 60*60*24*90))
        orderTime = orderDatetime.isoformat(" ")
        cursor.execute("INSERT INTO orders (itemId, orderState, orderTime) VALUES (?, ?, ?)", (itemId, orderState, orderTime))

connection.commit()
connection.close()