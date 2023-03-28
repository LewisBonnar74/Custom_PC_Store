from db.run_sql import run_sql

from models.gpu import GPU
from models.cpu import CPU
from models.ram import RAM
from models.motherboard import Motherboard
from models.psu import PSU
from models.custom_pc import Custom_PC

def save(ram):
    sql = "INSERT INTO rams (name, price) VALUES (%s, %s) RETURNING *"
    values = [ram.name, ram.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    ram.id = id
    return ram

def select_all():
    all_rams = []

    sql = "SELECT * FROM rams"
    results = run_sql(sql)

    for row in results:
        ram = RAM(row['name'], row['price'], row['id'] )
        all_rams.append(ram)
    return all_rams

def select(id):
    ram = None
    sql = "SELECT * FROM rams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        ram = RAM(result['name'], result['price'], result['id'] )
    return ram

def delete_all():
    sql = "DELETE FROM rams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM rams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(ram):
    sql = "UPDATE rams SET (name, price) = (%s, %s) WHERE id = %s"
    values = [ram.name, ram.price, ram.id]
    run_sql(sql, values)
    