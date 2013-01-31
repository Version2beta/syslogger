from distutils.core import setup

setup(
    name='Syslogger',
    version='0.0.2',
    author='Rob Martin @version2beta',
    author_email='rob@version2beta.com',
    packages=['syslogger'],
    scripts=[],
    url='http://pypi.python.org/pypi/syslogger/',
    license='LICENSE.txt',
    description='Log messages by facility and level.',
    long_description=open('README.md').read(),
    install_requires=[],
    package_data={
        '': ['*.dist'],
      },
    entry_points={
        'console_scripts': [
          'syslogger = syslogger.syslogger:main',
        ],
      },
)
