# Atividade 3: Estratégia e Projeto de Testes do LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** [preencher]  
**Equipe:** [preencher, se aplicável]  
**Data:** [dd/mm/aaaa]

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| [nome] | [@usuario] |
| [nome] | [@usuario] |
| [nome] | [@usuario] |
| [nome] | [@usuario] |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

```
resposta: verificar a busca do restaurante por informações gerais como nome e descrição e o popup de pratos selecionados e se há persistência do pedido atual.
```

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Rene | Pesquisa de restaurantes | se a busca é efetiva e encontra os restaurantes certos por localidade ou culinária.
| Felipe | Popup de pedidos | Se o pedido atual do cliente fica salvo em cache. E ver se não vai sumir caso ele mude de página.


> Acrescentem ou removam linhas conforme o número de integrantes.

#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| Pesquisa por todos os pratos de todos os restaurantes ao mesmo tempo | Por enquanto não vai ser um requisito do sistema, outros testes tem prioridade.
| inclusão de cupom/desconto no pedido | Projeto não tem como foco o uso de cupons nos pedidos no momento



### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Sistema | Interações do cliente com o programa, de seu input até uma busca otimizada no banco de dados.
| Tipos de teste | Funcional | O objetivo é ver se a busca básica de restaurantes funciona
| Perspectiva caixa-preta ou caixa-branca | Caixa preta | O fluxo vai ser desde o input do usuário a resposta
| Técnicas de teste | Equivalência | Ou o texto de pesquisa encontra um restaurante ou não


| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | Integrção | É necessário validar a comunicação entre o estado global da aplicação (ou armazenamento local/sessão) e o roteamento da interface para garantir que o estado do popup se mantenha ao mudar de página. 
| Tipos de teste | Funcional | Valida se a regra de negócio (preservar dados e estado do popup) continua a funcionar corretamente após ações de navegação do utilizador sem perda de informação. garantir que atualizações no sistema não quebrem a recepção de novos pedidos. 
| Perspectiva caixa-preta ou caixa-branca | Caixa preta | O objetivo é validar o comportamento do sistema do ponto de vista do usuário final.
| Técnicas de teste | Transicao de Estados | A funcionalidade altera seu estado com base nas ações de navegação do usuário. Essa técnica garante a cobertura de todas as trocas de rotas e retenção de estado. 



### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | navegador, conexão, restaurantes cadastrados, 
| Responsáveis pelo planejamento | QA
| Responsáveis pela especificação dos casos | QA
| Responsáveis pela futura execução | QA



### 2.5 Critérios

Rene
| Critério | Definição da equipe |
|---|---|
| Entrada | Restaurantes cadastrados
| Saída | Filtro correto da pesquisa
| Suspensão | queda de conexão, poucos restaurantes.

Felipe
| Critério | Definição da equipe |
|---|---|
| Entrada | Pratos cadastrados
| Saída | Manter o mesmo pedido apos trocar de pagina
| Suspensão | queda de conexão, poucos pratos.


---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

> Cada integrante deve analisar pelo menos um risco relacionado à funcionalidade escolhida. No trabalho individual, devem ser analisados dois riscos.

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | Rene | Pesquisa de restaurantes | Não conseguir filtrar, ou filtrar mal | Não conseguir achar o restaurante rapidamente | Médio | Médio | Médio | Poderia enganar o cliente de que não existe restaurante em tal localidade ou com tal culinária
| R02 | Felipe | Manter os dados do popup de pedido em cache | Perda de dados do pedido ao mudar de página | O operador do delivery perde a visibilidade do pedido que acabou de chegar e deixa de o atender. | Média | Alto | Alta | Trata-se da falha central da funcionalidade. A perda de informação afeta diretamente o tempo de resposta e a operação do restaurante, podendo levar ao cancelamento de pedidos por atraso. 


> Acrescentem as linhas necessárias e mantenham identificadores únicos: R01, R02, R03 etc.

### 3.2 Aplicação das técnicas

> Cada integrante deve aplicar pelo menos uma técnica adequada à funcionalidade e ao risco analisado. A equipe deve utilizar, no conjunto da atividade, pelo menos duas técnicas diferentes.

#### Análise do integrante 1

**Integrante:** Rene 
**Funcionalidade:** Pesquisa de restaurantes
**Risco relacionado:** R01  
**Técnica escolhida:** Equivalência 

**Por que a técnica foi escolhida:**  

```
Rene: Foi escolhida a equivalência pois é preciso montar uma pesquisa com palavras chaves, e verificar a compatibilidade da pesquisa com os restaurantes filtrados, tipo pesquisar por um nome que tem no meio de um restaurante, ou por algo que só tem nas descrições dos restaurantes.
```


**Aplicação da técnica:**  
| Classe | Situação | Valor representativo
| Inválida | Pesquisa local não existe | Bahia
| Válida | Pesquisa local existe | Sul
| Válida | Pesquisa culinária existe | Brasileira


**Casos derivados:** 

- CT01: Pesquisar restaurantes pelo local “Bahia”;
- CT02: Pesquisar restaurantes pelo local “Sul”;
- CT03: Pesquisar restaurantes pela culinária “Brasileira”.

#### Análise do integrante 2

**Integrante:** Felipe
**Funcionalidade:** Manter os dados do popup de pedido em cache
**Risco relacionado:** R02  
**Técnica escolhida:** Transição de estados 


**Por que a técnica foi escolhida:**  

```
Felipe: A funcionalidade de persistência depende diretamente das ações sequenciais de navegação do usuário e de como o estado do popup (Visível, Oculto, Aceito) responde a essas trocas de rotas. A técnica permite mapear cada estado do popup antes e depois do evento de mudança de página. 
```

**Aplicação da técnica:**  

