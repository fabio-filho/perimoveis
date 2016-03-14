# -*- coding: utf-8 -*-
from lib_validator import IS_MONEY


db.define_table('tbHomePageSlideResources',
            Field('mTempImage', 'upload', label=T('Image'), requires=IS_NOT_EMPTY()),
            Field('mImage', 'string', label=T('Image'), readable=False, writable=False),
            Field('mThumbnail', 'string', label=T('Thumbnail'), readable=False, writable=False),
            Field('mLabel', 'string', label=T('Label'), requires=IS_NOT_EMPTY()),
            auth.signature
)



db.define_table('tbProducts',
            Field('mLabel', 'string', label=T('Label'), requires=IS_NOT_EMPTY()),
            Field('mPrice', 'float', label=T('Price'), requires= IS_MONEY()),
            Field('mPaymentInstallments', 'integer',
                        requires=IS_IN_SET([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
                        #labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                        label=T('Payment Installments')),
            Field('mIsVisibleToShelf', 'boolean', default=False, writable=False, readable=False),
            auth.signature
)
