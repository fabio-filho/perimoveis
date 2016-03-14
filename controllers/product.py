# -*- coding: utf-8 -*-




def index():

    return dict(mRows=db(db.tbProducts.id>0).select())



@auth.requires_login()
def add():
    Validator.admin()

    mForm=SQLFORM(db.tbProducts, submit_button=T('Save and add an image'))

    Validator.form_process(mForm, URL('product', 'index'))

    return dict(mForm=mForm)



@auth.requires_login()
def edit():
    Validator.admin()
    Validator.valide_args(1)

    db.tbProducts.id.readable = False

    mForm=SQLFORM(db.tbProducts,
            db.tbProducts(request.args[0]),
            submit_button=T('Save changes'))

    Validator.form_process(mForm, URL('product', 'index'))

    mImages = db(db.tbProductsUploads.mProduct==request.args[0]).select()

    return dict(mForm=mForm, mImages=mImages,mFormImage=get_image_add_form(request.args[0]))




@auth.requires_login()
def get_image_add_form(mProductId):

      Validator.admin()

      mForm = FORM(LABEL(T("File")+"(s):"), INPUT(_name='mFiles', _type='file', _multiple=''),
          BR(),INPUT(_type='submit', _value=T("Send images")))

      if mForm.accepts(request.vars, formname="mForm"):

        if hasattr(request.vars, 'mFiles'):

          #fix this method to accepts one file
          #if isinstance(e, list):
          print '()())()()()()()()', len(request.vars.mFiles)
          if len(request.vars.mFiles) > 0:
            mFiles = request.vars['mFiles']
            if not isinstance(mFiles, list):
              mFiles = [files]

            for f in mFiles:
              mFile = db.tbProductsUploads.mFile.store(f, f.filename)
              db.tbProductsUploads.insert(mFile=mFile, mFilename=f.filename, mProduct=mProductId)
              db.commit()

            #redirect(URL('product', 'index'))
          else:
            mForm.errors.mFiles = "No files selected"

      return mForm


@auth.requires_login()
def get_cut_image():

    Validator.admin()
    Validator.valide_args(1)

    from lib_image import MyImage
    #save file in a temp file and after remove it
    return MyImage.cut(URL('app', 'download', args=[db.tbProductsUploads(request.args[0]).mFile]))
