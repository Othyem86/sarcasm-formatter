from setuptools import setup, find_packages

packages = find_packages()

setup(
	name="sarcasm-formatter",
	version="9999",
	description = "Format text alternating between lower-case and upper-case characters.",
	author = "Emil Föger",
	url = "https://github.com/Othyem86/sarcasm-formatter",
	keywords = ["sarcasm", "formatter", "meme"],
	classifiers = [],
	install_requires = [],
	provides = ["sarcasm_formatter"],
	packages = packages,
	extras_require = {
		},
	entry_points = {'console_scripts' : \
			['sarcasm = cli:main']
		},
	)
