# -*- coding: utf-8 -*-




def index():

    mRowsTemp = db(db.tbProducts.id>0).select(orderby=db.tbProducts.mName)
    mThumbnailList = []
    mRows = []
    for mIndex in range(0, len(mRowsTemp)):
        mResult = db(db.tbProductsImageUploads.mProduct==mRowsTemp[mIndex].id).select()
        if len(mResult) > 0:
            mThumbnailList.append(mResult.first().mThumbnail)
            mRows.append(mRowsTemp[mIndex])

    return dict(mRows=mRows, mThumbnailList=mThumbnailList)


def view():
    Validator.valide_args(1)

    mImages = db(db.tbProductsImageUploads.mProduct== request.args[0]).select()
    if len(mImages) <= 0:
        redirect(URL('app', 'index'))

    return dict(mRow=db.tbProducts(request.args[0]), mImages=mImages)

@auth.requires_login()
def manager():
    Validator.admin()
    return dict(mRows=db(db.tbProducts.id>0).select(orderby=db.tbProducts.mName))



@auth.requires_login()
def add():
    Validator.admin()

    mForm=SQLFORM(db.tbProducts, submit_button=T('Save and add an image'))

    Validator.form_process(mForm, mUrl=None, mOnAccepted=add_accepted)

    return dict(mForm=mForm)



@auth.requires_login()
def add_accepted(mForm):
    redirect(URL('product', 'edit', args=[mForm.vars.id]))
    pass


@auth.requires_login()
def edit():
    Validator.admin()
    Validator.valide_args(1)

    db.tbProducts.id.readable = False
    db.tbProducts.mIsVisibleToShelf.writable = True

    mForm=SQLFORM(db.tbProducts,
            db.tbProducts(request.args[0]),
            submit_button=T('Save changes'))

    Validator.form_process(mForm, URL('product', 'edit', args=[request.args[0]]))

    mImages = db(db.tbProductsImageUploads.mProduct==request.args[0]).select()

    return dict(mForm=mForm, mRows=mImages, mFormImage=get_image_add_form(request.args[0]))




@auth.requires_login()
def get_image_add_form(mProductId):
      from lib_image import MyImage
      Validator.admin()

      mForm = FORM(LABEL(T("File")+"(s):"), INPUT(_id="tbProductsImageUploads_mTempImage", _name='mFiles', _type='file', _multiple=''),
          BR(),INPUT(_class="btn btn-primary", _type='submit', _value=T("Send images")))

      if mForm.accepts(request.vars, formname="mForm"):

        if hasattr(request.vars, 'mFiles'):

          mFiles = request.vars['mFiles']
          if mFiles == '':
              redirect(URL('product', 'edit', args=[mProductId]))

          if not isinstance(mFiles, list):
            mFiles = [mFiles]

          if len(mFiles) > 0:

            for f in mFiles:
              mFile = db.tbProductsImageUploads.mFile.store(f, f.filename)
              db.tbProductsImageUploads.insert(mFile=mFile, mFilename=f.filename,
                                mProduct=mProductId, mThumbnail=MyImage.transform(mFile, MyImage.THUMBNAIL_DIMENSION))
              db.commit()

            redirect(URL('product', 'edit', args=[mProductId]))
          else:
            mForm.errors.mFiles = "No files selected"

      return mForm




@auth.requires_login()
def remove():

    Validator.admin()
    Validator.valide_args(1)

    mProduct = db.tbProducts(request.args[0])
    print "#============"
    print mProduct
    print len(db(db.tbProductsImageUploads.mProduct == mProduct.id).select())

    for mProductUpload in db(db.tbProductsImageUploads.mProduct == mProduct.id).select():
        print mProductUpload
        MyFile(request.folder + 'uploads/'+mProductUpload.mThumbnail).remove()

    db(db.tbProductsImageUploads.mProduct == mProduct.id).delete()
    db(db.tbProducts.id==mProduct.id).delete()

    redirect(URL('product', 'manager'))
    pass
