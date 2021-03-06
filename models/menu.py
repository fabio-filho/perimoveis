# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.title_label = 'Peri Móveis'
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Peri Móveis <atendimento@ad-media.tv>'
response.meta.description = 'Peri Móveis'
response.meta.keywords = 'peri, moveis, perimoveis, estantes, bancos, madeira'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('app', 'index'), []),
    #(T('About'), False, URL('app', 'about'), []),
    (T('Contact'), False, URL('app', 'contact'), []),
    (T('Products'), False, URL('app', 'products'), []),
    (T('Account'), False, URL('manager', 'index'), [])
]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################
