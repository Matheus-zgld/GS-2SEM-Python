# 🧠 Projeto SYNAPSE - Global Solution 2025
**Tema:** O Futuro do Trabalho

---

## 👥 Integrante

* **Nome:** Matheus Henrique Ferreira Camargo da Silva
* **RM:** 566232

---

## 🎥 Link para o Vídeo
O vídeo de demonstração do sistema SYNAPSE em funcionamento está disponível no link abaixo:

> **[https://youtu.be/99ZBT0h5VSE]**

---

## 🎯 O Problema
O tema "O Futuro do Trabalho" aponta para uma transformação global impulsionada pela Inteligência Artificial, robótica e automação. Este cenário cria "novas oportunidades", mas também "desafios inéditos". O Fórum Econômico Mundial estima que quase um quarto das profissões mudará radicalmente até 2027.

Isso gera uma **"necessidade urgente de requalificação contínua"** (*reskilling* e *upskilling*) para que os trabalhadores permaneçam relevantes.

> O principal problema é a lacuna (o "gap") entre as habilidades atuais da força de trabalho e as competências exigidas pelas novas profissões. Se não for gerenciada, essa transição corre o risco de "exacerbar desigualdades", deixando para trás populações vulneráveis e indo contra os Objetivos de Desenvolvimento Sustentável (ODS) da ONU.

O desafio é: como criar uma solução que prepare as pessoas de forma prática, conectada e acessível?

## 💡 A Solução: SYNAPSE
O **SYNAPSE** é um protótipo funcional de uma **rede social profissional focada em requalificação (*reskilling*)**, desenvolvida inteiramente em Python.

Em vez de apenas "conectar pessoas", o SYNAPSE foi projetado para **conectar habilidades a oportunidades** e **aprendizes a mentores**. Ele atua como uma "bússola de carreira" que guia o usuário ativamente através da transição profissional, transformando a incerteza do futuro em um plano de ação comunitário.

A plataforma é construída sobre um ecossistema de funcionalidades que se entrelaçam com o tema:

1.  👤 **Perfis Baseados em Habilidades:** O núcleo do perfil do usuário é seu portfólio de *skills*, que podem ser **endossadas (⭐)** pela comunidade, validando sua competência.
2.  📰 **Rede Social Ativa:** Os usuários podem seguir profissionais, criar posts (com limite de 500 caracteres), curtir (❤️) e comentar (💬), fomentando uma "comunidade de aprendizagem colaborativa".
3.  🗂️ **Hub de Projetos:** Usuários podem cadastrar projetos (como este GS) e *etiquetar as habilidades* que usaram, criando um portfólio prático que prova sua competência.
4.  🗺️ **Trilhas de Aprendizagem (Learning Paths):** A funcionalidade central. Usuários podem criar e compartilhar "Trilhas de Aprendizagem" públicas (ex: "Minha jornada para virar Analista de Ética de IA"), conectando cursos e projetos.
5.  🚀 **Análise de Carreira (Módulos de IA):**
    * **Análise de Skill Gap:** O usuário compara suas habilidades com as de "profissões do futuro" (cadastradas no sistema) e vê exatamente o que falta.
    * **Consultor de IA (Bot):** Um bot simulado que analisa o cargo atual do usuário, informa o "risco de automação" e sugere proativamente carreiras alternativas para migração.

---

## 🛠️ Diferencial e Requisitos Técnicos
O diferencial do SYNAPSE é ser uma **ferramenta de ação prática e gamificada**, e não uma plataforma passiva. Ele não apenas informa o usuário sobre o problema, mas o guia ativamente na solução.

### Alinhamento Temático
* Aborda diretamente os pilares do desafio: "novas formas de aprendizagem", "requalificação (reskilling)", "uso de IA como parceira", "gamifique experiências" e "comunidades de aprendizagem".
* **Foco na Prática:** A inclusão de "Hub de Projetos" e "Trilhas de Aprendizagem" foca em demonstrar competência prática, não apenas certificados.

### ✅ Conformidade Técnica (100%)
O projeto cumpre rigorosamente **todos** os requisitos técnicos solicitados no PDF da disciplina:

* **Estrutura de Menu:** Implementa uma estrutura de menu completa, clara e navegável, com múltiplos níveis (ex: Menu Principal, Menu Logado, Painel Admin).
* **Validações:** Realiza validações em todas as entradas de dados do usuário (ex: username não pode ter espaço, e-mail deve conter "@", senha com tamanho mínimo, posts com limite de caracteres).
* **Tratamento de Exceções:** Aplica `try-except` (ex: na `obter_escolha_menu`) para evitar que o programa quebre com entradas inválidas (como letras em vez de números).
* **Estruturas de Decisão e Repetição:** Utiliza extensivamente `if/elif/else`, `while` (para menus e validações) e `for` (para iterar sobre feeds, listas de usuários, etc.).
* **Funções Modulares:** É 100% modularizado. Todo o código é organizado em dezenas de funções com passagem de parâmetros e retorno (ex: `realizar_login(db)`, `criar_post(username, db)`).
* **Dicionários como Base de Dados:** **Toda** a base de dados do sistema (usuários, posts, comentários, curtidas, conexões, projetos, trilhas, cursos, profissões) é gerenciada através de dicionários complexos e aninhados.
* **Usabilidade:** Garante uma boa experiência de usuário com um design de console limpo, feedback constante (mensagens de erro e sucesso) e navegação intuitiva.
