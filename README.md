# [Caltech-UCSD Birds-200-2011 (CUB)](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)- reader & csv writer class

## python reader & csv writer class + sample usage

### Goals -
 - read downloaded CUB data files into python data structure 
 - expose simple data access methods
 - add original image photos sizes data
 - expose csv writer method to write the attributes into single csv file
    
### prerequesits (includes image draw bounding boxes and image display)-  
 - numpy  
 - os  
 - sys  
 - cv2  
 - csv  
 - pandas  
 - PIL  
 - matplotlib  
 - pprint  

### inputs -  
 - CUB_PATH # (class init) path to the downloaded CUB databse folder  
 - CSV_PATH # (csv write method) csv filename path to write  
       
### class methods -  
 - getCubSize()              # CUB database size  (int images list size, int number of categories)  
 - getImages()               # CUB images list    (dictionary 'image number' : 'image path')  
 - getImagesSizes()          # CUB images sizes   (dictionary 'image number' : \['width','height'\])  
 - getBoxes()                # CUB bounding boxes (dictionary 'image number' : \['xcenter','ycenter', 'width', 'height\])  
 - getImgClasses()           # CUB images classes (dictionary 'image number' : 'class number')  
 - getClasses()              # CUB classes names  (dictionary 'class number' : 'class name')  
 - writeCubToCsv(file path)  # write to csv,   
     - file format :   
         - csv header row,  
         - data rows :  
             - image path,  
             - image size,  
             - image class name,  
             - bounding box xmin,  
             - bounding box ymin,  
             - bounding box xmax,  
             - bounding box ymax,  
             - bounding box centerx,  
             - bounding box centery,  
             - bounding box width,  
             - bounding box height,  
                
### usage - {put your input in these brackets}
```python
    cub = CUB_ReadWrite({cub download folder path})  # inialize class read all CU data files from 'folder path'  
    cub.{method()}                                   # call class methods, retuns CUB data as described above  
    cub.writeCubToCsv({output csv file name path})   # writes csv file to 'file path' in format decribed above  
    del(cub)                                         # deletes cub object  
```
    
#### see below in usage sample section (very) simple csv read and display images using csv, pandas, PIL packages  
