# -*- coding: utf-8 -*-



db.define_table('tbHomePageSlideResources',
            Field('mTempImage', 'upload', label=T('Image'), requires=IS_NOT_EMPTY()),
            Field('mImage', 'string', label=T('Image'), readable=False, writable=False),
            Field('mThumbnail', 'string', label=T('Thumbnail'), readable=False, writable=False),
            Field('mLabel', 'string', label=T('Label'), requires=IS_NOT_EMPTY()),
            auth.signature)
