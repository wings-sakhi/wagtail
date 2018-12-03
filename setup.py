import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
     name='wagtail-wings',  
     version='0.1',
     scripts=['wagtail'] ,
     author="Mukunth Krishnasagar",
     author_email="mukunth@wings.lc",
     description="A Custom wagtail package with encryption",
    #  long_description=long_description,
     long_description="Yet to be added",
     long_description_content_type="text/markdown",
     url="https://github.com/wings-sakhi/wagtail",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
