# [Caltech-UCSD Birds-200-2011 (CUB)](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)- reader & csv writer class

## python reader & csv writer class + sample usage

### Goals -
 - read downloaded CUB data files into python data structure 
 - expose simple data access methods
 - add original image photos sizes data
 - expose csv writer method to write the attributes into single csv file
    
### CUB data
download the CUB data files from [CUB data files](http://www.vision.caltech.edu/visipedia-data/CUB-200-2011/CUB_200_2011.tgz)

### class prerequesits -  
 - os  
 - csv  
 - PIL  
 
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
                
### basic usage - just write csv file 
```python
    # {put your input in these brackets}
    cub = CUB_ReadWrite({cub download folder path})  # inialize class read all CU data files from 'folder path'  
    cub.writeCubToCsv({output csv file name path})   # writes csv file to 'file path' in format decribed above  
    del(cub)                                         # deletes cub object  
```

### optional usage - call class methods to use CUB source data
```python
    #{put your input in these brackets}
    cub = CUB_ReadWrite({cub download folder path})  # inialize class read all CU data files from 'folder path' 
    cub.{method()}                                   # call class methods, retuns CUB data as described above     	
    cub.writeCubToCsv({output csv file name path})   # writes csv file to 'file path' in format decribed above  
    del(cub)                                         # deletes cub object  
```
### better usage - ead csv data into pandas dataframe, use pandas to acess CUB data
```python
    #{put your input in these brackets}
    cub = CUB_ReadWrite({cub download folder path})  # inialize class read all CU data files from 'folder path' 
    cub.writeCubToCsv({output csv file name path})   # writes csv file to 'file path' in format decribed above  
    del(cub)                                         # deletes cub object  
    csvData =  pd.read_csv(csvPath)                  # read the csv creates file into pandas dataframe and use pandas  "magic"
```

#### see below in usage sample section (very) simple csv read and display images using csv, pandas, PIL packages  
