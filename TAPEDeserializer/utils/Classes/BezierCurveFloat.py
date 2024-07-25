import struct
from utils.Classes.BezierCurveFloatLinear import BezierCurveFloatLinear
from utils.Classes.BezierCurveFloatConstant import BezierCurveFloatConstant
from utils.Classes.BezierCurveFloatMulti import BezierCurveFloatMulti
from utils.Tape import *
from utils.Tape import getClipNameFromBytes

class BezierCurveFloat:
    def __init__(self, f):
        self.f = f

    def Deserialize(self):
        #Detect what beziercurve this shit is
        byte = self.f.read(4)
        byte = self.f.read(4)
        class_get_hex = byte.hex().upper()  # Converte os bytes para hexadecimal e garante que seja em maiúsculas
        clip_name = getClipNameFromBytes(byte)  # Passa os bytes diretamente
        
        clip_data = {
            "__class": "BezierCurveFloat",
            "Curve": {}
        }
        
        if (clip_name == "BezierCurveFloatConstant"):
            byte = self.f.read(4)
            clip_instance = BezierCurveFloatConstant(self.f)
            curve_data = clip_instance.Deserialize()
            clip_data["Curve"] = curve_data
            
        elif (clip_name == "BezierCurveFloatLinear"):
            byte = self.f.read(4)
            clip_instance = BezierCurveFloatLinear(self.f)
            curve_data = clip_instance.Deserialize()
            clip_data["Curve"] = curve_data
            
        elif (clip_name == "BezierCurveFloatMulti"):
            byte = self.f.read(4)
            clip_instance = BezierCurveFloatMulti(self.f)
            curve_data = clip_instance.Deserialize()
            clip_data["Curve"] = curve_data
            
        elif (clip_name == "NULL"):
            pass
            
        return clip_data