import shutil, os, time, datetime, re
from PIL import Image

os.chdir('C:\\Users\\Laura\\Pictures\\from phone')

fileNamePattern = re.compile(r'DSC_\d\d\d\d.JPG')

for file in os.listdir('.'):
    # newFileName = datetime.datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d %H.%M.%S")

    print(file)

    searchResult = fileNamePattern.search(file)

    if searchResult != None:
        absWorkingDir = os.path.abspath('.')
        dateTaken = Image.open(file)._getexif()[36867]
        dateTakenFormat = datetime.datetime.strptime(dateTaken, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d %H.%M.%S")

        originalFileName = os.path.join(absWorkingDir, file)
        newFileName = os.path.join(absWorkingDir, dateTakenFormat + ".JPG")

        print("Old file name: " + originalFileName)
        print("New file name: " + newFileName)

        # Uncomment after testing
        # shutil.move(originalFileName, newFileName)

    print()