1) Sair da tela sem perder o que digitou.

Visível (com dados) -> Troca de rota -> Oculto (dados guardados)

2) Reabrir o popup e checar se o cache recuperou as informações.

Oculto (em outra rota) -> Voltar à rota anterior -> Visível (dados restaurados)

3) Garantir que o cancelamento voluntário apague o cache para não resgatar Lixo.

Visível -> Clicar em Cancelar -> Oculto (cache limpo)


**Casos derivados:** 
- CT04: Trocar de página após o tempo de 61 segundos
- CT05: Trocar de página aos exatos 30 seg
- CT06: Trocar de página aos exatos 59 seg

> Repitam ou removam a seção de análise conforme o número de integrantes.

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste

> No trabalho individual, elabore três casos. No trabalho em equipe, cada integrante deve elaborar pelo menos dois casos relacionados à própria funcionalidade.

### CT01: Pesquisar restaurantes pelo local “Bahia”

**Integrante responsável:** Rene
**Funcionalidade:** Pesquisa de restaurantes
**Risco ou requisito relacionado:** R01 
**Técnica utilizada:** Equivalência

**Pré-condição:**  
Restaurantes cadastrados


**Dados de entrada:**  
Apenas o input de pesquisa com “Bahia”


**Passos:**

1. Entrar no local eats na página principal
2. Escrever “Bahia” no input de pesquisa.


**Resultado esperado:**  
Nenhum restaurante deve aparecer, pois não existe restaurante com localidade Bahia

---

### CT02: Pesquisar restaurantes pelo local “Bahia”

**Integrante responsável:** Rene
**Funcionalidade:** Pesquisa de restaurantes
**Risco ou requisito relacionado:** R01 
**Técnica utilizada:** Equivalência

**Pré-condição:**  
Restaurantes cadastrados


**Dados de entrada:**  
Apenas o input de pesquisa com “Sul”


**Passos:**

1. Entrar no local eats na página principal
2. Escrever Sul no input de pesquisa.


**Resultado esperado:**  
Alguns restaurantes devem aparecer, pois esse input é uma localidade válida.


---

### CT03: Pesquisar restaurantes pela culinária “Brasileira”.


**Integrante responsável:** Rene
**Funcionalidade:** Pesquisa de restaurantes
**Risco ou requisito relacionado:** R01 
**Técnica utilizada:** Equivalência

**Pré-condição:**  
Restaurantes cadastrados


**Dados de entrada:**  
Apenas o input de pesquisa com “Brasileira”


**Passos:**

1. Entrar no local eats na página principal
2. Escrever “Brasileira” no input de pesquisa.


**Resultado esperado:**  
Alguns restaurantes devem aparecer, pois esse input é uma culinária válida.

---

## CT04: Trocar de página após o tempo de 61 segundos.


**Integrante responsável:** Felipe
**Funcionalidade:** Manter os dados do popup de pedido em cache
**Risco ou requisito relacionado:** R02 
**Técnica utilizada:** Transição de Estados

**Pré-condição:**  
Pratos cadastrados


**Dados de entrada:**  
Adicionar prato ao pedido e mudar de pagina aos 61 segundos após a adição


**Passos:**

1. Entrar no local eats na pagina do restaurante x
2. clicar em adicionar em qualquer prato
3. mudar de pagina apos esperar 61 segundos 


**Resultado esperado:**  
Os dados devem ser mantidos no popup de pedido

---

## CT05: Trocar de página aos exatos 30 seg.


**Integrante responsável:** Felipe
**Funcionalidade:** Manter os dados do popup de pedido em cache
**Risco ou requisito relacionado:** R02 
**Técnica utilizada:** Transição de Estados

**Pré-condição:**  
Pratos cadastrados


**Dados de entrada:**  
Adicionar prato ao pedido e mudar de página aos exatos 30 seg após a adição


**Passos:**

1. Entrar no local eats na pagina do restaurante x
2. clicar em adicionar em qualquer prato
3. mudar de pagina depois de 30seg
 

**Resultado esperado:**  
Os dados devem ser mantidos no popup de pedido.

---

## CT06: Trocar de página aos exatos 59 seg.


**Integrante responsável:** Felipe
**Funcionalidade:** Manter os dados do popup de pedido em cache
**Risco ou requisito relacionado:** R02 
**Técnica utilizada:** Transição de Estados

**Pré-condição:**  
1. Usuário autenticado/navegando no sistema. 
2. Pratos cadastrados e disponíveis no cardápio. 


**Dados de entrada:**  
Adicionar prato ao pedido e mudar de pagina aos exatos 59 seg apos a adição


**Passos:**

1. Entrar no local eats na pagina do restaurante x
2. Clicar em adicionar em qualquer prato
3. Mudar de pagina depois de 59seg


**Resultado esperado:**  
Os dados devem ser mantidos no popup de pedido

---

### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Rene | Pesquisa de restaurantes | R01 | Equivalência | CT01, CT02 e CT03
| Felipe | Manter os dados do popup de pedido em cache | R02 | Transferência de Estados | CT04, CT05 e CT06


> Acrescentem as linhas necessárias. Verifiquem se todos os riscos selecionados possuem casos de teste relacionados.

---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**
Gemini

**Como foi utilizada:**
Gerado promps para entender melhor qual tecnica usar para a funcionalidade R02

**Uma sugestão que precisou ser alterada ou rejeitada:**
A ia sugeriu a mesma tecnica que ja tinha sido usada pelo colega, tive que mudar o promp para dizer que nao podia ser a mesma tecnica usada antes.

**Como as respostas foram verificadas:**
Foi analisado a resposta e filtrado somente as informações úteis para responder e preencher as tabelas. e validado se a tecnica fazia sentido ou nao para a minha funcionalidade.
