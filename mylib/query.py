"""Query the database"""

import sqlite3


def query():
    # Connect and query DB

    print("Average of count_products:")
    for row in cursor.fetchall():
        print(row[0])

    print("\nSum of count_products:")
    for row in cursor.fetchall():
        print(row[0])

    # Close connection

    return "Success"


print(query())
