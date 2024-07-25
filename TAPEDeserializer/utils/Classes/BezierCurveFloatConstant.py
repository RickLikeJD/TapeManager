import struct

class BezierCurveFloatConstant:
    def __init__(self, f):
        self.f = f
    
    def Deserialize(self):
        byte = self.f.read(4)
        value_entry = struct.unpack('>f', byte)[0]
        
        clip_data = {
            "__class": "BezierCurveFloatConstant",
            "Value": value_entry
        }
        
        return clip_data