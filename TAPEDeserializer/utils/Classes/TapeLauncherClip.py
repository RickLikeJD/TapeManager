import struct
from utils.Classes.BezierCurveFloat import BezierCurveFloat  # Importe corrigido
from utils.Tape import *

class TapeLauncherClip:
    def __init__(self, f):
        self.f = f
    
    def Deserialize(self):
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
        
        byte = self.f.read(4) # 00000000

        byte = self.f.read(4)  # Actor Len
        entry_actor_len = struct.unpack('>I', byte)[0]
        actindices_total = entry_actor_len

        actor_indices = []
        for actor in range(actindices_total):
            byte = self.f.read(4)  # ActorIndices
            entry_actorindices = struct.unpack('>I', byte)[0]
            actor_indices.append(entry_actorindices)

        byte = self.f.read(4)  # ActorIndices
        byte = self.f.read(4)  # ActorIndices
        tapelabel = "placeholder"
        print("CRC32 NÃO IMPLEMENTADO EM TAPELAUNCHERCLIP")

        clip_data = {
            "__class": "TapeLauncherClip",
            "Id": id_entry,
            "TrackId": tid_entry,
            "IsActive": isactive_entry,
            "StartTime": st_entry,
            "Duration": d_entry,
            "ActorIndices": actor_indices,
            "Action": 0,
            "TapeLabels": tapelabel
        }

        return clip_data