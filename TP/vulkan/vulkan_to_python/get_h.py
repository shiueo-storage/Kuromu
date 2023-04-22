import os
import shutil

path = "./khronos_vulkan_headers"
h_files = os.listdir(path)
h_files = [file for file in h_files if file.endswith(".h")]

for file in h_files:
    shutil.copy(os.path.join(path, file), os.path.join("vulkan_include", file))
