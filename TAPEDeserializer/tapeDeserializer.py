import struct
import os
import json
import pathlib
from tkinter import Tk, filedialog
from utils.StringID import *
from utils.Tape import getClipNameFromBytes

# Inicializa o Tkinter (para usar o seletor de arquivos)
openFile = Tk()
openFile.title('')

# Procura o arquivo TAPE
dtapefile = filedialog.askopenfilename(
    initialdir=str(pathlib.Path().absolute()),
    title="Select your TAPE file",
    filetypes=[("Tape (.tape.ckd)", "*.tape.ckd")]
)

from utils.Classes.TranslationClip import *
from utils.Classes.AlphaClip import *
from utils.Classes.SizeClip import *
from utils.Classes.FXClip import *
from utils.Classes.SoundSetClip import *
from utils.Classes.RotationClip import *
from utils.Classes.ProportionClip import *
from utils.Classes.TapeLauncherClip import *
from utils.Classes.MaterialGraphicDiffuseColorClip import *
from utils.Classes.ColorClip import *
from utils.Classes.MaterialGraphicDiffuseAlphaClip import *
from utils.Classes.SpawnActorClip import *

# Inicializa o dicionário de saída
tape_data = {
    "__class": "Tape",
    "Clips": [],
    "ActorPaths": [],
    "TapeClock": 2,
    "TapeBarCount": 1,
    "FreeResourcesAfterPlay": 0,
    "MapName": "animations"
}

# Abre e lê o arquivo
with open(dtapefile, "rb") as f:
    # Header
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)  # Tape
    byte = f.read(4)  # timeline ver
    timeline_ver = struct.unpack('>I', byte)[0]
    
    # Infos
    byte = f.read(4)
    entries = struct.unpack('>I', byte)[0]
    total = entries
    # Infos

    # Processa cada entrada no arquivo TAPE
    for x in range(entries):
        byte = f.read(4)  # Pegando a classe :0
        class_get_hex = byte.hex().upper()  # Converte os bytes para hexadecimal e garante que seja em maiúsculas
        
        clip_name = getClipNameFromBytes(byte)  # Passa os bytes diretamente
        
        if clip_name == "TranslationClip":
            print(f"{clip_name} encontrada!")
            clip_instance = TranslationClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)
        
        elif clip_name == "AlphaClip":
            print(f"{clip_name} encontrada!")
            clip_instance = AlphaClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)
            
        elif clip_name == "SizeClip":
            print(f"{clip_name} encontrada!")
            clip_instance = SizeClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)
            
        elif clip_name == "FXClip":
            print(f"{clip_name} encontrada!")
            clip_instance = FXClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)

        elif clip_name == "SoundSetClip":
            print(f"{clip_name} encontrada!")
            clip_instance = SoundSetClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)

        elif clip_name == "RotationClip":
            print(f"{clip_name} encontrada!")
            clip_instance = RotationClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)

        elif clip_name == "ProportionClip":
            print(f"{clip_name} encontrada!")
            clip_instance = ProportionClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)

        elif clip_name == "TapeLauncherClip":
            print(f"{clip_name} encontrada!")
            clip_instance = TapeLauncherClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)
            
        elif clip_name == "MaterialGraphicDiffuseColorClip":
            print(f"{clip_name} encontrada!")
            clip_instance = MaterialGraphicDiffuseColorClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)

        elif clip_name == "MaterialGraphicDiffuseAlphaClip":
            print(f"{clip_name} encontrada!")
            clip_instance = MaterialGraphicDiffuseAlphaClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)

        elif clip_name == "ColorClip":
            print(f"{clip_name} encontrada!")
            clip_instance = ColorClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)
            
        elif clip_name == "SpawnActorClip":
            print(f"{clip_name} encontrada!")
            clip_instance = SpawnActorClip(f)
            clip_data = clip_instance.Deserialize()
            tape_data["Clips"].append(clip_data)
            
        else:
            print("Classe não implementada " + clip_name)
            print("Bytes da classe: " + class_get_hex)
    
    # Voltar 16 bytes
    f.seek(-16, 1)
    # Ler novamente o byte que foi lido por último
    byte = f.read(24)
    byte = f.read(4)
    
    actorpath_len = struct.unpack('>I', byte)[0]
    
    try:
        for ActorPaths in range(actorpath_len):
            byte = f.read(4)
            byte = f.read(4)
            byte = f.read(4)
            length = struct.unpack('>I', byte)[0]
            # Leitura dos bytes do texto
            text_bytes = f.read(length)

            # Decodificação dos bytes como string
            text_string = text_bytes.decode('utf-8')  # Ou a codificação apropriada
            tape_data["ActorPaths"].append(text_string)
            byte = f.read(4)
    except:
        pass

# Extrai o nome do arquivo original sem extensão
tape_filename = os.path.splitext(os.path.basename(dtapefile))[0]

# Garante que o diretório de saída exista
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Escreve o dicionário no arquivo como JSON
output_path = os.path.join(output_dir, f"{tape_filename}.ckd")
with open(output_path, "w") as arq:
    json.dump(tape_data, arq, indent=4)

# Destrói o Tkinter
openFile.destroy()
