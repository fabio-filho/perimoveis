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

    Validator().form_process(mForm, URL("manager", "home_slide_resources") )

    return dict(mForm=mForm)



def download():

    return response.download(request, db)
