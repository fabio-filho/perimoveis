# -*- coding: utf-8 -*-




db.define_table('tbHomePageSlideResources',
            Field('mFile', 'upload', label=T('Image'), requires=IS_NOT_EMPTY()),
            Field('mLabel', 'string', label=T('Label'), requires=IS_NOT_EMPTY()),
            auth.signature)
