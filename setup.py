import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="huggingface_dl",
    version="0.0.4",
    author="yanqiangmiffy",
    author_email="1185918903@qq.com",
    description=("Command-line program to download models from huggingface.co"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yanqiangmiffy/huggingface-dl",
    project_urls={
        "Bug Tracker": "https://github.com/yanqiangmiffy/huggingface-dl/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests","transformers>=4.13.0",
        "click>=0.4.4",
        "huggingface-hub>=0.8.1",
        "packaging>=21.3"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "huggingface_dl = huggingface_dl.__main__:main",
        ]
    }
)