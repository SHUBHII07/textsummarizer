import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description =f.read()

__version__="0.0.0"

repo_name="textsummarizer"
author_name='SHUBHII07'
src_repo="TextSummarizer"
Author_email='shubhangi.sakarkar@gmail.com'
 
setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_name,
    author_email=Author_email,
    long_description=long_description,
    description="A samml package for NLP",
    long_description_content="text/markdown",
    url=f"https://github.com/{author_name}/{repo_name}",
    project_urls={
        "Bug Tracker":"https://github.com/{author_name}/{repo_name}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')

    )