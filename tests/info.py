#!/usr/bin/env python

import auracle_test
import json


class TestInfo(auracle_test.TestCase):

    def testSingleInfoQuery(self):
        r = self.Auracle(['info', 'auracle-git'])
        self.assertEqual(r.process.returncode, 0)


    def testExitSuccessIfAtLeastOneFound(self):
        r = self.Auracle(['info', 'auracle-git', 'packagenotfoundbro'])
        self.assertEqual(r.process.returncode, 0)


    def testExitFailureOnNotFound(self):
        r = self.Auracle(['info', 'packagenotfoundbro'])
        self.assertNotEqual(r.process.returncode, 0)


    def testBadResponsesFromAur(self):
        r = self.Auracle(['info', '503'])
        self.assertNotEqual(r.process.returncode, 0)
        self.assertEqual('error: unexpected HTTP status code 503\n',
                r.process.stderr.decode())


if __name__ == '__main__':
    auracle_test.main()
