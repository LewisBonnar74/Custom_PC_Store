from flask import Flask, render_template, request, redirect
from flask import Blueprint
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
import repositories.custom_pc_repository as custom_pc_repository

custom_pc_blueprint = Blueprint("custom_pcs", __name__)

@custom_pc_blueprint.route("/custom_pcs")
def custom_pcs():
    custom_pcs = custom_pc_repository.select_all() 
    return render_template("custom_pcs/index.html", all_custom_pcs = custom_pcs)

@custom_pc_blueprint.route("/custom_pcs/create", methods=['GET'])
def new_task():
    gpus = gpu_repository.select_all()
    cpus = cpu_repository.select_all()
    rams = ram_repository.select_all()
    motherboards = motherboard_repository.select_all()
    psus = psu_repository.select_all()
    return render_template("custom_pcs/create.html", gpus = gpus, cpus = cpus, rams = rams, motherboards = motherboards, psus = psus)

@custom_pc_blueprint.route("/custom_pcs", methods=['POST'])
def create_new_pc():
    name = request.form['name']
    gpu_id = request.form['gpu']
    cpu_id = request.form['cpu']
    ram_id = request.form['ram']
    motherboard_id = request.form['motherboard']
    psu_id = request.form['psu']
    

    gpu = gpu_repository.select(gpu_id)
    cpu = cpu_repository.select(cpu_id)
    ram = ram_repository.select(ram_id)
    motherboard = motherboard_repository.select(motherboard_id)
    psu = psu_repository.select(psu_id)

    components = [gpu, cpu, ram, motherboard, psu]

    total_price = 0
    for component in components:
        total_price += component.price

    custom_pc = Custom_PC(name, total_price, gpu, cpu, ram, motherboard, psu)
    custom_pc_repository.save(custom_pc)
    return redirect('/custom_pcs')
    