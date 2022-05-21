from connect import connectDB

def add_prod(id, name, price, description):
    conn = connectDB()
    with conn.cursor() as cursor:
        cursor.execute('insert into products(id, name, price, description) values (%s,%s,%s,%s)', (id, name, price, description))
    conn.commit()
    conn.close()

def list_prod():
    conn = connectDB()
    products = []
    with conn.cursor() as cursor:
        cursor.execute('select id, name, price, description from products')
        products = cursor.fetchall()
    conn.close()
    return products