from setuptools import setup, find_packages

setup(
    name='setup',
    version='1.1',
    packages=find_packages(),
    scripts=["subtera.py", "banner.py", "text.py", "sendmsg.py"],
    url='',
    license='',
    author='Ovusi Norbert',
    author_email='jakpornobert@gmail.com',
    description='An application to provide anonymity when sending emails'
)
