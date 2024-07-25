import struct
from utils.Classes.BezierCurveFloat import BezierCurveFloat  # Importe corrigido
from utils.Tape import *

class ActorEnableClip:
    def __init__(self, clip):
        self.clip = clip
        
    def Serialize(self):
        clip_class = self.clip["__class"]
        clipHeaders = getClipDICT(clip_class)
        serialized = clipHeaders
        serialized += struct.pack(">I", self.clip["Id"])
        serialized += struct.pack(">I", self.clip["TrackId"])
        serialized += struct.pack(">I", self.clip["IsActive"])
        serialized += struct.pack(">i", self.clip["StartTime"])
        serialized += struct.pack(">I", self.clip["Duration"])
        
        serialized += struct.pack(">i", 0)
       
        item_list = self.clip['ActorIndices']
        count = 0
        for i in item_list:  
            count = count + 1
        
        serialized += struct.pack(">I", count)

        serialized += struct.pack(">I", self.clip["ActorEnable"])
        
        serialized += struct.pack(">i", 0)
        
        return serialized
        