import binascii


def get_type(file=str):
    # Get the character sequence after the last dot in a file name.
    result = ""

    if(file.find(".")):
        list = file.split(".")
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
    return []

def get_binary_header(file=str):
    header = b''

    with open(file, 'rb') as binary_file:
        type = get_type(file)
        signatures = get_magicnumbers(type)

        if (type in ["bmp", "dib", "gz"]):
            header = binary_file.read(2)
            if(header in signatures):
                return True
            else:
                print("Header " + str(header))
        elif(type in ["jpg", "jpeg", "jp2", "j2k", "jpf", "jpm", "jpg2", "j2c", "jpc", "jpx", "mj2"]):
            header = binary_file.read(4)
            if(header in signatures):
                return True
            else:
                print("Header " + str(header))

        elif type in ["gif", "7z", "xz"]:
            header = binary_file.read(6)
            if(header in signatures):
                return True
            else:
                print("Header " + str(header))

        elif type in ["blend"]:
                    header = binary_file.read(7)
                    if(header in signatures):
                        return True
                    else:
                        print("Header " + str(header))

        elif type in ["png", "deb", "doc", "xls", "ppt", "msi", "msg"]:
            header = binary_file.read(8)
            if(header in signatures):
                return True
            else:
                print("Header " + str(header))

        elif type == "mp4":
            binary_file.seek(4,1)
            header = binary_file.read(4)
            if(header in signatures):
                return True
            else:
                print("Header " + str(header))

        elif type == "webp":
            header = binary_file.read(4)
            binary_file.seek(4,1)
            header += binary_file.read(4)

            if(header in signatures):
                return True
            else:
                print("Header " + str(header))
            
        return False

files = [
    ""
]

for file_path in files:
    match = get_binary_header(file_path)
    if get_magicnumbers(get_type(file_path)).count < 0:    
        if not match:
            print(file_path.split("\\")[-1] + " - Header Match =" + str(match) + "\n")
        else:
            print("File " + file_path.split("\\")[-1] + " matches what is expected")
    else:
        print("Type not suported, sorry :(")