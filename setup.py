from setuptools import setup

setup(
    name="asyncinit",
    version="0.2.4",
    description="Class decorator to enable async __init__",
    author="Mick Koch",
    license="MIT",
    author_email="mick@kochm.co",
    url="https://github.com/kchmck/pyasyncinit",
    packages=["asyncinit"],
    python_requires=">=3.5",
    extras_require={
        "dev": [
            "pylint~=2.1",
            "pytest~=3.6",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="async init asyncio",
)
