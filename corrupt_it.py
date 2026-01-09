def corrupt_png(input_path, output_path):
    with open(input_path, 'rb') as f:
        data = bytearray(f.read())

    # Header Corruption: Changing the PNG signature to 'CORRUPT!'
    # Standard is: \x89\x50\x4E\x47\x0D\x0A\x1A\x0A
    data[0:8] = b'\x43\x4F\x52\x52\x55\x50\x54\x21'

    # Tail Corruption: Changing 'IEND' to 'DEAD'
    # We look for the 'IEND' string which is 8 bytes from the end
    data[-8:-4] = b'\x44\x45\x41\x44'

    with open(output_path, 'wb') as f:
        f.write(data)
    print(f"Success: {output_path} is now corrupted and unopenable.")

corrupt_png('original.png', 'challenge.png')