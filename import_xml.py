import xmltodict
import psycopg2

from psycopg2 import Error


try:
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
        database="gameshop",
    )
    connection.autocommit = True
    cursor = connection.cursor()

    with open("shop.xml") as fd:
        obj = xmltodict.parse(fd.read())

    insert_query = """INSERT INTO games_product (title, price, description, category, image_url) VALUES (%s, %s, %s, %s, %s)"""

    for p in obj["SHOP"]["SHOPITEM"]:
        try:
            product_data = (
                p["PRODUCT"],
                p["PRICE_VAT"],
                p["DESCRIPTION"],
                p["CATEGORYTEXT"],
                p["IMGURL"],
            )
            cursor.execute(insert_query, product_data)
        except KeyError:
            continue

    print("Product data were successfully inserted into database.")

    cursor.close()
    connection.close()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
