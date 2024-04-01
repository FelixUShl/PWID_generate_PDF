def hex8b(qr_name: str) -> str:
    return qr_name[:-4].upper()


def dec3b(qr_name: str) -> str:
    return str(int(qr_name[-10:-4], 16))


def fac_code(qr_name: str) -> str:
    fc = str(int(hex8b(qr_name)[-6:-4], 16))
    code = str(int(hex8b(qr_name)[-4:], 16))
    return f"{fc},{code}"


def generate_qr_list(qrs: list, path: str) -> list:
    data = list()
    for qr in qrs:
        data.append([f"{path}/{qr}", f"HEX 8b: {hex8b(qr)}", f"DEC 3b: {dec3b(qr)}", f"FC: {fac_code(qr)}"])
    return data
