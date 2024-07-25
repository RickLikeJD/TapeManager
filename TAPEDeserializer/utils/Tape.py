import struct
  
def getClipNameFromBytes(clip_bytes):  # Um Dict para classes Just Dance (TAPE)
    clip_headers = {
        bytes.fromhex("D128885D"): "ActorEnableClip",
        bytes.fromhex("8607D582"): "AlphaClip", 
        bytes.fromhex("115F128D"): "TapeLauncherClip",
        bytes.fromhex("F61B3A75"): "ColorClip", 
        bytes.fromhex("547775BC"): "ProportionClip", 
        bytes.fromhex("52B89D18"): "SizeClip",
        bytes.fromhex("2D8C885B"): "SoundSetClip",
        bytes.fromhex("36A312DC"): "TranslationClip",
        bytes.fromhex("4DE6D871"): "BezierCurveFloatLinear",
        bytes.fromhex("B7914191"): "BezierCurveFloatConstant",
        bytes.fromhex("E2BC4FB2"): "BezierCurveFloatMulti",
        bytes.fromhex("0E1E8158"): "TapeReferenceClip",
        bytes.fromhex("0F19B038"): "FXClip",
        bytes.fromhex("C6FED58E"): "MaterialGraphicDiffuseColorClip",
        bytes.fromhex("511FC7A5"): "MaterialGraphicUVScaleClip",
        bytes.fromhex("7A9C58B3"): "RotationClip",
        bytes.fromhex("E68412CA"): "MaterialGraphicDiffuseAlphaClip",
        bytes.fromhex("A247B5D3"): "SpawnActorClip",
        bytes.fromhex("FFFFFFFF"): "NULL"
    }
    
    return clip_headers.get(clip_bytes, "Classe não encontrada")