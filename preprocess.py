import os
import shutil


def main():
    for count, filename in enumerate(os.listdir("raw")):
        print(filename)
        pad = 15
        x, y = tuple(int(d) for d in filename.split(".")[0].split(","))
        dst = "5," + str(pad+(x//5)) + "," + str(pad-(y//5)) + ".png"
        src = 'raw/' + filename
        dst = 'map/' + dst
        print(src, "->", dst)
        shutil.copy(src, dst)
if __name__ == '__main__':
    main()
