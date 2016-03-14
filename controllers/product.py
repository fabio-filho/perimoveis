# -*- coding: utf-8 -*-




def index():

    return dict(mRows=db(db.tbProducts.id>0).select())



@auth.requires_login()
def add():
    Validator.admin()

    mForm=SQLFORM(db.tbProducts, submit_button=T('Add a product'))

    Validator.form_process(mForm, URL('product', 'index'))

    return dict(mForm=mForm)



@auth.requires_login()
def edit():
    Validator.admin()
    Validator.valide_args(1)

    return dict(mForm=SQLFORM(db.tbProducts,
                db.tbProducts(request.args[0]),
                submit_button=T('Save changes')))
