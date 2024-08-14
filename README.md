Trabalho de algoritmo e estrutura de dados 2

A ideia do trabalho consiste em:

Descrever, de forma suscinta, a aplicação que será desenvolvida na disciplina. Atentar para a
descrição do objetivo da aplicação, das entidades envolvidas e das operações a serem executadas.
Considerando a aplicação escolhida para ser implementada, pede-se:

1.  Implemente estruturas para representar as entidades que fazem parte da aplicação
e crie bases de dados para estas entidades. As bases de dados devem ser criadas 
desordenadas, de acordo com algum critério definido para identificar de forma única cada 
entidade.
2.  Implemente estratégias de buscas sequenciais e binárias para as iterar nas bases 
definidas.
3.  Implemente algum método de ordenação em disco (EXCETO o Insertion Sort) 
para ordenar as bases de dados, caso necessário.
4.  Implemente operações que exemplique as interações entre as entidades da 
aplicação

A aplicação a ser desenvolvida é um sistema de gerenciamento de eventos que permite a
criação e administração de eventos, convidados, comidas e bebidas.
Objetivo: Facilitar o gerenciamento de eventos, desde a criação até a organização dos
participantes e dos itens a serem servidos.
Entidades Envolvidas:
1. Usuário: Representa os responsáveis pela criação e gerenciamento dos eventos.
2. Evento: Representa os eventos que serão organizados.
3. Convidado: Representa as pessoas que serão convidadas para os eventos.
4. Comida: Representa os itens alimentares que serão servidos nos eventos.
5. Bebida: Representa as bebidas que serão servidas nos eventos.
Operações Executadas:
1. Geração de IDs: Cada entidade recebe um identificador único gerado
automaticamente.
2. Persistência de Dados: As informações de usuários, eventos, convidados, comidas
e bebidas são salvas em arquivos para que possam ser carregadas em futuras
execuções.
3. Ordenação e Busca: Utiliza-se algoritmos de ordenação (merge sort) para ordenar
os dados e algoritmos de busca (sequencial e binária) para encontrar entidades
específicas com base em critérios como nome.
4. Interações com Eventos: Permite adicionar convidados a eventos e listar os
convidados de um evento específico.
A aplicação é projetada para simular um sistema básico de gestão de eventos, abrangendo
a criação, organização e busca de informações relevantes para o gerenciamento eficiente
