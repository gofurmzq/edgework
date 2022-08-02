"""Installation script for flask-api-with-jwt application."""
from pathlib import Path
from pyclbr import readmodule_ex
from setuptools import setup, find_packages

DESCRIPTION = (
    "Boileplate Flask API with  Flask-RESTx, SQLAlchemy, pytest, flake8, "
    "tox configured"
)
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Muhamad Gofur Muzaqi"
AUTHOR_EMAIL = "muhamadgofurmuzaqi@gmail.com"
PROJECT_URLS = {
    "Documentation": "https://github.com/gofurmzq/flask-api-with-jwt/blob/main/README.md",
    "Bug Tracker": "https://github.com/gofurmzq/edgework/issues",
    "Source Code": "https://github.com/gofurmzq/edgework"
}
INSTALL_REQUIRES = [
    "Flask==2.1.0",
    "flask-restx",
    "Flask-Caching",
    "python-dotenv",
    "Werkzeug==2.1.2"
]
EXTRAS_REQUIRE = {
    "dev": [
        "pandas",
        "gunicorn"
    ]
}

setup(
    name="edgerworks",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="Apache License",
    url="https://github.com/gofurmzq/flask-api-with-jwt",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)