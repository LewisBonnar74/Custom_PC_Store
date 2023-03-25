from db.run_sql import run_sql

from models.gpu import GPU
from models.cpu import CPU
from models.ram import RAM
from models.motherboard import Motherboard
from models.psu import PSU
from models.custom_pc import Custom_PC

def save(cpu):
    sql = "INSERT INTO cpus (name, price) VALUES (%s, %s) RETURNING *"
    values = [cpu.name, cpu.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    cpu.id = id
    return cpu

def select_all():
    cpus = []

    sql = "SELECT * FROM cpus"
    results = run_sql(sql)

    for row in results:
        cpu = CPU(row['name'], row['price'], row['id'] )
        cpus.append(cpu)
    return cpus

def select(id):
    cpu = None
    sql = "SELECT * FROM cpus WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        cpu = CPU(result['name'], result['price'], result['id'] )
    return cpu