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

gpu1 = GPU("RTX 4080", 1000)
gpu_repository.save(gpu1)
cpu1 = CPU("i5 13600k", 250)
cpu_repository.save(cpu1)
ram1 = RAM("32gb DDR5", 150)
ram_repository.save(ram1)
motherboard1 = Motherboard("Z690", 300)
motherboard_repository.save(motherboard1)
psu1 = PSU("1000w", 300)
psu_repository.save(psu1)

gpu_repository.select_all()
cpu_repository.select_all()
ram_repository.select_all()
motherboard_repository.select_all()
psu_repository.select_all()

custom_pc1 = Custom_PC("High End Gaming PC", gpu1.price+cpu1.price+ram1.price+motherboard1.price+psu1.price, gpu1, cpu1, ram1, motherboard1, psu1)
custom_pc_repository.save(custom_pc1)

custom_pc_repository.select_all()