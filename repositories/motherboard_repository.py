from db.run_sql import run_sql

from models.gpu import GPU
from models.cpu import CPU
from models.ram import RAM
from models.motherboard import Motherboard
from models.psu import PSU
from models.custom_pc import Custom_PC

def save(motherboard):
    sql = "INSERT INTO motherboards (name, price) VALUES (%s, %s) RETURNING *"
    values = [motherboard.name, motherboard.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    motherboard.id = id
    return motherboard

def select_all():
    motherboards = []

    sql = "SELECT * FROM motherboards"
    results = run_sql(sql)

    for row in results:
        motherboard = Motherboard(row['name'], row['price'], row['id'] )
        motherboards.append(motherboard)
    return motherboards

def select(id):
    motherboard = None
    sql = "SELECT * FROM motherboards WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        motherboard = Motherboard(result['name'], result['price'], result['id'] )
    return motherboard