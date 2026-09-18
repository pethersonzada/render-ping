# Render Keep-Alive

[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/pethersonzada/render-ping/keep-alive.yml?style=flat-square&logo=github-actions&logoColor=white&label=Automation)](https://github.com/pethersonzada/render-ping/actions/workflows/keep-alive.yml)
[![Render](https://img.shields.io/badge/Render-Free%20Tier-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-00C7B7?style=flat-square&logo=opensourceinitiative&logoColor=white)](LICENSE)

Automação inteligente construída com GitHub Actions para eliminar o "cold start" (latência de inicialização) de serviços hospedados no plano gratuito do Render.

## Como Funciona

Como os servidores gratuitos do Render entram em modo de repouso após um período de inatividade, a primeira requisição do usuário sofre com um atraso perceptível enquanto o container acorda. Este projeto resolve isso de forma automatizada:

1. Um workflow do **GitHub Actions** dispara periodicamente de forma autônoma.
2. O robô executa um comando leve via `curl` na rota de verificação do backend.
3. O servidor permanece ativo e responsivo em tempo integral, garantindo performance instantânea para os usuários sem nenhum custo financeiro.

---

## Tecnologias Utilizadas

* **GitHub Actions** (para orquestração e execução do cron agendado)
* **cURL** (para requisições HTTP de verificação)

---

## Configuração do Workflow

O script está configurado no diretório `.github/workflows/keep-alive.yml` para rodar a cada 10 minutos de forma autônoma.
