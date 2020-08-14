# -*- coding: utf-8 -*-
from udemy.testaddon.testing import UDEMY_TESTADDON_FUNCTIONAL_TESTING
from udemy.testaddon.testing import UDEMY_TESTADDON_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = UDEMY_TESTADDON_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_youtube_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='youtube'
        )
        self.assertTrue(view.__name__ == 'youtube')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in youtube'
        # )

    def test_youtube_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='youtube'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = UDEMY_TESTADDON_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
