# -*- coding: utf-8 -*-



def index():

    return dict(mRows=db(db.tbHomePageSlideResources.id>0).select(),
                mProducts=db((db.tbProducts.id>0) & (db.tbProducts.mIsVisibleToShelf==True)).select(),
                mProductsImages=db(db.tbProductsImageUploads.id>0).select(groupby=db.tbProductsImageUploads.mProduct))


def blog():

    return dict()



def contact():

    return dict()



def about():

    return dict()



def products():
    redirect(URL('product', 'index'))
    return dict()




def download():
    return response.download(request, db)
