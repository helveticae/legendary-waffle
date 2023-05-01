import numpy as np

def generate_chunk(size=8):
    # Very basic island where 0 is water and 1 is land
    chunk = np.zeros((size, size))
    center = size // 2
    radius = size // 4
    for i in range(size):
        for j in range(size):
            if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
                chunk[i][j] = 1
    return chunk

if __name__ == "__main__":
    tiny_island = generate_chunk()
    print(tiny_island)

    from PIL import Image # Testing rendering map with PIL
    size = 512

    map_data = generate_chunk(size)

    im = Image.new('RGB', (size, size), (0, 0, 255))
    pixels = im.load()
    for i in range(size):
        for j in range(size):
            if map_data[i][j] == 1:
                pixels[i, j] = (0, 255, 0)

    im.save('island-map-test.png')
