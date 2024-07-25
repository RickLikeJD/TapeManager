import struct
from utils.Classes.BezierCurveFloat import BezierCurveFloat  # Importe corrigido
from utils.Tape import *
from utils.StringID import *

class SoundSetClip:
    def __init__(self, f):
           self.f = f
           
    def str_handle(self):
        # Leitura do comprimento do texto
        byte = self.f.read(4)
        length = struct.unpack('>I', byte)[0]

        # Leitura dos bytes do texto
        text_bytes = self.f.read(length)

        # Decodificação dos bytes como string
        text_string = text_bytes.decode('utf-8')  # Ou a codificação apropriada

        return text_string

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
        
        # Handling with names
        soundsetpath_file = self.str_handle()
        
        # Handling with directory
        soundsetpath_directory = self.str_handle()
        
        byte = self.f.read(4) # skip UbiArt Framework CRC32
        
        byte = self.f.read(4) # SoundChannel
        soundchannel_entry = struct.unpack('>I', byte)[0]
        
        byte = self.f.read(4) # StartOffset
        startoff_entry = struct.unpack('>I', byte)[0]
        
        byte = self.f.read(4) # StopsOnEnd
        stopsonend_entry = struct.unpack('>I', byte)[0]

        byte = self.f.read(4) # AccountedForDuration
        accforduration_entry = struct.unpack('>I', byte)[0]

        clip_data = {
            "__class": "SizeClip",
            "Id": id_entry,
            "TrackId": tid_entry,
            "IsActive": isactive_entry,
            "StartTime": st_entry,
            "Duration": d_entry,
            "SoundSetPath": soundsetpath_directory + soundsetpath_file,
            "SoundChannel": soundchannel_entry,
            "StartOffset": startoff_entry,
            "StopsOnEnd": stopsonend_entry,
            "AccountedForDuration": accforduration_entry
        }
        
        return clip_data