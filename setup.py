from setuptools import setup, find_packages
import os

version = '1.0.1dp'

requires = [
    'setuptools',
    'tooz',
    'retrying',
    'jmespath',
    'enum',
    'jsonschema',
]

test_requires = requires + [
    'mock',
    'webtest',
    'pytest',
    'python-coveralls',
]

docs_requires = requires + [
    'sphinxcontrib-httpdomain',
]

entry_points = {
    'openprocurement.bridge.basic.handlers': [
        'common = openprocurement.bridge.rbot.handlers:RendererBot',
    ],
    'openprocurement.bridge.basic.filter_plugins': [
        'contract_data = openprocurement.bridge.rbot.filters:ContractDataFilter'
    ],

}

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

setup(name='openprocurement.bridge.rbot',
      version=version,
      description="",
      long_description=README,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
      ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/openprocurement/openprocurement.bridge.rbot',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.bridge'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={'test': test_requires, 'docs': docs_requires},
      test_suite="openprocurement.bridge.rbot.tests.main.suite",
      entry_points=entry_points)
