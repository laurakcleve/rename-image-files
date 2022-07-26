import shutil, os, time, datetime, re
from PIL import Image

os.chdir('M:\\Downloads\\from phone\\rename')

# Default camera names
# fileNamePattern = re.compile(r'DSC_\d\d\d\d.jpg')


fileNamePattern = re.compile(r'(PXL_)?(\d){8}_(\d){9}(\.PORTRAIT-02\.ORIGINAL)?(\.MP)?(\.PORTRAIT)?(\.NIGHT)?.jpg$')
fileNamePattern_2 = re.compile(r'(00[01]00([lt]r)?(PORTRAIT|IMG)_00[01]00_BURST(\d){17}(~2).jpg$)|(^(MV)?IMG_(\d){8}_(\d){6}(~2).jpg$)')
fileNamePattern_2_2 = re.compile(r'PXL_(\d){8}_(\d){9}(\.PORTRAIT)?(~2).jpg$')
fileNamePattern_3 = re.compile(r'PXL_(\d){8}_(\d){9}(\.PORTRAIT)?(~3).jpg$')
fileNamePattern_blurred = re.compile(r'PXL_(\d){8}_(\d){9}\.PORTRAIT-01\.COVER.jpg$')

# (old?) Pixel names
# fileNamePattern = re.compile(r'(00[01]00([lt]r)?(PORTRAIT|IMG)_00[01]00_BURST(\d){17}.jpg$)|(^(MV)?IMG_(\d){8}_(\d){6}.jpg$)')
# fileNamePattern_2 = re.compile(r'(00[01]00([lt]r)?(PORTRAIT|IMG)_00[01]00_BURST(\d){17}(~2).jpg$)|(^(MV)?IMG_(\d){8}_(\d){6}(~2).jpg$)')
# fileNamePattern_blurred = re.compile(r'(00[01]00([lt]r)?(PORTRAIT|IMG)_00[01]00_BURST(\d){17}(_COVER)(~2)?.jpg$)')

# CameraMX names
# fileNamePattern = re.compile(r'PHOTO_\d\d\d\d\d\d\d\d_\d\d\d\d\d\d.jpg')

for file in os.listdir('.'):
    # newFileName = datetime.datetime.strptime(time.ctime(os.path.getctime(file)), "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d %H.%M.%S")

    print(file)

    searchResult = fileNamePattern.search(file)
    searchResult_2 = fileNamePattern_2.search(file)
    searchResult_2_2 = fileNamePattern_2_2.search(file)
    searchResult_3 = fileNamePattern_3.search(file)
    searchResult_blurred = fileNamePattern_blurred.search(file)

    if searchResult != None or searchResult_2 != None or searchResult_2_2 != None or searchResult_3 != None or searchResult_blurred != None:
        absWorkingDir = os.path.abspath('.')
        dateTaken = Image.open(file)._getexif()[36867]
        dateTakenFormat = datetime.datetime.strptime(dateTaken, "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d %H.%M.%S")

        originalFileName = os.path.join(absWorkingDir, file)
        if searchResult != None:
            newFileName = os.path.join(absWorkingDir, dateTakenFormat + ".jpg")
        elif searchResult_2 != None:
            newFileName = os.path.join(absWorkingDir, dateTakenFormat + " 2.jpg")
        elif searchResult_2_2 != None:
            newFileName = os.path.join(absWorkingDir, dateTakenFormat + " 2.jpg")
        elif searchResult_3 != None:
            newFileName = os.path.join(absWorkingDir, dateTakenFormat + " 3.jpg")
        elif searchResult_blurred != None:
            newFileName = os.path.join(absWorkingDir, dateTakenFormat + " blurred.jpg")

        print("Old file name: " + originalFileName)
        print("New file name: " + newFileName)

        # Uncomment after testing
        shutil.move(originalFileName, newFileName)


    print()