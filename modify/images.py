from PIL import Image

class imagehandler:

    ## Creates all black image of given size
    def createImage(width, height, basevec=None, imgname="img.jpg"):
        matlist = []

        if basevec is None:
            basevec = np.ones((width * height * 3), 'uint8')
        else:
            for b in enumerate(basevec):
                if (b[1] < 0):
                    basevec[b[0]] = 0
                if (b[1] > 1):
                    basevec[b[0]] = 1

        rgb_array = np.zeros((width, height, 3), 'uint8')
        for x in range(0, width):
            for y in range(0, height):
                rgb_array[x, y, 0] = basevec[x * y] * 255  # R
                rgb_array[x, y, 1] = basevec[x * y + (width * height)] * 255  # G
                rgb_array[x, y, 2] = basevec[x * y + (width * height * 2)] * 255  # B

        img = Image.fromarray(rgb_array)
        img.save(imgname)
        # img.show()

        # print("image created")
