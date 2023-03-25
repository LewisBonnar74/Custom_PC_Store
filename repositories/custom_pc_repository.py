from db.run_sql import run_sql

from models.gpu import GPU
from models.cpu import CPU
from models.ram import RAM
from models.motherboard import Motherboard
from models.psu import PSU
from models.custom_pc import Custom_PC
import repositories.gpu_repository as gpu_repository
import repositories.cpu_repository as cpu_repository
import repositories.ram_repository as ram_repository
import repositories.motherboard_repository as motherboard_repository
import repositories.psu_repository as psu_repository

def save(custom_pc):
    sql = "INSERT INTO custom_pcs (name, total_price, gpu_id, cpu_id, ram_id, motherboard_id, psu_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [custom_pc.name, custom_pc.total_price, custom_pc.gpu.id, custom_pc.cpu.id, custom_pc.ram.id, custom_pc.motherboard.id, custom_pc.psu.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    custom_pc.id = id
    return custom_pc

def select_all():
    custom_pcs = []

    sql = "SELECT * FROM custom_pcs"
    results = run_sql(sql)

    for row in results:
        gpu = gpu_repository.select(row['gpu_id'])
        cpu = cpu_repository.select(row['cpu_id'])
        ram = ram_repository.select(row['ram_id'])
        motherboard = motherboard_repository.select(row['motherboard_id'])
        psu = psu_repository.select(row['psu_id'])
        custom_pc = Custom_PC(row['name'], row['total_price'], gpu, cpu, ram, motherboard, psu, row['id'] )
        custom_pcs.append(custom_pc)
    return custom_pcs

def select(id):
    custom_pc = None
    sql = "SELECT * FROM custom_pcs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        gpu = gpu_repository.select(result['gpu_id'])
        cpu = cpu_repository.select(result['cpu_id'])
        ram = ram_repository.select(result['ram_id'])
        motherboard = motherboard_repository.select(result['motherboard_id'])
        psu = psu_repository.select(result['psu_id'])
        custom_pc = Custom_PC(result['name'], result['total_price'], gpu, cpu, ram, motherboard, psu, result['id'] )
    return custom_pc