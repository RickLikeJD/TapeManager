import struct
from utils.Classes.SizeClip import *

def getTapeHeader():
    serializedHeader = struct.pack(">I", 1)  # Serializa o número da versão
    serializedHeader += bytes.fromhex("FFFFFFFF")  # Valor temporário em hex
    serializedHeader += bytes.fromhex("9E8454600000009C")  # Classe em hex(Tape)
    return serializedHeader
    
def getClipDICT():  # A Dict for Just Dance (TAPE) Classes
    return {
        b'\xD1\x28\x88\x5D': "ActorEnableClip",
        b'\x86\x07\xD5\x82': "AlphaClip",
        b'\x11\x5F\x12\x8D': "TapeLauncherClip",
        b'\xF6\x1B\x3A\x75': "ColorClip",
        b'\x54\x77\x75\xBC': "ProportionClip",
        b'R\xb8\x9d\x18': SizeClip,
        b'\x36\xA3\x12\xDC': "TranslationClip",
        b'\x4D\xE6\xD8\x71': "BezierCurveFloatLinear",
        b'\xB7\x91\x41\x91': "BezierCurveFloatConstant",
        b'\xE2\xBC\x4F\xB2': "BezierCurveFloatMulti",
        b'\x0E\x1E\x81\x58': "TapeReferenceClip",
        b'\x0F\x19\xB0\x38': "FXClip",
        b'\xC6\xFE\xD5\x8E': "MaterialGraphicDiffuseColorClip",
        b'\x51\x1F\xC7\xA5': "MaterialGraphicUVScaleClip",
        b'\x7A\x9C\x58\xB3': "RotationClip"
    }
    
    
def getClipDICT2(clip_class):  # A Dict for Just Dance (TAPE) Classes
    clip_headers = {
        "ActorEnableClip": bytes.fromhex("D128885D" + "00000068"),
        "AlphaClip": bytes.fromhex("8607D5820000002C"), 
        "TapeLauncherClip": bytes.fromhex("115F128D00000044"),
        "ColorClip": bytes.fromhex("F61B3A75" + "00000044"), 
        "ProportionClip": bytes.fromhex("547775BC00000030"), 
        "SizeClip": bytes.fromhex("52B89D1800000030"),
        "TranslationClip": bytes.fromhex("36A312DC" + "00000044"),
        "BezierCurveFloatLinear": bytes.fromhex("4DE6D871" + "00000024"),
        "BezierCurveFloatConstant": bytes.fromhex("B7914191" + "00000008"),
        "BezierCurveFloatMulti": bytes.fromhex("E2BC4FB2" + "00000014"),
        "TapeLauncherClip": bytes.fromhex("115F128D" + "FFFFFFFF"),
        "TapeReferenceClip": bytes.fromhex("0E1E8158" + "00000054"),
        "FXClip": bytes.fromhex("0F19B038" + "00000034"),
        "MaterialGraphicDiffuseColorClip": bytes.fromhex("C6FED58E" + "0000004C"),
        "MaterialGraphicUVScaleClip": bytes.fromhex("511FC7A5" + "00000040"),
        "RotationClip": bytes.fromhex("7A9C58B3" + "00000034")
    }
    return clip_headers.get(clip_class, b'')
