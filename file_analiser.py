import binascii

class signature:
    def __init__(self, path=str):
        self.file_name = path.split("\\")[-1]
        self.expected_signatures = get_magicnumbers(get_type(self.file_name))
        self.actual_signature = get_signature(path)
        self.match_signature = True if self.actual_signature in self.expected_signatures else False
        

def get_type(path=str):
    # Get the character sequence after the last dot in a file name.
    result = ""

    if(path.find(".")):
        list = path.split(".")
        return list[-1]

    return result

def get_magicnumbers(file_type):
    if file_type in ["jpg", "jpeg", "jp2", "j2k", "jpf", "jpm", "jpg2", "j2c", "jpc", "jpx", "mj2"]:
        return [
            binascii.unhexlify(b'FFD8FFDB'),
            binascii.unhexlify(b'FFD8FFE0'),
            binascii.unhexlify(b'FFD8FFEE'),
            binascii.unhexlify(b'FFD8FFE1'),
            binascii.unhexlify(b'0000000C'),
            binascii.unhexlify(b'FF4FFF51')
        ]
    elif file_type == "png":
        return [
            binascii.unhexlify(b'89504E470D0A1A0A')
        ]
    elif file_type == "gif":
        return [
            binascii.unhexlify(b'474946383761'),
            binascii.unhexlify(b'474946383961')
        ]
    elif file_type=="mp4":
        return [
            binascii.unhexlify(b'66747970'),
            binascii.unhexlify(b'66747970')
        ]
    elif file_type=="webp":
        return [
            binascii.unhexlify(b'5249464657454250')
        ]
    elif file_type=="7z":
        return[
            binascii.unhexlify(b'377ABCAF271C')
        ]
    elif file_type=="deb":
        return[
            binascii.unhexlify(b'213C617263683E0A')
        ]
    elif file_type in ["doc", "xls", "ppt", "msi", "msg"]:
        return[
            binascii.unhexlify(b'D0CF11E0A1B11AE1')
        ]
    elif file_type=="gz":
        return[
            binascii.unhexlify(b'1F8B')
        ]
    elif file_type=="xz":
        return[
            binascii.unhexlify(b'FD377A585A00')
        ]
    elif file_type in ["zip", "aar", "apk", "docx", "epub", "ipa", "jar", "kmz", "maff", "msix", "odp", "ods", "odt", "pk3", "pk4", "pptx", "usdz", "vsdx", "xlsx", "xpi", "whl"]:
        return[
            binascii.unhexlify(b'504B0304'),
            binascii.unhexlify(b'504B0506'),
            binascii.unhexlify(b'504B0708')
        ]
    elif file_type in ["bmp", "dib", "gz", "exe", "dll", "mui", "sys", "scr", "cpl", "ocx", "ax", "iec", "ime", "rs", "tsp", "fon", "efi"]:
        return[
            binascii.unhexlify(b'4D5A')
        ]
    return []

def get_signature(path=str):
    type = get_type(path)
    with open(path, 'rb') as binary_file:
        if (type in ["bmp", "dib", "gz", "exe", "dll", "mui", "sys", "scr", "cpl", "ocx", "ax", "iec", "ime", "rs", "tsp", "fon", "efi"]):
            return binary_file.read(2)
        
        elif(type in ["jpg", "jpeg", "jp2", "j2k", "jpf", "jpm", "jpg2", "j2c", "jpc", "jpx", "mj2", "zip", "aar", "apk", "docx", "epub", "ipa", "jar", "kmz", "maff", "msix", "odp", "ods", "odt", "pk3", "pk4", "pptx", "usdz", "vsdx", "xlsx", "xpi", "whl"]):
            return binary_file.read(4)
        
        elif type in ["gif", "7z", "xz"]:
            return binary_file.read(6)

        elif type in ["blend"]:
            return binary_file.read(7)

        elif type in ["png", "deb", "doc", "xls", "ppt", "msi", "msg"]:
            return binary_file.read(8)

        elif type == "mp4":
            binary_file.seek(4,1)
            return binary_file.read(4)

        elif type == "webp":
            header = binary_file.read(4)
            binary_file.seek(4,1)
            header += binary_file.read(4)
            return header