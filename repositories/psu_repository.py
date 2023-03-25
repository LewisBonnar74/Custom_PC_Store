from db.run_sql import run_sql

from models.gpu import GPU
from models.cpu import CPU
from models.ram import RAM
from models.motherboard import Motherboard
from models.psu import PSU
from models.custom_pc import Custom_PC

def save(psu):
    sql = "INSERT INTO psus (name, price) VALUES (%s, %s) RETURNING *"
    values = [psu.name, psu.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    psu.id = id
    return psu
    
def select_all():
    psus = []

    sql = "SELECT * FROM psus"
    results = run_sql(sql)

    for row in results:
        psu = PSU(row['name'], row['price'], row['id'] )
        psus.append(psu)
    return psus

def select(id):
    psu = None
    sql = "SELECT * FROM psus WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        psu = PSU(result['name'], result['price'], result['id'] )
    return psu