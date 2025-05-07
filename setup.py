from setuptools import setup, find_packages

setup(
    name="Just_Light_Development",  
    version="0.1.0",
    author="Subhodip",
    author_email="noemail",
    description="It is a micro web framework for Python.It's designed for rapid prototyping and building lightweight web applications with minimal overhead.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Subhodip1307/Just_Light_Development",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10", 
    install_requires=[
        "Jinja2",  
        "uvicorn",  
      
    ],
)