#!/usr/bin/env python3
import argparse
import os
import addoninfo
from gmpublish import GmPublish

def main():
	# Define command line parameters
	parser = argparse.ArgumentParser(description = "Garry's mod workshop cli wrapper.")
	args = parser.parse_args()
	curdir = os.getcwd()

	# Try to get the addon information
	try:
		addon = addoninfo.get_addon_info(addoninfo.find_addon(curdir))
		publisher = GmPublish(addon)
	except addoninfo.AddonNotFoundError as err:
		print(err)
		return

	if addon.has_workshop_id():
		pass
	else:
		pass

if __name__ == '__main__':
	main()