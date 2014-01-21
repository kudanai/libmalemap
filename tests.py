#!/usr/bin/env python

import unittest
import libmlemap

class TestSequenceFunctions(unittest.TestCase):

	def setUp(self):
		self.map = libmlemap.MaleMap()

	def testFetch(self):
		# teste valid queries are return with data
		self.failUnless(self.map.fetch('STEAM BLUE'),'valid query did not return data')
		self.failUnless(self.map.fetch_category('1'),'valid category did not return data')
		self.failUnless(len(self.map.fetch_category('1'))>1,'category listing returned only one item')

		# test that invalid queries return None
		self.assertEqual(self.map.fetch('STEAM BLUES'),None,'invalid query returned other than None')
		self.assertEqual(self.map.fetch_category('222'),None,'invalid query returned data')

	def testSearch(self):
		# test if valid search results return values
		self.failUnless(self.map.query('STEAM'),'valid search didnt return data')

		#test if invalid search returns None
		self.failIf(self.map.query('STEKFJLK#$#'),'invalid search returned other than None')


if __name__ == '__main__':
	unittest.main()