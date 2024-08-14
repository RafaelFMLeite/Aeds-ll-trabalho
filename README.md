# Sistema de Gerenciamento de Eventos

## Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação para o gerenciamento de eventos, facilitando a criação e organização de eventos, incluindo a administração de convidados, comidas e bebidas. O objetivo é fornecer uma ferramenta eficiente para gerenciar todos os aspectos de um evento, desde a criação até a organização dos participantes e dos itens a serem servidos.

## Objetivo

O principal objetivo da aplicação é facilitar o gerenciamento de eventos, abrangendo a criação e administração dos eventos e suas respectivas entidades, como convidados, comidas e bebidas. A aplicação permite realizar operações de ordenação e busca para facilitar o acesso às informações e garantir uma gestão eficiente dos eventos.

## Entidades Envolvidas

1. **Usuário**:
   - Representa os responsáveis pela criação e gerenciamento dos eventos.
   - Cada usuário possui um identificador único e um nome.

2. **Evento**:
   - Representa os eventos que serão organizados.
   - Cada evento é associado a um usuário organizador e possui um nome único.

3. **Convidado**:
   - Representa as pessoas que serão convidadas para os eventos.
   - Cada convidado possui um identificador único e um nome.

4. **Comida**:
   - Representa os itens alimentares que serão servidos nos eventos.
   - Cada comida possui um identificador único e um nome.

5. **Bebida**:
   - Representa as bebidas que serão servidas nos eventos.
   - Cada bebida possui um identificador único e um nome.

## Operações Implementadas

1. **Geração de IDs**:
   - Cada entidade recebe um identificador único gerado automaticamente, garantindo a singularidade de cada registro.

2. **Persistência de Dados**:
   - As informações das entidades (usuários, eventos, convidados, comidas e bebidas) são salvas em arquivos locais, permitindo que sejam carregadas e manipuladas em futuras execuções do sistema.

3. **Ordenação e Busca**:
   - Implementação de algoritmos de ordenação em disco (como Merge Sort) para organizar as bases de dados.
   - Algoritmos de busca sequencial e binária são usados para localizar entidades específicas com base em critérios como nome.

4. **Interações com Eventos**:
   - A aplicação permite adicionar convidados a eventos, bem como listar os convidados de um evento específico.
   - Também é possível adicionar comidas e bebidas aos eventos, garantindo uma gestão completa dos itens a serem servidos.

## Estruturas de Dados e Algoritmos

- **Estruturas de Dados**:
  - Estruturas simples foram utilizadas para representar as entidades do sistema, incluindo listas para armazenar os registros.

- **Algoritmos de Busca**:
  - Implementação de busca sequencial para iterar pelas bases de dados de forma desordenada.
  - Implementação de busca binária para iterar pelas bases de dados após a ordenação.

- **Algoritmos de Ordenação**:
  - Foi implementado o algoritmo de ordenação Merge Sort para organizar as bases de dados, garantindo que as buscas binárias possam ser realizadas de forma eficiente.

## Interações Entre Entidades

- **Adição de Convidados**:
  - Permite associar convidados a eventos específicos, mantendo um registro dos participantes.

- **Adição de Comidas e Bebidas**:
  - Permite adicionar itens alimentares e bebidas aos eventos, facilitando a organização dos recursos a serem servidos.

## Conclusão

Esta aplicação foi projetada para simular um sistema básico de gestão de eventos, com foco na eficiência da criação, organização e busca de informações relevantes para o gerenciamento de eventos. Com o uso de técnicas de algoritmos de ordenação e busca, o sistema é capaz de garantir uma experiência organizada e eficaz para o usuário final.
