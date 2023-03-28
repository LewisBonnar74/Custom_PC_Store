from db.run_sql import run_sql

from models.gpu import GPU
from models.cpu import CPU
from models.ram import RAM
from models.motherboard import Motherboard
from models.psu import PSU
from models.custom_pc import Custom_PC

def save(gpu):
    sql = "INSERT INTO gpus (name, price) VALUES (%s, %s) RETURNING *"
    values = [gpu.name, gpu.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    gpu.id = id
    return gpu

def select_all():
    gpus = []

    sql = "SELECT * FROM gpus"
    results = run_sql(sql)

    for row in results:
        gpu = GPU(row['name'], row['price'], row['id'] )
        gpus.append(gpu)
    return gpus

def select(id):
    gpu = None
    sql = "SELECT * FROM gpus WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        gpu = GPU(result['name'], result['price'], result['id'] )
    return gpu

def delete_all():
    sql = "DELETE FROM gpus"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gpus WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(gpu):
    sql = "UPDATE gpus SET (name, price) = (%s, %s) WHERE id = %s"
    values = [gpu.name, gpu.price, gpu.id]
    run_sql(sql, values)
    