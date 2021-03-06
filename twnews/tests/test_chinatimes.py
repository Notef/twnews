"""
中時電子報單元測試
"""

import unittest
from twnews.soup import NewsSoup, pkgdir

#@unittest.skip
class TestChinatimes(unittest.TestCase):

    def setUp(self):
        self.url = 'https://www.chinatimes.com/realtimenews/20180916001767-260402'
        self.dtf = '%Y-%m-%d %H:%M:%S'

    def test_01_sample(self):
        """
        測試中時電子報樣本
        """
        nsoup = NewsSoup(pkgdir + '/samples/chinatimes.html.gz', mobile=False)
        self.assertEqual('chinatimes', nsoup.channel)
        self.assertIn('悲慟！北市士林年邁母子 住處上吊自殺身亡', nsoup.title())
        self.assertEqual('2018-09-16 15:31:00', nsoup.date().strftime(self.dtf))
        self.assertEqual('謝明俊', nsoup.author())
        self.assertIn('北市士林區葫蘆街一處民宅', nsoup.contents())

    def test_02_desktop(self):
        """
        測試中時電子報桌面版
        """
        nsoup = NewsSoup(self.url, refresh=True, mobile=False)
        self.assertEqual('chinatimes', nsoup.channel)
        self.assertIn('悲慟！北市士林年邁母子 住處上吊自殺身亡', nsoup.title())
        self.assertEqual('2018-09-16 15:31:00', nsoup.date().strftime(self.dtf))
        self.assertEqual('謝明俊', nsoup.author())
        self.assertIn('北市士林區葫蘆街一處民宅', nsoup.contents())

    def test_03_mobile(self):
        """
        測試中時電子報行動版
        """
        nsoup = NewsSoup(self.url, refresh=True, mobile=True)
        self.assertEqual('chinatimes', nsoup.channel)
        self.assertIn('悲慟！北市士林年邁母子 住處上吊自殺身亡', nsoup.title())
        self.assertEqual('2018-09-16 15:31:00', nsoup.date().strftime(self.dtf))
        self.assertEqual('謝明俊', nsoup.author())
        self.assertIn('北市士林區葫蘆街一處民宅', nsoup.contents())
