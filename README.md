### This ipynb presents CUB reader and writer class and sample usage

Goals -   
    read downloaded CUB data files into data structure  
    expose simple data acess methods 
    add images sizes data  
    expose csv writer method to write the data into single csv file  
      
prerequesits (includes image draw bounding boxes and image display)-  
    numpy,  
    os,  
    cv2,  
    csv,  
    pandas,  
    PIL,  
    matplotlib,  
    pprint,  
  
  
inputs -  
    CUB_PATH # (class init) path to original download folder  
    CSV_PATH # (csv write method) csv file path for writer  
         
class methods -  
    getCubSize()              # CUB database size  (int)  
    getImages()               # CUB images list    (dictionary 'image number' : 'image path')  
    getImagesSizes()          # CUB images sizes   (dictionary 'image number' : \['width','height'\])  
    getBoxes()                # CUB bounding boxes (dictionary 'image number' : \['xcenter','ycenter', 'width', 'height\])  
    getImgClasses()           # CUB images classes (dictionary 'image number' : 'class number')  
    getClasses()              # CUB classes names  (dictionary 'class number' : 'class name')  
    writeCubToCsv(file path)  # write to csv,   
      
        file format :   
            csv header row,  
            row :  
                image path,  
                image size,  
                image class name,  
                bounding box xmin,  
                bounding box ymin,  
                bounding box xmax,  
                bounding box ymax,  
                  
                  
usage -   
       cub = CUB_ReadWrite(folde path)  # inialize class read all CU data files from 'folder path'  
       cub.{method()}                   # returns methods CUB data as described above  
       cub.writeCubToCsv(file path)     # writes csv file to 'file path' in format decribed above  
       del(cub)                         # deletes object  
      
see below in usage sample section (very) simple csv read and display images using csv, pandas, PIL packages  
