import os
import shutil


def main():
    for count, filename in enumerate(os.listdir("raw")):
        print(filename)
        if 'DS_Store' in filename:
            continue
        n = 5
        zoom = 8
        pad = (2**zoom) / 2
        x, y = tuple(int(d) for d in filename.split(".")[0].split(","))
        dst = str(zoom)+"," + str(pad+(x//n)) + "," + str(pad-(y//n)) + ".png"
        src = 'raw/' + filename
        dst = 'map/' + dst
        print(src, "->", dst)
        shutil.copy(src, dst)
if __name__ == '__main__':
    main()
