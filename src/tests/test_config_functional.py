"""
Various tests for config
"""

import os
import unittest
import tempfile

from .test_process import TestProcessProto
from pybitmessage.bmconfigparser import BMConfigParser


class TestProcessConfig(TestProcessProto):
    """A test case for keys.dat"""
    home = tempfile.mkdtemp()

    def test_config_defaults(self):
        """Test settings in the generated config"""
        self._stop_process()
        self._kill_process()
        config = BMConfigParser()
        config.read(os.path.join(self.home, 'keys.dat'))

        self.assertEqual(config.safeGetInt(
            'bitmessagesettings', 'settingsversion'), 10)
        self.assertEqual(config.safeGetInt(
            'bitmessagesettings', 'port'), 8444)
        # don't connect
        self.assertTrue(config.safeGetBoolean(
            'bitmessagesettings', 'dontconnect'))
        # API disabled
        self.assertFalse(config.safeGetBoolean(
            'bitmessagesettings', 'apienabled'))

        # extralowdifficulty is false
        self.assertEqual(config.safeGetInt(
            'bitmessagesettings', 'defaultnoncetrialsperbyte'), 1000)
        self.assertEqual(config.safeGetInt(
            'bitmessagesettings', 'defaultpayloadlengthextrabytes'), 1000)
