import PIL, numpy
from PIL import Image

def oneDHoriz(pix,coord,pix2):
    '''Takes a h*w*d numpy array named pix (d is bit depth, d=3 for RGB) and creates a horizontal1D slice through row coord, filling array pix2.  Returns 1D image.'''
    rowslice=numpy.take(pix,[coord,],axis=0)[0]
    pix2[:,:]=rowslice
    image=Image.fromarray(pix2)
    return(image)

if __name__ == '__main__':
    
    # Find all jpegs  in current directory
    import os,sys
    syspath = os.path.dirname(sys.argv[0])
    fullpath = os.path.abspath(syspath)
    allfiles=os.listdir(fullpath)
    filelist=[]
    for filename in allfiles:
        if filename[-4:] in ('.jpg','.JPG') or filename[-5:] in ('.jpeg','.JPEG'):
            filelist.append(filename)
    if len(filelist)==0:
        print("No .jpeg files found....")

    for f in filelist:
        # Build input pixel array and array for storing output
        froot=f.split(".")[0]
        pim=Image.open(f)
        w,h=pim.size
        pix=numpy.array(pim)
        pix2=numpy.zeros((h/4,w,3),numpy.uint8)

        # Slice and save to file
        for y in xrange(0,h-1,h/10):
            im=oneDHoriz(pix,y,pix2)
            im.save(froot+"_Horiz%05d"%y+".png")

        # Transpose pixels before slicing if you want to slice vertically
        pix=numpy.transpose(pix,axes=(1,0,2))
        pix2=numpy.zeros((h,w/4,3),numpy.uint8)
        pix2=numpy.transpose(pix2,axes=(1,0,2))

        # Slice, rotate and save to file
        for x in xrange(0,w-1,w/10):
            im=oneDHoriz(pix,x,pix2).rotate(-90)
            im.save(froot+"_Vert%05d"%x+".png")


