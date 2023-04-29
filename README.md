# Single Page Application - Personagens da Marvel

## O que é?

O projeto é uma SPA (Single Page Application) que exibe dados a partir de requisições à API da Marvel.

## Funcionalidades:

* Ver todos os personagens, suas descrições e imagens (quando disponíveis)

* Visualizar apenas alguns personagens (paginação)

* Avançar a visualização dos personagens (paginação)

* Pesquisar personagens de forma individual, visualizando sua foto, descrição e lista de quadrinhos (quando disponível)

* Buscar o personagem no Google

## Linguagens

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
* Python

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
* HTML

![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
* CSS

![JAVASCRIPT](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
* JavaScript

## Bibliotecas e framework

Além disso, foi utilizada a biblioteca/micro framework Flask (Python) para facilitar o desenvolvimento do site.

Para utilizar o projeto é necessário realizar a instalação de algumas bibliotecas externas, sendo elas:

`Flask`

`Hashlib`

`Request`

## Como usar?

**Instalando (passo a passo):**

1. Faça o download dos arquivos

2. Instale as bibliotecas necessárias (flask, hashlib e request)

3. Execute o arquivo `app.py`

Realize a instalação das bibliotecas através do uso de pip:

```pip install Flask```

```pip install hashlib```

```pip install request```

É possível ter acesso a todos os requerimentos da aplicação no arquivo [requirements.txt](/requirements.txt)

OBS: Caso deseje trocar a chave da API pela sua, é possível realizar a alteração no arquivo `consumer.py` nas variáveis `public_key` e `private_key`.

## Imagens


## API da Marvel

A API da Marvel é gratuita. Para utilizá-la é preciso ter uma conta e chaves (pública e privada).
[Marvel for Developers](https://developers.marvel.com)
