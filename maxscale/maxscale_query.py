# Name: Abiyu Gebremeskel
# Email: atgebremeskel@student.rtc.edu
# Due date: June 18, 2024 Class:
# CNE 370 Intro to  Virtualization
# Description: This script connects to a MaxScale instance and performs various queries to fetch data
# from MariaDB databases.

import mysql.connector


def connect_to_db():
    # Establish a connection to the MariaDB database via MaxScale
    return mysql.connector.connect(user="maxuser", password="maxpwd", host="10.0.0.218", port=4000)


def fetch_largest_zipcode(cursor):
    # Fetch and print the largest zipcode from zipcodes_one
    cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;")
    result = cursor.fetchone()
    print('The largest zipcode in zipcodes_one:', result[0])


def fetch_zipcodes_in_KY(cursor):
    # Fetch and print all zipcodes where the state is KY (Kentucky)
    cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State = 'KY';")
    results = cursor.fetchall()
    print('All zipcodes where state = KY:')
    for result in results:
        print(result[0])


def fetch_zipcodes_in_range(cursor):
    # Fetch and print all zipcodes between 40000 and 41000
    cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;")
    results = cursor.fetchall()
    print('All zipcodes between 40000 and 41000:')
    for result in results:
        print(result[0])


def fetch_total_wages_PA(cursor):
    # Fetch and print the TotalWages column for records where the state is PA (Pennsylvania)
    cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'PA';")
    results = cursor.fetchall()
    print('The TotalWages column where state = PA:')
    for result in results:
        print(result[0])


def main():
    # Main function to connect to the database and execute the queries
    db = connect_to_db()
    cursor = db.cursor()

    fetch_largest_zipcode(cursor)
    fetch_zipcodes_in_KY(cursor)
    fetch_zipcodes_in_range(cursor)
    fetch_total_wages_PA(cursor)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
