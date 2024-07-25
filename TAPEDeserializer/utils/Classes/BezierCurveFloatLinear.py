import struct
from utils.Tape import *

class BezierCurveFloatLinear:
    def __init__(self, f):
        self.f = f
        
    def Deserialize(self):
        ValueLeft = []
        NormalLeftOut = []
        ValueRight = []
        NormalRightIn = []
        
        for VL_unpk in range(2):
            byte = self.f.read(4)
            value = struct.unpack('>f', byte)[0]
            ValueLeft.append(value)
        
        for NLOut_unpk in range(2):
            byte = self.f.read(4)
            value = struct.unpack('>f', byte)[0]
            NormalLeftOut.append(value)
        
        for VR_unpk in range(2):
            byte = self.f.read(4)
            value = struct.unpack('>f', byte)[0]
            ValueRight.append(value)
        
        for NRIn_unpk in range(2):
            byte = self.f.read(4)
            value = struct.unpack('>f', byte)[0]
            NormalRightIn.append(value)
        
        # Cria o vetor ValueLeft com os dois valores lidos
        clip_data = {
            "__class": "BezierCurveFloatLinear",
            "ValueLeft": ValueLeft,
            "NormalLeftOut": NormalLeftOut, 
            "ValueRight": ValueRight, 
            "NormalRightIn": NormalRightIn, 
        }
        
        return clip_data
