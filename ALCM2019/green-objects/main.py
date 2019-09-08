image_size = int(input())

red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)
white = (100, 100, 100)

known_colors = [red, green, blue, white]
color_names = ["R", "G", "B", "W"]

count = 0
for row in range(image_size):

    for j in range(image_size):
        pixels_colors = []
        
        try:
            whitespace = input()
        except:
            continue

        pixels = input().split()

        idx = 0
        for i in range(len(pixels) // 3):
            rgb = (int(pixels[idx]), int(pixels[idx + 1]), int(pixels[idx + 2]))

            if rgb in known_colors:
                pixels_colors.append((color_names[known_colors.index(rgb)]))
                
            if rgb == known_colors[1]:
                pixel_index = (row, i)
                print(pixel_index)


            idx += 3

        print(pixels_colors.count("G"))
    count += 1

print("################")
