import re
from finder import get_dota_path
import os
import argparse
parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('-d',"--drive", type=str, help='disk / folder where the dota is located')
parser.add_argument('-c',"--cfg_path", type=str, help='the path from the dota 2 beta folder to the autoexec file' , default = "game\dota\cfg\\autoexec.cfg")
parser.add_argument('-k',"--key", type=str, help='which button to replace the attack button with' , default = "s")

args = parser.parse_args()
dota_drive = args.drive
dota_cfg_template_path = args.cfg_path
key = args.key

dota_path = get_dota_path("E:")
cfg_path = os.path.join(dota_path,dota_cfg_template_path)

if not os.path.exists(cfg_path):
    parrent_dir = os.path.dirname(cfg_path)
    if not parrent_dir:
        raise OSError("Неправильный путь к конфигу")
    else:
        bind_cmd = f'bind "{key}" "dota_player_units_auto_attack 1;mc_attack"'  # не нашел как из конфига достать уже назначенную клавишу , в таком случае атака будет на обе кнопки
        cfg_file = open(cfg_path, "w")
        cfg_file.write(bind_cmd)
        cfg_file.close()
else:
    with open(cfg_path, "r") as file:
        content = file.read()
        
    splited_cmds = content.split("\n")

    for i in range(len(splited_cmds)):
        cmd = splited_cmds[i]
        if "mc_attack" in cmd:
            pattern = '".{0,1}"'
            splited_cmds[i] = re.sub(pattern, f'"{key}"', cmd)
            unbind = re.search(pattern, cmd).group()
            if "unbind" not in splited_cmds[i+1]:
                splited_cmds[i] += "\nunbind "
                splited_cmds[i] += unbind
            else:
                splited_cmds[i+1] = re.sub(pattern, f'{unbind}',splited_cmds[i+1] )
    cfg_file = open(cfg_path, "w")
    cfg_file.write("\n".join(splited_cmds))
    cfg_file.close()
  

from pywinauto import Application

Application().start('"C:\\Program Files (x86)\Steam\\steam.exe"')
