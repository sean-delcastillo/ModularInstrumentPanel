import argparse

def argparse_init() -> argparse.Namespace:
	"""Handles CLI arguments and returns argparse Namespace"""
	parser = argparse.ArgumentParser(description="Mips Selector and Exporter")
	parser.add_argument("-f", "--file",
				help="A toml file for profile creation",
				required=True
		)
	args = parser.parse_args()
	return args