import os
import re
from tqdm import tqdm 
import argparse


def find(name, path):
    for root, dirs, files in tqdm(os.walk(path)):
        if name in files or name in dirs:
            return os.path.join(root, name)
def get_dota_path(dota_drive):
    if dota_drive is None:
        drives = re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)
        for drive in drives:
            print(f"Ищу папку с дотой на диске {drive}")
            res = find("dota 2 beta", drive)
            if res != None:
                return res
        return None
    else:
        res = find("dota 2 beta", dota_drive)
        if res != None:
            return res
        else:
            return None
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Videos to images')
    parser.add_argument('-d',"--drive", type=str, help='disk / folder where the dota is located')
    args = parser.parse_args()
    dota_drive = args.drive
    print(get_dota_path(dota_drive))