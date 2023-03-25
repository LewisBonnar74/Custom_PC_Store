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
    return render_template("custom_pcs/create.html", gpus = gpus, cpus = cpus, rams = rams, motherboards = motherboards, psus = psus, zip = zip)

# @custom_pc_blueprint.route("/custom_pcs" methods=['POST'])
# def create_new_pc():
#     name = request.form['name']
#     total_price = 
#     gpu =  request.form['gpu_id']
#     cpu =  request.form['cpu_id']
#     ram =  request.form['ram_id']
#     motherboard =  request.form['motherboard_id']
#     psu =  request.form['psu_id']
#     custom_pc = Custom_PC(name, total_price, )