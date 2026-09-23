# Atividade 2: Organização da Qualidade no LocalEats

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

**Elemento de Competência:** Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

---

## 2. Tarefa 1: Diagnóstico da situação

### 2.1 Problemas organizacionais

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Funcionalidades chegam aos usuários com defeitos; | Produto sem conformidade, logo, insatisfação dos clientes 
| Os critérios para considerar uma funcionalidade pronta não estão claros; | Má organização do time, acúmulo de bugs, processos lentos.
| Algumas atividades são realizadas por mais de uma pessoa, enquanto outras não possuem responsável definido. |  Tempo e esforço perdido



### 2.2 Responsabilidade pela qualidade

**A qualidade do LocalEats deve ser responsabilidade exclusiva do profissional de QA? Justifiquem.**

```
resposta: Não, pois os programadores e implementadores também devem trabalhar juntos para montar pipelines efetivas, e também testes automatizados, para assegurar que nenhuma falha passe. A pipeline de desenvolvimento e integração deve funcionar bem com os testes e o QA para permitir isso.
```

---

## 3. Tarefa 2: Papéis e competências

> Cada integrante deve ser responsável pela análise de pelo menos um papel. Acrescentem ou removam linhas conforme a composição da equipe e os papéis escolhidos.

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Rene | DevOps | Automatizar a integração e implementação de código, com testes automatizados, logs de auditoria, políticas de implementação, e plano automático para reverter a implementação caso necessário. | Trabalhar bem com git, docker, algum tipo de criador de pipeline (tipo github actions), entender sobre nuvem, testes automatizados. | Conversar bem com pessoas de diferentes áreas (programadores, técnicos de nuvem e stakeholders). Ensinar sobre pipeline.
| Felipe | Liderança Técnica | Delegar tarefas, fazer o code review, tomar decisões finais, aprimorar o fluxo/processo e gerir o grupo de forma estratégica extraindo o maximo de cada um. |  Entender todos os processos e regras de negócio, ter amplo conhecimento das stacks do projeto. | Saber gerir grupo, otima comunicação com suporte/implantação/devs.

---

## 4. Tarefa 3: Matriz de responsabilidades

> Substituam “Papel 1”, “Papel 2”, “Papel 3” e “Papel 4” pelos papéis definidos pela equipe. Acrescentem ou removam colunas conforme necessário.

Utilizem:

- **R:** responsável por executar a atividade;
- **A:** aprovador ou responsável final;
- **C:** consultado antes da execução ou decisão;
- **I:** informado sobre o resultado.

| Atividade de qualidade | DevOps | QA | Desenvolvedor | Responsável pelo produto |
|---|:---:|:---:|:---:|:---:|
| Definir critérios de aceitação | - | R | - | C, A 
| Revisar requisitos | - | R | - | A 
| Implementar a funcionalidade | - | - | R | A
| Revisar o código | A | - | R | - 
| Criar testes unitários | A | - | R | -
| Planejar e executar testes do sistema | R | R | - | -
| Registrar e acompanhar defeitos | - | R | - | I
| Priorizar a correção dos defeitos | - | R | I | C
| Aprovar a disponibilização da versão | R | - | - | I



### 4.1 Lacuna ou conflito encontrado

**Lacuna ou conflito:**  
```
resposta: “Planejar e executar testes do sistema”, poderia ser algo tanto do QA quanto do DevOps
```

**Consequência:**  
```
resposta: retrabalho desnecessário, falta de organização.
```

### 4.2 Práticas de QA recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Abordagem Three Amigos | requisitos incompletos, casos de teste desalinhados com a regra de negócio e cenários de testes criados tardiamente. | QA, Dev e Analista de Negócios. 
| Shift-Left Testing | Detecção tardia de falhas de arquitetura/integração, acúmulo de testes na fase final da sprint e execuções de testes de sistema com atrasos. | QA, Dev, DevOps



---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
gemini

**Como foi utilizada:**
Usando para entender quais praticas de QA podem ser adotadas

**Como as respostas foram verificadas:**
de forma manual, cada resposta da IA foi analisada e ajustada para fazer sentido ao contexo do trabalho.

