# -*- coding: utf-8 -*-


@auth.requires_login()
def index():
    Validator.admin()
    return dict()



@auth.requires_login()
def home_slide_resources():
    Validator.admin()
    return dict(mRows=db(db.tbHomePageSlideResources.id>0).select())


@auth.requires_login()
def add_home_slide_resource():
    Validator.admin()

    mForm = SQLFORM(db.tbHomePageSlideResources, submit_button=T('Add an image'))

    Validator.form_process(mForm, URL("manager", "home_slide_resources"), mOnAccepted=add_home_slide_resource_accepted)

    return dict(mForm=mForm)

@auth.requires_login()
def add_home_slide_resource_accepted(mForm):
    Validator.admin()

    #Adding thumbnail.
    from lib_image import MyImage
    mRow = db.tbHomePageSlideResources(mForm.vars.id)
    db(db.tbHomePageSlideResources.id==mForm.vars.id).update(mThumbnail=MyImage.tranform(mRow.mTempImage, MyImage.THUMBNAIL_DIMENSION))
    db(db.tbHomePageSlideResources.id==mForm.vars.id).update(mImage=MyImage.tranform(mRow.mTempImage, MyImage.IMAGE_GOOD_DIMENSION))

    print 'temp image', mRow.mTempImage
    MyFile(request.folder + 'uploads/'+str(mRow.mTempImage)).remove()
    pass


def download():
    return response.download(request, db)

@auth.requires_login()
def remove_image():

    Validator.admin()
    Validator.valide_args(1)

    mFile = db.tbHomePageSlideResources(request.args[0])

    MyFile(request.folder + 'uploads/'+mFile.mThumbnail).remove()
    MyFile(request.folder + 'uploads/'+mFile.mImage).remove()

    db(db.tbHomePageSlideResources.id==mFile.id).delete()

    MessageBox(T('File') + ' <b>'+mFile.mLabel+'</b> ' + T('removed!')).showSuccess()
    redirect(URL('manager', 'home_slide_resources'))
    pass
