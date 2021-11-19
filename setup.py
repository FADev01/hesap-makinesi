from setuptools import setup, find_packages
with open("README.txt","r") as fh:
    long_description =fh.read()
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7',
]

setup(
  long_description=long_description,
  long_description_content_type="text/markdown",
  name='hesapmakinesi',
  version='1.0.1',
  description='Just a calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/FADev01/hesap-makinesi',  
  author='Furkan Akbulut',
  author_email='akbulutfurkanDEV@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='hesapmakinesi calculator', 
  packages=find_packages(),
  install_requires=[''] 
)