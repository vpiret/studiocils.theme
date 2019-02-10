# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from studiocils.theme.testing import STUDIOCILS_THEME_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that studiocils.theme is properly installed."""

    layer = STUDIOCILS_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if studiocils.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'studiocils.theme'))

    def test_browserlayer(self):
        """Test that IStudiocilsThemeLayer is registered."""
        from studiocils.theme.interfaces import (
            IStudiocilsThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IStudiocilsThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = STUDIOCILS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['studiocils.theme'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if studiocils.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'studiocils.theme'))

    def test_browserlayer_removed(self):
        """Test that IStudiocilsThemeLayer is removed."""
        from studiocils.theme.interfaces import \
            IStudiocilsThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IStudiocilsThemeLayer,
            utils.registered_layers(),
        )
