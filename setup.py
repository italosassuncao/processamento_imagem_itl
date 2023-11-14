from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_imagem_itl",
    version="0.0.1",
    autor="Italo",
    email="italo18sil@gmail.com",
    descricao="Vazio",
    descricao_longa=page_description,
    descricao_longa_tipo_conteudo="text/markdown",
    url="https://github.com/italosassuncao/processamento_imagem_itl",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.6"
)
