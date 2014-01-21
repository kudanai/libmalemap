#!/usr/bin/env python

"""libmlemap.py: provides a pythonic interface for http://male-map.com
	2013 - @kudanai. For developmental use only. Do not use in production"""

import requests
from bs4 import BeautifulSoup

__MBaseURL__ = "http://male-map.com/"		# base url
__MSearchURL__ = "ajax_searchaddress.php"	# q=xxxx
__MCatURL__ = "ajax_categorylocations.php"	# cid=2
__MFetchURL__ = "ajax_fetch_address.php"	# pl=xxx

class MaleMap():
	def __init__(self):
		pass

	def __get_response(self,url,params=None):
		response = requests.get(__MBaseURL__+url, params=params)
		if response.status_code==200:
			if response.text.startswith('Address not found') or response.text.startswith('Address Not Found') or 'Invalid Data' in response.text:
				return None

			return response
		else:
			return None

	def query(self,query):
		"""search the site for closest match to :query and returns a list or None"""
		response = self.__get_response(__MSearchURL__,{'q':query})
		if not response:
			return None

		data=response.text
		data=[line.strip() for line in data.split('\n') if line.strip()]
		return data


	def fetch(self,query):
		"""fetch the location data for specified :query. returns a dict or None"""
		response = self.__get_response(__MFetchURL__,{'pl':query})
		if not response:
			return None

		soup = BeautifulSoup(response.text,'xml')
		location = soup("location")
		return location[0].attrs


	def fetch_category_listing(self):
		"""not implemented:"""
		"""gets a listing of categories in a dict of category_id:category_name"""
		pass


	def fetch_category(self,query):
		"""returns a list of location dicts for the given category"""

		response = self.__get_response(__MCatURL__,{'cid':query})
		if not response:
			return None

		spam = []
		soup = BeautifulSoup(response.text)
		for location in soup('location'):
			spam.append(location.attrs)

		return spam