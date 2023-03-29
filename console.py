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

custom_pc_repository.delete_all()
gpu_repository.delete_all()
cpu_repository.delete_all()
ram_repository.delete_all()
motherboard_repository.delete_all()
psu_repository.delete_all()

gpu1 = GPU("RTX 3060", 340)
gpu_repository.save(gpu1)

cpu1 = CPU("i5 13600k", 250)
cpu_repository.save(cpu1)

ram1 = RAM("16gb DDR5", 80)
ram_repository.save(ram1)

motherboard1 = Motherboard("Z690", 300)
motherboard_repository.save(motherboard1)

psu1 = PSU("1000w", 300)
psu_repository.save(psu1)

gpu2 = GPU('RTX 3070', 400)
gpu_repository.save(gpu2)

cpu2 = CPU("AMD 5600", 150)
cpu_repository.save(cpu2)

ram2 = RAM("16gb DDR4", 50)
ram_repository.save(ram2)

motherboard2 = Motherboard("B550", 90)
motherboard_repository.save(motherboard2)

psu2 = PSU("600W", 60)
psu_repository.save(psu2)

gpu3 = GPU("AMD 7900XT", 900)
gpu_repository.save(gpu3)

cpu3 = CPU("7950X3D", 600)
cpu_repository.save(cpu3)

ram3 = RAM("64gb DDR5", 300)
ram_repository.save(ram3)

motherboard3 = Motherboard("X570", 150)
motherboard_repository.save(motherboard3)

psu3 = PSU("850w", 150)
psu_repository.save(psu3)

gpu4 = GPU('RTX 4090', 1400)
gpu_repository.save(gpu4)

cpu4 = CPU("i7 13900k", 600)
cpu_repository.save(cpu4)

ram4 = RAM("64gb DDR4", 150)
ram_repository.save(ram4)

motherboard4 = Motherboard("B660", 90)
motherboard_repository.save(motherboard4)

psu4 = PSU("500W", 50)
psu_repository.save(psu4)

gpu_repository.select_all()
cpu_repository.select_all()
ram_repository.select_all()
motherboard_repository.select_all()
psu_repository.select_all()

prebuilt_pc1 = Custom_PC("High End Prebuilt", gpu4.price+cpu3.price+ram3.price+motherboard1.price+psu1.price, gpu4, cpu3, ram3, motherboard1, psu1)
custom_pc_repository.save(prebuilt_pc1)

prebuilt_pc2 = Custom_PC("Budget Prebuilt", gpu1.price+cpu2.price+ram2.price+motherboard2.price+psu4.price, gpu1, cpu2, ram2, motherboard2, psu4)
custom_pc_repository.save(prebuilt_pc2)



custom_pc_repository.select_all()