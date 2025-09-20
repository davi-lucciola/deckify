# undefined

Esse projeto é uma plataforma de estudos através de FlashCards, onde as coleções de Flash Cards podem ser geradas utilizando AI e também compartilhadas com a comunidade

## Requisitos 

### Gerenciamento de Coleção de Flash Cards

- O usuário poderá listar todas as suas coleções de flash cards.
- Todo usuário poderá criar coleções de flash cards.
- A coleção de flash cards poderá ter tags associadas identificar o(s) assunto(s) relacionado(s).
- A coleção de flash cards pode ser publica ou privada.
- O usuário pode copiar coleções de flash cards
- O usuário poderá editar ou excluir suas próprias coleções de flash cards
- O usuário poderá detalhar as coleções para ver os flashes cards pertencentes a uma coleção.
- O usuário pode criar coleções gerando flash cards automaticamente dado o seu objetivo, mediante ao preenchimento de alguma(s) informações.

### Gerenciamento de Flash Cards

- Cada flash card terá uma pergunta e uma resposta
- O usuário poderá gerenciar os flash cards dentro do detalhamento da coleção
- O usuário pode adicionar flash cards a suas coleções
- O usuário pode editar os flash cards das suas coleções 
- O usuário pode excluir os flash cards das suas coleções
- O usuário pode regerar flash cards escolhendo aqueles que ele quer manter e os que ele quer excluir

### Marketplace de Flash Cards

- Todo usuário poderá ver as coleções de flash cards publicos em uma página de "Marketplace"
- Na página de marketplace, o usuário poderá pesquisar coleções de flash cards
- Na página de marketplace, as coleções de flash cards devem ser carregadas parcialmente de alguma forma (paginação ou infinity scrolling)
- O usuário poderá adicionar flash cards publicos a sua própria coleção (curtida e/ou favorito)
- As coleções de flash card recomendadas na consulta inicial devem considerar as preferencias do usuário e as mais adicionadas pela comunidade (curtidas e/ou favoritadas)

### Usuários e Autenticação

- Qualquer pessoa pode cadastrar seu proprio usuário na plataforma (Com email e senha, ou com o google).
- A identificação de cada usuário deve ser realizada através do email (ele será unico).
- Todo usuário poderá autenticar na plataforma utilizando email e senha.
- O usuário deverá confirmar o seu email ao criar sua conta (exceto se ele criar a conta pelo google).
- Todo usuário poderá recuperar sua senha, mediante confirmação do email cadastrado e via link de recuperação de senha (com tempo de expiração).
