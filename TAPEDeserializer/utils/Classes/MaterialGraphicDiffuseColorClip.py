import struct
from utils.Classes.BezierCurveFloat import BezierCurveFloat  # Importe corrigido
from utils.Tape import *

class MaterialGraphicDiffuseColorClip:
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

        byte = self.f.read(4)  # LayerIdx
        lidx_entry = struct.unpack('>I', byte)[0]
        
        byte = self.f.read(4)  # UVModifierIdx
        uvmidx_entry = struct.unpack('>I', byte)[0]

        curve_R = BezierCurveFloat(self.f).Deserialize()
        curve_G = BezierCurveFloat(self.f).Deserialize()
        curve_B = BezierCurveFloat(self.f).Deserialize()
        
        clip_data = {
            "__class": "MaterialGraphicDiffuseColorClip",
            "Id": id_entry,
            "TrackId": tid_entry,
            "IsActive": isactive_entry,
            "StartTime": st_entry,
            "Duration": d_entry,
            "ActorIndices": actor_indices,
            "LayerIdx": lidx_entry,
            "UVModifierIdx": uvmidx_entry,
            "CurveR": curve_R,
            "CurveG": curve_G,
            "CurveB": curve_B
        }
        
        return clip_data