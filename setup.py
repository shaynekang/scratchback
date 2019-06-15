import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='scratchback', 
     version='0.1',
     author="DS School",
     author_email="support@dsschool.co.kr",
     description="Crawler for Proggraming Course",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/shaynekang/scratchback",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
