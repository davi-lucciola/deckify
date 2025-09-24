# Deckify

Esse projeto é uma plataforma de estudos através de FlashCards, onde as coleções de Flash Cards podem ser geradas utilizando AI e também compartilhadas com a comunidade

## Requisitos 

### Gerenciamento de Decks

- O usuário poderá listar decks.
- Todo usuário poderá criar decks.
- O deck poderá ter tags associadas identificar o(s) assunto(s) relacionado(s).
- A deck pode ser publico ou privado (ele deve nascer privado sempre para ser publicado, ou ao ser criado o usuário escolherá?).
- O deck pode conter no máximo 60 flash cards.
- O usuário pode copiar decks publicos ou próprios.
- O usuário poderá editar ou excluir suas próprios decks.
- O usuário poderá detalhar os decks para ver os flashes cards pertencentes.
- O usuário pode criar decks gerando flash cards automaticamente dado o seu objetivo, mediante ao preenchimento de alguma(s) informações.

### Gerenciamento de Flash Cards

- Cada flash card terá uma pergunta, uma resposta e uma explicação (opcional).
- O flash card pode ter dicas que serão mostradas junto com a pergunta.
- A pergunta ou a resposta pode ter conteúdos de texto e imagem/gif.
- O usuário poderá gerenciar os flash cards dentro do detalhamento do deck.
- O usuário pode adicionar flash cards no deck.
- O usuário pode editar os flash cards dos seus decks. 
- O usuário pode excluir os flash cards dos seus decks.
- O usuário pode regerar flash cards escolhendo aqueles que ele quer manter e os que ele quer excluir.

### Estudo de Deck

- O usuário poderá clicar para estudar o deck.
- Ao usuário ver a resposta, ele informar o nivel de dificuldade para ele, baseado nesse resposta
a carta será mostrada com mais frequencia durante o estudo (ou mais rapidamente).

### Biblioteca de Decks

- Todo usuário poderá ver decks publicos em uma página de "Biblioteca".
- Na biblioteca, o usuário poderá pesquisar os decks por titulo/descrição ou por tag(s).
- Na biblioteca, os decks devem ser carregados parcialmente de alguma forma fornecendo uma continuidade para visualização (paginação ou infinity scrolling)
- O usuário poderá adicionar decks publicos ao favoritar um deck.
- O usuário poderá recomendar ou não recomendar um deck com uma comentário de avaliação.
- No detalhamento de um deck na biblioteca, será mostrado as avaliações da comunidade.
- O usuário poderá informar em cada avaliação se ela foi util ou não
- Os decks recomendados na consulta inicial devem considerar as preferencias do usuário, quantidade de favoritos e avaliações.

### Usuários e Autenticação

- Qualquer pessoa pode cadastrar seu proprio usuário na plataforma (Com email e senha, ou com o google).
- Ao realizar a primeira autenticação o usuário pode selecionar as tags de assuntos de sua preferencia.
- A identificação de cada usuário deve ser realizada através do email (ele será unico).
- Todo usuário poderá autenticar na plataforma utilizando email e senha.
- O usuário deverá confirmar o seu email ao criar sua conta (exceto se ele criar a conta pelo google).
- Todo usuário poderá recuperar sua senha, mediante confirmação do email cadastrado e via link de recuperação de senha (com tempo de expiração).

## Backlog

- Adicionar comentários para o deck ou flash card.
- Adicionar outros usuários como Editores do Deck (Ter Auditoria)
- Batalha de Decks
- Merge de Decks (ou Estudar com mais de um Deck)
- Limitar a Geração de Decks / Cards Baseado em um Plano de Uso
- Implementar uma forma de Ler o Card (em Audio).
- Implementar Tipos Diferentes de Flash Card (Multipla Escolha, Questões Abertas, Auto Complete e ETC)
