# -*- coding: utf-8 -*-



def index():

    return dict(mRows=db(db.tbHomePageSlideResources.id>0).select())


def blog():

    return dict()



def contact():

    return dict()



def about():

    return dict()



def products():
    redirect(URL('product', 'index'))
    return dict()
