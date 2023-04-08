from setuptools import setup
import os

VERSION = "0.1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="{{ cookiecutter.project_snake_case }}",
    description="{{ cookiecutter.project_description }}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",{% if cookiecutter.github_author_username %}
    author="{{ cookiecutter.author_name }}",{% endif %}{% if cookiecutter.github_author_username %}
    url="https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_kebab_case }}",
    project_urls={
        "Issues": "https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_kebab_case }}/issues",
        "CI": "https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_kebab_case }}/actions",
        "Changelog": "https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_kebab_case }}/releases",
    },{% endif %}
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["{{ cookiecutter.project_snake_case }}"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)