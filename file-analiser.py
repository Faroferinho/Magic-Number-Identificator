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
    return [binascii.unhexlify(b'00')]

def get_binary_header(file=str):
    header = b''

    with open(file, 'rb') as binary_file:
        type = get_type(file)
        signatures = get_magicnumbers(type)

        if(type in ["jpg", "jpeg", "jp2", "j2k", "jpf", "jpm", "jpg2", "j2c", "jpc", "jpx", "mj2"]):
            header = binary_file.read(4)
            if(header in signatures):
                return True
            else:
                print("Header " + str(header))
        elif(type == "png"):
            header = binary_file.read(8)
            if(header in signatures):
                return True
            else:
                print("Header " + str(header))
        elif type == "gif":
            header = binary_file.read(6)
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

file_path = ""
match = get_binary_header(file_path)
if not match:
    print(file_path.split("\\")[-1] + " - Header Match? " + str(match) + "\n")