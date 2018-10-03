import requests
from PIL import Image 
import random

def create_random_rgb_bitmap():
    """
    So the logic behind this is clunky but essentially since we can only
    get 10k random numbers per call we split into 4 pieces and just have
    all the red values, all the green, all the blue, and zip them together
    and just iterate through it all
    """
    image = Image.new('RGB', (128, 128), "black")
    pixel_map = image.load()

    red_values = []
    blue_values = []
    green_values = []

    # get literally every number we need
    for _ in range(4):
        red_values += get_random_color_values()
        blue_values += get_random_color_values()
        green_values += get_random_color_values()


    # go through pixel by pixel and edit it to a color
    i = 0
    j = 0
    for r,g,b in zip(red_values, green_values, blue_values):

        if i >= image.size[0] and j >= image.size[1]:
            break
        if i >= image.size[0]:
            i = 0
        if j >= image.size[1]:
            j = 0
            i += 1
        pixel_map[i, j] = (r, g, b) 
        j += 1

    image.show()

def get_random_color_values():
    """
    :returns: enough random values for either R, G, or B
    """
    base_url = "https://www.random.org/integers/?num=4096&min=1&max=255&col=1&base=10&format=plain&rnd=new"

    try:
        r = requests.get(base_url)
        results = r.text.split("\n")[:-1]
        return list(map(int, results))
    except requests.exceptions.HTTPError as e:
        print("http error: {}".format(e))

    # rand_nums = []
    # for _ in range(4096):
    #     rand_nums.append(random.randint(0, 256))
    
    # return rand_nums


def main():
    create_random_rgb_bitmap()

if __name__ == "__main__":
    main()
