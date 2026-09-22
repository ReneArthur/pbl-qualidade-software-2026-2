# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** Qualidade Software Noite.

**Equipe:** Rene e Felipe 

**Data:** 22/09/2026

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| Rene | [Rene](https://github.com/ReneArthur) |
| Felipe | [Felipe Tatsuya Aso](https://github.com/asottsuy) |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Pesquisar por restaurante próximos | Cliente | Cliente terá muita dificuldade de escolher onde comer
| Explícita | Filtrar por nacionalidade de comidas | Cliente | Dificuldade em achar restaurantes que o cliente que comer no momento
| Implícita | Responsividade | Cliente | Seria muito difícil de usar o app no computador ou celular (telas diferentes)
| Implícita | Bom SEO | Restaurantes | A falta de um bom SEO num website pode dificultar a busca do site nos navegadores


### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

```
Resposta: Sim, se ele não for responsivo por exemplo, pode ser muito difícil ou até impossível usar o app para computador ou celular, ou monitores com uma resolução mais baixa, se isso acontecer as funcionalidades explícitas perdem o peso completamente por simplesmente serem inacessíveis para o cliente.
```

---

## 3. Tarefa 2: Exploração da aplicação

> Cada integrante deve explorar uma funcionalidade, realizando uma utilização esperada e uma utilização alternativa, inválida ou incompleta. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Rene | Favoritar um restaurante e ver na aba de “Meus favoritos” | Clicado em um restaurante, depois clicado no botão de “favoritar” depois navegado para a área de favoritos | O restaurante foi favoritado corretamente, e ele apareceu na listagem instantaneamente. | [ver evidência](evidencias/favoritar-restaurante-lista.mkv)
| Felipe | Filtro por palavra chave não funciona | Pesquisei o nome do ‘mexicana’ no filtro | Ao pesquisar por culinárias que estão no site, o filtro não retorna nenhum card | [ver evidência](evidencias/pesquisa-mexicana-vazio.png)


---

## 4. Tarefa 3: Requisitos e características de qualidade

> Cada integrante deve formular um requisito de qualidade relacionado à mesma funcionalidade explorada na Tarefa 2. Acrescentem ou removam linhas conforme o número de integrantes.

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Rene | Favoritar restaurante | Lista de restaurantes favoritados | É necessário ter uma listagem para poder ver os restaurantes favoritados. |  teste manual, favoritar um restaurante e navegar até a lista.
| Felipe | Filtrar restaurante | Listagem de restaurantes | Deve aparecer os restaurantes filtrados pela palavra chave | teste manual, digitar a palavra e clicar em buscar no filtro

---


## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
não utilizada