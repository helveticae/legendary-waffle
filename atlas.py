import numpy as np
from PIL import Image # Testing rendering map with PIL

def generate_chunk(size=8):
    # Very basic island where 0 is water and 1 is land
    chunk = np.zeros((size, size))
    center = size // 2
    radius = size // 4
    ones_coords = []
    for i in range(size):
        for j in range(size):
            if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
                chunk[i][j] = 1
                ones_coords.append((i,j))

    # Randomize starting position within land (value 1)
    rand_coord = np.random.choice(len(ones_coords))
    chunk[ones_coords[rand_coord]] = 3
    return chunk


def detect_position(chunk, x, y):
    return chunk[x][y]


def render_visual():
    size = 512
    map_data = generate_chunk(size)

    # Find the coordinate of the starting point (value 3) in the map
    start_coord = None
    for i in range(size):
        for j in range(size):
            if map_data[i][j] == 3:
                start_coord = (i, j)
                break
        if start_coord:
            break

    # Render the map as an image
    im = Image.new('RGB', (size, size), (0, 0, 255))
    pixels = im.load()
    for i in range(size):
        for j in range(size):
            if map_data[i][j] == 1:
                pixels[i, j] = (0, 255, 0)
            elif map_data[i][j] == 3:
                # Set a 6x6 square around the starting point to black
                for m in range(i - 3, i + 3):
                    for n in range(j - 2, j + 3):
                        if m >= 0 and m < size and n >= 0 and n < size:
                            pixels[m, n] = (0, 0, 0)
    im.show()

if __name__ == "__main__":
    tiny_island = generate_chunk()
    print(tiny_island)
    print(detect_position(tiny_island, 3, 5))  # should print 1
    render_visual()
