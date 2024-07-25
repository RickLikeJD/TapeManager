import struct
from utils.Tape import *
from utils.StringID import *

class FXClip:
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
        
        byte = self.f.read(4) # SKIP (these bytes should be from FXName)
        print("CRC32 NÃO IMPLEMENTADO EM FXClip")
        fxname = "placeholder"


        byte = self.f.read(4)  # KillParticlesOnEnd
        particles_entry = struct.unpack('>I', byte)[0]

        clip_data = {
            "__class": "FXClip",
            "Id": id_entry,
            "TrackId": tid_entry,
            "IsActive": isactive_entry,
            "StartTime": st_entry,
            "Duration": d_entry,
            "ActorIndices": actor_indices,
            "FxName": fxname,
            "KillParticlesOnEnd": particles_entry
        }
        
        
        return clip_data