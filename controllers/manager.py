# -*- coding: utf-8 -*-





@auth.requires_login()
def index():

    return dict()



@auth.requires_login()
def home_slide_resources():

    return dict(mRows=db(db.tbHomePageSlideResources.id>0).select())


@auth.requires_login()
def add_home_slide_resource():

    mForm = SQLFORM(db.tbHomePageSlideResources, submit_button=T('Submit'))

    Validator.form_process(mForm, URL("manager", "home_slide_resources"), mOnAccepted=add_home_slide_resource_accepted)

    return dict(mForm=mForm)

@auth.requires_login()
def add_home_slide_resource_accepted(mForm):
    #Adding thumbnail.
    from lib_thumbnail import Thumbnail
    mRow = db.tbHomePageSlideResources(mForm.vars.id)
    db(db.tbHomePageSlideResources.id==mForm.vars.id).update(mThumbnail=Thumbnail.toThumbnail(mRow.mImage))
    pass


def download():
    return response.download(request, db)

def remove_image():

    Validator.valide_args(1)

    mFile = db.tbHomePageSlideResources(request.args[0])
    import os
    os.remove(request.folder + 'uploads/'+mFile.mThumbnail)

    db(db.tbHomePageSlideResources.id==mFile.id).delete()

    MessageBox(T('File') + ' <b>'+mFile.mLabel+'</b> ' + T('removed!')).showSuccess()
    redirect(URL('manager', 'home_slide_resources'))
    pass
