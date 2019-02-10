# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import studiocils.theme


class StudiocilsThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=studiocils.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'studiocils.theme:default')


STUDIOCILS_THEME_FIXTURE = StudiocilsThemeLayer()


STUDIOCILS_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(STUDIOCILS_THEME_FIXTURE,),
    name='StudiocilsThemeLayer:IntegrationTesting'
)


STUDIOCILS_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(STUDIOCILS_THEME_FIXTURE,),
    name='StudiocilsThemeLayer:FunctionalTesting'
)


STUDIOCILS_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        STUDIOCILS_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='StudiocilsThemeLayer:AcceptanceTesting'
)
