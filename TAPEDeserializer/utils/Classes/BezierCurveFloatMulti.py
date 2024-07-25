import struct

class BezierCurveFloatMulti:
    def __init__(self, f):
        self.f = f
        
    def Deserialize(self):
        byte = self.f.read(4)
        keyslen = struct.unpack('>I', byte)[0]  # Supondo que a quantidade de chaves seja um inteiro

        keys = []
        for _ in range(keyslen):
            byte = self.f.read(4)
            ValueLeft = []
            NormalIn = []
            NormalOut = []

            for _ in range(2):
                byte = self.f.read(4)
                value = struct.unpack('>f', byte)[0]
                ValueLeft.append(value)

            for _ in range(2):
                byte = self.f.read(4)
                value = struct.unpack('>f', byte)[0]
                NormalIn.append(value)

            for _ in range(2):
                byte = self.f.read(4)
                value = struct.unpack('>f', byte)[0]
                NormalOut.append(value)

            # Adiciona cada chave à lista de chaves
            keys.append({
                "__class": "KeyFloat",
                "Value": ValueLeft,
                "NormalIn": NormalIn, 
                "NormalOut": NormalOut, 
            })

        # Retorna o dicionário com todas as chaves
        return {
            "__class": "BezierCurveFloatMulti",
            "Keys": keys
        }
