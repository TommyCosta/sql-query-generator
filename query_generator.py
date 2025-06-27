import sqlite3, argparse

def build_query(args):
    base_query = "SELECT items.itemId, items.itemState, items.stockCount, orders.orderId, orders.orderState, orders.orderTime FROM items LEFT JOIN orders ON items.itemId = orders.itemId WHERE 1=1"
    params = []

    if args.itemId:
        base_query += " AND itemId = ?"
        params.append(args.itemId)
    if args.itemState:
        base_query += " AND itemState = ?"
        params.append(args.itemState)
    if args.stockCount:
        base_query += " AND stockCount = ?"
        params.append(args.stockCount)
    if args.orderId:
        base_query += " AND orderId = ?"
        params.append(args.orderId)
    if args.orderState:
        base_query += " AND orderState = ?"
        params.append(args.orderState)
    if args.start:
        base_query += " AND orderTime >= ?"
        params.append(args.start)
    if args.end:
        base_query += " AND orderTime <= ?"
        params.append(args.end)

    return base_query, params

def run_query(db_path, query, params):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    connection.close()
    return results

def print_results(results):
    if not results:
        print("No matching logs found.")
        return
    else:
        headers = ["Item ID", "Item State", "Stock Count", "Order ID", "Order State", "Order Time"]
        string_rows = [[str(cell) for cell in row] for row in results]
        all_rows = [headers] + string_rows
        column_widths = []
        for column_index in range(len(headers)):
            max_width = max(len(r[column_index]) for r in all_rows)
            column_widths.append(max_width)
        frmt = " | ".join(f"{{:<{w}}}" for w in column_widths)
        print(frmt.format(*headers))
        seperator = "-".join("-" * w for w in column_widths)
        print(seperator)
        for r in string_rows:
            print(frmt.format(*r))

def main():
    parser = argparse.ArgumentParser(description="Query logs from retailer_logs.db")
    parser.add_argument("--db", default="retailer_logs.db", help="Path to SQLite database file (default: retailer_logs.db)")
    parser.add_argument("--itemId", help="Filter by item ID.")
    parser.add_argument("--itemState", help="Filter by item state.")
    parser.add_argument("--stockCount", help="Filter by available inventory count.")
    parser.add_argument("--orderId", help="Filter by order ID.")
    parser.add_argument("--orderState", help="Filter by order state.")
    parser.add_argument("--start", help="Start date (e.g., 2025-05-01).")
    parser.add_argument("--end", help="End date (e.g., 2025-05-31).")

    args = parser.parse_args()
    query, params = build_query(args)
    results = run_query(args.db, query, params)
    print_results(results)

if __name__ == "__main__":
    main()