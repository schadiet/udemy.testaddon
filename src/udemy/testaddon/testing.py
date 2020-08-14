# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import udemy.testaddon


class UdemyTestaddonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=udemy.testaddon)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'udemy.testaddon:default')


UDEMY_TESTADDON_FIXTURE = UdemyTestaddonLayer()


UDEMY_TESTADDON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UDEMY_TESTADDON_FIXTURE,),
    name='UdemyTestaddonLayer:IntegrationTesting',
)


UDEMY_TESTADDON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UDEMY_TESTADDON_FIXTURE,),
    name='UdemyTestaddonLayer:FunctionalTesting',
)


UDEMY_TESTADDON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UDEMY_TESTADDON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='UdemyTestaddonLayer:AcceptanceTesting',
)
