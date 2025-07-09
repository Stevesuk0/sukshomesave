import os


for i in os.listdir():
    if i.endswith('.dat_old'):
        os.remove(i)