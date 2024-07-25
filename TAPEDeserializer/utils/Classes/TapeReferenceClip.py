import struct
from utils.Classes.BezierCurveFloat import BezierCurveFloat  # Importe corrigido
from utils.Tape import *
from utils.StringID import *

class TapeReferenceClip:
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
        path = [self.clip["Path"].replace(self.clip["Path"].split("/")[-1], ""), self.clip["Path"].split("/")[-1]]
        
        serialized += struct.pack(">I", len(path[1])) + path[1].encode()
        serialized += struct.pack(">I", len(path[0])) + path[0].encode()
        
        toCRC = self.clip["Path"]
        StringID = StrToCRC(STRIDE, toCRC, len(toCRC))
        serialized += struct.pack(">I", StringID)
        
        serialized += struct.pack(">I", 0)
        serialized += struct.pack(">I", self.clip["Loop"])
        serialized += struct.pack(">I", 0)
        
        return serialized