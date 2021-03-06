#TO INSTALL pip install Pillow

from gluon import current
import os
try:
    from PIL import Image
except:
    import Image

class MyImage:

    THUMBNAIL_DIMENSION = [250, 150]

    IMAGE_FULLHD_DIMENSION = [1980, 1080]
    IMAGE_HD_DIMENSION = [1280, 720]
    IMAGE_GOOD_DIMENSION = [960, 540]

    @staticmethod
    def cut(mImage, mResolution=THUMBNAIL_DIMENSION, mFit=True):
        return MyImage.transform_engine(mImage, mResolution, mFit)


    @staticmethod
    def transform_engine(image, box=THUMBNAIL_DIMENSION, fit=True):
        '''Downsample the image.
         @param img: Image -  an Image-object
         @param box: tuple(x, y) - the bounding box of the result image
         @param fit: boolean - crop the image to fill the box
        '''

        if image:
            request = current.request
            img = Image.open(request.folder + 'uploads/' + image)
            #preresize image with factor 2, 4, 8 and fast algorithm
            factor = 1
            while img.size[0] / factor > 2 * box[0] and img.size[1] * 2 / factor > 2 * box[1]:
                factor *= 2
            if factor > 1:
                img.thumbnail((img.size[0] / factor, img.size[1] / factor), Image.NEAREST)

            #calculate the cropping box and get the cropped part
            if fit:
                x1 = y1 = 0
                x2, y2 = img.size
                wRatio = 1.0 * x2 / box[0]
                hRatio = 1.0 * y2 / box[1]
                if hRatio > wRatio:
                    y1 = int(y2 / 2 - box[1] * wRatio / 2)
                    y2 = int(y2 / 2 + box[1] * wRatio / 2)
                else:
                    x1 = int(x2 / 2 - box[0] * hRatio / 2)
                    x2 = int(x2 / 2 + box[0] * hRatio / 2)
                img = img.crop((x1, y1, x2, y2))

            #Resize the image with best quality algorithm ANTI-ALIAS
            img.thumbnail(box, Image.ANTIALIAS)

            return img


    @staticmethod
    def transform(image, box=THUMBNAIL_DIMENSION, fit=True, name="thumb"):

        request = current.request
        img = MyImage.transform_engine(image, box, fit)
        root, ext = os.path.splitext(image)
        thumb = '%s_%s__%sx%s_%s' % (root, name, box[0], box[1], ext)
        img.save(request.folder + 'uploads/' + thumb)
        return thumb
