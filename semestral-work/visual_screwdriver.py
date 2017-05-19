from PIL import Image
import numpy as np
import os


class VisualScrewdriver:
    imageCounter = 1
    imagePath = None
    imageData = None
    autoSave = False

    @staticmethod
    def noImageLoaded():
        print("No image is loaded, use `help` command for list of commands.")

    @staticmethod
    def commandExit():
        pass

    @staticmethod
    def commandHelp():
        print("""Welcome in Visual screwdriver.

Below are listed available commands. Each command will apply to modified image. 
If you want to apply commands to raw image, use `reset` command first. 
- exit               - terminates the app
- help               - prints this help
- save               - save locally stored image
- autosave           - toggle auto saving of the image
- new                - sets new image source and reset locally stored image 
- reset              - resets the locally stored image to original image
- rotateR            - rotates the image to right by 90 percent
- rotateL            - rotates the image to left by 90 percent
- mirrorX            - mirrors the image by X axis
- mirrorY            - mirrors the image by Y axis
- invert             - inverts colors of the image
- dark               - make the image darker
- light              - make the image lighter
- greyscale          - converts the image to greyscale
- highlight          - highlight edges of the image
""")

    def commandSave(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        if not os.path.exists("export"):
            os.makedirs("export")

        while os.path.isfile("export/" + str(self.imageCounter) + ".png"):
            self.imageCounter += 1

        Image.fromarray(self.imageData, "RGB").save("export/" + str(self.imageCounter) + ".png")
        print("Saving image into", "export/" + str(self.imageCounter) + ".png", "file.")
        self.imageCounter += 1

    def commandAutosave(self):
        self.autoSave = not self.autoSave
        print("Toggling autosave to", self.autoSave)

    def commandNew(self):
        self.imagePath = input("Enter image file: ")
        if not os.path.isfile(self.imagePath):
            print("Wrong file.")
        else:
            self.imageData = np.array(Image.open(self.imagePath))
            print("Storing new image.")

    def commandReset(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        if not os.path.isfile(self.imagePath):
            print("Wrong file. Cannot reset to original image.")
        else:
            self.imageData = np.array(Image.open(self.imagePath))
            print("Resetting stored image.")

    def commandRotateR(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        self.imageData = np.rot90(self.imageData, 3)

        if self.autoSave:
            self.commandSave()

    def commandRotateL(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        self.imageData = np.rot90(self.imageData)

        if self.autoSave:
            self.commandSave()

    def commandMirrorX(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        self.imageData = self.imageData[::-1]

        if self.autoSave:
            self.commandSave()

    def commandMirrorY(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        self.imageData = self.imageData[:, ::-1]

        if self.autoSave:
            self.commandSave()

    def commandInvert(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        self.imageData[...] = 255 - self.imageData[...]

        if self.autoSave:
            self.commandSave()

    def commandDark(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        self.imageData[...] = self.imageData[...] * (1 - 0.25)

        if self.autoSave:
            self.commandSave()

    def commandLight(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        self.imageData[...] = self.imageData[...] + (256 - self.imageData[...]) * 0.25

        if self.autoSave:
            self.commandSave()

    def commandGreyscale(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        w, h, c = self.imageData.shape

        for x in range(w):
            for y in range(h):
                grey = self.imageData[x, y, 0] * 0.2989 + \
                       self.imageData[x, y, 1] * 0.5870 + \
                       self.imageData[x, y, 2] * 0.1140

                for z in range(c):
                    self.imageData[x, y, z] = grey

        if self.autoSave:
            self.commandSave()

    def commandHighlight(self):
        if self.imageData is None:
            self.noImageLoaded()
            return

        tmp = np.array(self.imageData).copy()

        w, h, c = self.imageData.shape

        for x in range(1, w - 1):
            for y in range(1, h - 1):
                for z in range(c):
                    col = (
                        + 9 * self.imageData[x, y, z]
                        - self.imageData[x - 1, y, z]
                        - self.imageData[x + 1, y, z]
                        - self.imageData[x, y + 1, z]
                        - self.imageData[x, y - 1, z]
                        - self.imageData[x - 1, y + 1, z]
                        - self.imageData[x - 1, y - 1, z]
                        - self.imageData[x + 1, y - 1, z]
                        - self.imageData[x + 1, y + 1, z])

                    if col < 0:
                        col = 0

                    if col > 255:
                        col = 255

                    tmp[x, y, z] = col

        self.imageData = tmp

        if self.autoSave:
            self.commandSave()
