# 👩‍💻 Projeto para seleção de estágio backend python

# PROJETO MINI-TWITTER

by b2bit

  

Bem-vindo(a) ao projeto de seleção para backend developers da b2bit! Neste projeto, vamos abordar algumas técnicas e tecnologias que você utilizará no seu dia-a-dia aqui na empresa 😉. Abaixo, segue um índice sobre este documento.

  

  

# **🏁 DESCRIÇÃO**

Implementar uma API REST em que um usuário possa realizar um cadastro, publicar Posts e ver as publicações de outros usuários.

  

# **📄 REQUISITOS TÉCNICOS**

*   Criar a aplicação em formato REST;
*   Python 3;
*   Django REST Framework (preferencialmente). Mas pode utilizar qualquer framework em Python. Queremos avaliar se você conhece os conceitos da web;
*   Banco de dados: relacional. Preferencialmente PostgreSQL;

  

**Diferencial**

*   [Diagrama entidade relacional](https://lucid.app/lucidchart/84cc1690-6063-440b-96f8-ce066dcfda1a/edit?viewport_loc=-11%2C-11%2C2219%2C1067%2C0_0&invitationId=inv_41eb459e-0619-4a1b-ad02-b6c706ea817f) do banco de dados utilizado no projeto;

  

# 👨🏼‍🏫 **CASOS DE USO**

## **CASO 1: Cadastro de usuário**

O ator faz o cadastro no sistema através da API. Como usuário, ele deve poder fazer o cadastro, para que ele tenha acesso ao Login. Use os campos que achar necessário para a definição do modelo do usuário.

  

## **CASO 2: Autenticação (Login)**

O ator deve ser autenticado no sistema através de um Token. Como usuário, ele deve poder fazer login, para que ele tenha acesso ao sistema. Este token deve ter uma data de expiração.

  

## **CASO 3: Fazer uma publicação**

O ator cria um post. Esta publicação é persistida no sistema. Como usuário, ele deve poder criar uma publicação, para que possa ser vista por outros usuários do sistema.

  

## **CASO 4: Feed geral**

*   O ator deve receber, no formato JSON, o feed dos últimos 10 posts utilizando paginação.

  

  

# **📜 Regras de negócio**

*   O usuário não deve ver os próprios Posts.

  

  

# 💯 EXTRAS

Entregas extras que serão muito bem vistas.

*   Deploy do projeto (colocar em produção);
*   Upload de arquivos estáticos;
*   Servir arquivos estáticos. Preferencialmente por uma CDN. Indicamos o AWS S3;

  

  

# ✅ Checklist

- [x] Caso de uso 1
- [x] Caso de uso 2
- [x] Caso de uso 3
- [x] Caso de uso 4

  

# 🔗 Resources & external links

| <br>**RESOURCE**<br> | <br>**LINK**<br> |
| ---| --- |
| Django | [https://www.djangoproject.com/](https://www.djangoproject.com/) |
| Django REST Framework | [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/) |
| ERD: Diagrama Entidade Relacional | [https://www.lucidchart.com/pages/pt/o-que-e-diagrama-entidade-relacionamento](https://www.lucidchart.com/pages/pt/o-que-e-diagrama-entidade-relacionamento) |
| Testes em Django | [https://docs.djangoproject.com/en/4.0/intro/tutorial05/](https://docs.djangoproject.com/en/4.0/intro/tutorial05/) |
