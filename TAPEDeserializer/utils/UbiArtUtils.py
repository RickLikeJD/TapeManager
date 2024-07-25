def tellSize(fileStream, add=20000):
    length = fileStream.tell()
    fileStream.seek(4)
    fileStream.write((length + add).to_bytes(4, byteorder="big", signed=False))

def utf8len(s):
    return len(s.encode('utf-8-sig'))
    
def hex_to_rgb(value): #https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    
