import struct
from utils.Classes.BezierCurveFloat import BezierCurveFloat  # Importe corrigido
from utils.Tape import *

class MaterialGraphicUVScaleClip:
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
        
        for Actor in range(len(self.clip["ActorIndices"])):
            serialized += struct.pack(">i", self.clip['ActorIndices'][Actor])
        
        serialized += struct.pack(">i", self.clip["LayerIdx"])
        serialized += struct.pack(">i", self.clip["UVModifierIdx"])
        
        if "CurveScaleU" in self.clip and self.clip["CurveScaleU"].get("__class") == "BezierCurveFloat":
            serialized += struct.pack(">i", 4)
            bezier_curve_x = BezierCurveFloat(self.clip["CurveScaleU"])
            serialized += bezier_curve_x.Serialize()
        
        if "CurveScaleV" in self.clip and self.clip["CurveScaleV"].get("__class") == "BezierCurveFloat":
            serialized += struct.pack(">i", 4)
            bezier_curve_y = BezierCurveFloat(self.clip["CurveScaleV"])
            serialized += bezier_curve_y.Serialize()

        if "CurvePivotX" in self.clip and self.clip["CurvePivotX"].get("__class") == "BezierCurveFloat":
            serialized += struct.pack(">i", 4)
            bezier_curve_z = BezierCurveFloat(self.clip["CurvePivotX"])
            serialized += bezier_curve_z.Serialize()
            
        if "CurvePivotY" in self.clip and self.clip["CurvePivotY"].get("__class") == "BezierCurveFloat":
            serialized += struct.pack(">i", 4)
            bezier_curve_z = BezierCurveFloat(self.clip["CurvePivotY"])
            serialized += bezier_curve_z.Serialize()
            
        return serialized