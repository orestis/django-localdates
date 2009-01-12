import os
from setuptools import setup

def find_files(directory, suffix_list):
    for root, dirs, files in os.walk(directory):
        relative_root = root[len(directory)+1:]
        for f in files:
            for suffix in suffix_list:
                if f.endswith(suffix):
                    yield os.path.join(relative_root, f)

package_data = list(find_files('localdates', ['.po', '.mo', '.html']))

kwargs = {
    'name' : 'localdates',
    'version' : 'dev',
    'description' : 'An addition to django that allows better presentation of date strings in a local way.',
    'author' : 'Orestis Markou',
    'author_email' : 'orestis@orestis.gr',
    'url' : 'http://code.google.com/p/django-localdates/',
    'packages' : ['localdates',
                  'localdates.templatetags'],
    'package_data': { 'localdates': package_data},
    'classifiers' : ['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Utilities'],
}

setup(**kwargs)
