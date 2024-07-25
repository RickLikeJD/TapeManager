import struct
from utils.Classes.BezierCurveFloat import BezierCurveFloat  # Importe corrigido
from utils.Tape import *
from utils.StringID import *

class SpawnActorClip:
    def __init__(self, f):
           self.f = f
           
    def str_handle(self):
        # Leitura do comprimento do texto
        byte = self.f.read(4)
        length = struct.unpack('>I', byte)[0]

        # Leitura dos bytes do texto
        text_bytes = self.f.read(length)

        # Decodificação dos bytes como string
        text_string = text_bytes.decode('utf-8')  # Ou a codificação apropriada

        return text_string

    def Deserialize(self):
    
        SpawnPosition = []
        
        byte = self.f.read(4) # 00000000
        
        byte = self.f.read(4) # ID
        id_entry = struct.unpack('>I', byte)[0]
        
        byte = self.f.read(4) # TrackId
        tid_entry = struct.unpack('>I', byte)[0]
        
        byte = self.f.read(4) # IsActive
        isactive_entry = struct.unpack('>I', byte)[0]
        
        byte = self.f.read(4) # StartTime
        st_entry = struct.unpack('>I', byte)[0]
        
        byte = self.f.read(4) # Duration
        d_entry = struct.unpack('>I', byte)[0]
        
        # Handling with names
        actorpath_file = self.str_handle()
        
        # Handling with directory
        actorpath_directory = self.str_handle()
        
        byte = self.f.read(4) # skip UbiArt Framework CRC32
        byte = self.f.read(4) # skip 00
        
        # Handling with names
        actorname_name = self.str_handle()
        
        for _ in range(3):
            byte = self.f.read(4) # SpawnPosition
            spawnposition_entry = struct.unpack('>f', byte)[0]
            SpawnPosition.append(spawnposition_entry)
        
        byte = self.f.read(4) # ParentActor
        parentactor_entry = struct.unpack('>I', byte)[0]

        clip_data = {
            "__class": "SpawnActorClip",
            "Id": id_entry,
            "TrackId": tid_entry,
            "IsActive": isactive_entry,
            "StartTime": st_entry,
            "Duration": d_entry,
            "ActorPath": actorpath_directory + actorpath_file,
            "ActorName": actorname_name,
            "SpawnPosition": SpawnPosition,
            "ParentActor": 0
        }
        byte = self.f.read(4) # skip 00
        byte = self.f.read(4) # skip 00
        byte = self.f.read(4) # skip 00
        
        return clip_data