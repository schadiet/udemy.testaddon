# -*- coding: utf-8 -*-

from udemy.testaddon import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Youtube(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('youtube.pt')

    def __call__(self):
        # Implement your own actions:
        #self.msg = _(u'A small message')
        self.youtubelink = 'https://www.youtube-nocookie.com/embed/{}'.format(self.context.ytid)
        return self.index()
