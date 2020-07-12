import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="email_fake-Mehrbod2002",
    version="0.0.1",
    author="Mehrbod Akhlaghpour",
    author_email="m9.akhlaghpoor@gmail.com",
    description="generate tem emails",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mehrbod2002/email_fake.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
