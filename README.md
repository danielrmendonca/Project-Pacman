<h1 align="center">🎮 Project Pac-Man</h1>

<p align="center">Jogo inspirado no funcionamento do clássico Pac-Man, mas com um design adaptado e único criado por nosso grupo. </p>

---

## 👥 Membros da Equipe

<div align="center">
  
| Integrante | Funções |
|-----------|------|
| Daniel Ramos `<drm3>`  | Telas, transições, menus, resultados, loop principal, documentação. |
| Hugo Jose `<hjbc>`   | Interface da pontuação, mecânicas de jogo do spawn. |
| Gabriel Nascimento `<gnss>`   | Sprites, design, mapas, integração do design com o código. |
| Gustavo Ferreira `<glfb>`    | Algoritmo principal do jogo, mecânica do jogo em geral, perseguição, coletáveis, mapa. |
| Rodrigo Neves `<ran>`    | Design, sprites, visual, artes, telas. |
| Wallace Leão `<wgsl>`    | Mecânica do jogo em geral, colisões, coletáveis, buffs. |

</div>

---

## 🎮 Sobre o Jogo

O **Project Pac-Man** é uma releitura moderna do clássico jogo de arcade. Se baseando no coceito de orientação a objetos, consiste em conseguir coletar 3 tipos de itens antes de ser pego pelo perseguidor..

---

## 🔧 Elementos do Jogo

### 🟡 Objeto Principal
O jogador controla um personagem principal que deve navegar por uma sala de aula, adquirindo os coletáveis: caneta, ajuda dos monitores e livros enquanto evita o contato do perseguidor.

### 🍒 Coletáveis

#### 🖊️ Canetas
Coletável básico, o principal para a condição de vitória.

#### 🧑‍🏫 Ajuda dos monitores.
Colétavel de velocidade.

#### 📗 Livro de matemática discreta
Coletável de intangibilidade.

### 👾 Perseguidor
Um NPC que patrulha o mapa com o objetivo de capturar o jogador. O contato com ele resulta em falha. Seu comportamento é parcialmente aleatório, com padrões de perseguição baseados na posição do jogador.

---

## 🧰 Bibliotecas e Ferramentas Utilizadas

### 📚 Bibliotecas

#### `pygame`
Biblioteca principal usada para desenvolvimento de jogos em Python.

**Instalação:**
```bash
pip install pygame
```

#### `pytmx`
Biblioteca responsável por carregar os mapas.

**Instalação:**
```bash
pip install pytmx
```

#### `sys`
Biblioteca padrão do Python utilizada para lidar com argumentos de linha de comando e encerrar o programa.  
> Não requer instalação.

#### `random`
Utilizada para gerar comportamentos aleatórios.  
> Não requer instalação.

#### `os`
Biblioteca padrão usada para interação com o sistema operacional, como manipulação de arquivos e diretórios.  
> Não requer instalação.

---

### 🛠️ Ferramentas

#### Miro
Ferramenta para brainstorm inicial e divisao de funções levando em consideração grau de urgência.

#### Visual Studio Code
Editor de código-fonte utilizado para desenvolvimento do projeto. Oferece integração com Git, extensões úteis e um ambiente amigável para desenvolvimento em equipe e organizado para aplicação de POO.

#### Git
Sistema de controle de versão utilizado para gerenciar alterações no código, permitindo colaboração simultânea entre os membros da equipe de forma organizada, foi o sistema utilizado pelo grupo para organização e avanço no projeto.

#### GitHub
Plataforma onde o repositório do projeto foi hospedado. Facilitou a colaboração, controle de versões, issues e visualização do progresso, com o github desktop, foi possível aproveitar muito bem a integração com git.

#### Tiled
Criador de mapas.

#### Pixel Art
Criar as artes dos personagens e coletáveis.

---

## 🧠 Conceitos

*Foi necessário para o projeto diversos conceitos estudados na disciplina, como repetições, funções, listas, tuplas, entre outros. O principal e fundamental foi a noção incial de orientação a objetos.*

### 📘 Lições Aprendidas

- Trabalho em equipe e divisão de tarefas com uso do Git e GitHub.
- Manipulação de mapas `.tmx`.
- Implementação de lógica de jogo com `pygame`.
- Aplicação prática de orientação a objetos no desenvolvimento de jogos.
- Integração de assets visuais com o código (sprites, mapas, elementos visuais).

---

## 📸 Capturas de Tela

![Menu principal](imagens/menu_principal.png)
![Gameplay](imagens/gameplay.png)
