import os
import csv
from PIL import Image
class CUB_ReadWrite:
    
    def __init__(self,cubPath):
        IMAGES_FILE   = "images.txt"
        BBOX_FILE     = "bounding_boxes.txt"
        IMGCLASS_FILE = "image_class_labels.txt"
        CLASSES_FILE  = "classes.txt"
        
        if (not (os.path.exists(cubPath))):
            raise ValueError("CUB data folder %s not found" % cubPath)
        else:
            self.cubPath = cubPath
            self.imgTxtPath = os.path.join(cubPath,IMAGES_FILE)
            self.bbTxtPath = os.path.join(cubPath,BBOX_FILE)
            self.imgClassPath = os.path.join(cubPath,IMGCLASS_FILE)
            self.classesPath = os.path.join(cubPath,CLASSES_FILE)
            if (not (os.path.exists(self.imgTxtPath)   and \
                     os.path.exists(self.bbTxtPath)    and \
                     os.path.exists(self.imgClassPath) and \
                     os.path.exists(self.classesPath)  and \
                     os.path.exists(os.path.join(cubPath,'images')))):
                raise ValueError("a CUB data file not found ({} ,{} ,{}, {}, {})".format(\
                               self.imgTxtPath, self.bbTxtPath, self.imgClassPath, \
                               self.classesPath, 'images folder' ))
            else: 
                self.imgList,self.imgDict,self.imgSizesDict = self._readImgTxt()
                self.bboxDict = self._readBB()
                self.imgClassDict = self._readImgClass()
                self.classesDict = self._readClasses()
        
    def _getImgSize(self,imgPath):
        im = Image.open(imgPath)
        return im.size

    def _readImgTxt(self):
        imgList = []
        imgDict = {}
        imgSizesDict = {}
        with open(self.imgTxtPath) as f:
            spamreader = csv.reader(f, delimiter=' ')
            for row in spamreader:
                imgList.append(int(row[0]))
                imgPath = os.path.join(self.cubPath+'images',row[1])
                width,height = self._getImgSize(imgPath)
                imgDict[int(row[0])] = imgPath
                imgSizesDict[int(row[0])] = [width,height]
        return imgList,imgDict,imgSizesDict

    def _readBB(self):
        bboxDict = {}
        with open(self.bbTxtPath) as f:
            spamreader = csv.reader(f, delimiter=' ')
            for row in spamreader:
                bboxDict[int(row[0])] = [ int(float(x)) for x in row[1:5] ]
        return bboxDict

    def _readImgClass(self):
        imgClassDict = {}
        with open(self.imgClassPath) as f:
            spamreader = csv.reader(f, delimiter=' ')
            for row in spamreader:
                imgClassDict[int(row[0])] = int(row[1])  #offset by 0 
        return imgClassDict

    def _readClasses(self):
        classDict = {}
        with open(self.classesPath) as f:
            spamreader = csv.reader(f, delimiter=' ')
            for row in spamreader:
                classDict[int(row[0])] = row[1]
        return classDict
    
    def getImages(self):
        return self.imgDict
   
    def getImagesSizes(self):
        return self.imgSizesDict
    
    def getBoxes(self):
        return self.bboxDict
    
    def getImgClasses(self):
        return self.imgClassDict
    
    def getClasses(self):
        return self.classesDict
    
    def getCubSize(self):
        return len(self.imgList) , len(self.classesDict)    
    
    def writeCubToCsv(self,csvFilePath):
        with open(csvFilePath, 'w') as csvfile:
            fieldnames = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax', 'centerx', 'centery', 'b-width', 'b-height' ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for k in self.imgList:
                i = k -1  # reindexing
                #imgPath = os.path.join(self.cubPath, self.imgDict[self.imgList[i]])
                imgPath  = self.imgDict[self.imgList[i]]
                imWidth  = self.imgSizesDict[self.imgList[i]][0]
                imHeight = self.imgSizesDict[self.imgList[i]][1] 
                imgClass = self.classesDict[self.imgClassDict[self.imgList[i]]]
                boxWidth = int(self.bboxDict[self.imgList[i]][2])
                boxHeight = int(self.bboxDict[self.imgList[i]][3])
                xmin = int(self.bboxDict[self.imgList[i]][0])
                ymin = int(self.bboxDict[self.imgList[i]][1])
                xmax = int(self.bboxDict[self.imgList[i]][0] + boxWidth)
                ymax = int(self.bboxDict[self.imgList[i]][1] + boxHeight)
                centerx = int(self.bboxDict[self.imgList[i]][0] + boxWidth / 2)
                centery = int(self.bboxDict[self.imgList[i]][1] + boxHeight / 2)
                writer.writerow({'filename' : imgPath,'width' : imWidth, 'height' : imHeight,'class' : imgClass,'xmin' : xmin,\
                     'ymin' : ymin,'xmax' : xmax,'ymax' : ymax, 'centerx' : centerx, 'centery' : centery, 'b-width' : boxWidth, 'b-height' : boxHeight})