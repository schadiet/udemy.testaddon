# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plone.supermodel import model
from zope.schema import TextLine


class IYoutube(model.Schema):
    """ Marker interface for Youtube
    """
    ytid = TextLine(title=(u'Youtube ID'), description=u'Please Enter the ID of Your Youtube Video', required=True)
