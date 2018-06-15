import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='tiny-elastic-cli',
  version='0.1.4',
  author='Einar Otto Stangvik',
  author_email='einaros@gmail.com',
  description='A very tiny elasticsearch query cli',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/einaros/tiny-elastic-cli',
  packages=setuptools.find_packages(),
  classifiers=(
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ),
  scripts=['bin/elastic'],
  install_requires=[
    'certifi',
    'elasticsearch',
    'urllib3>=1.22'
  ]
)
