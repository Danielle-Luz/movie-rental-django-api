<h1 align="center">Movie Rental Django API</h1>

<p align="center">
    <img alt="Badge indicando que o projeto foi criado em abril de 2023" src="https://img.shields.io/badge/Data%20de%20cria%C3%A7%C3%A3o-Abril%2F2023-blue">
    <img alt="Badge indicando que o status do projeto é 'concluído'" src="https://img.shields.io/badge/Status-Concluído-yellow">
</p>

## Índice

• <a href="#descricao">Descrição</a>
<br>
• <a href="#tecnologias">Tecnologias</a>
<br>
• <a href="#funcionalidades">Funcionalidades</a>
<br>
• <a href="#endpoints">Rotas do serviço</a>
<br>
• <a href="#Desenvolvedora">Desenvolvedora</a>
<br>
<p align="center">
</p>


<h2 id="descricao">Descrição</h2>
API feita com Django, capaz de gerenciar usuários, filmes e compras, incluindo serialização de dados, autenticação e permissões de rotas para diferentes tipos de usuário.

<h2 id="tecnologias">Tecnologias</h2>

- Python
- Django
- PostgreSQL

<h2 id="funcionalidades">Funcionalidades</h2>

- Usuário customizado com base no AbstractUser;
- Validação de dados customizada com serializers;
- Proteção de rotas via autenticação JWT e permissão customizada do Django Rest Framework;
- Tabela pivô customizada;
- Paginação com APIView;

<h2 id="endpoints">Rotas do serviço</h2>

### Users
| Método   | Rota             | Permissão      | Responsabilidade |
| -------- | -------------------- | --------------------- | -------- |
| POST     | /api/users/            | Livre para acesso        | Criar um novo usuário |
| GET    | api/users/<int:user_id>/   | Somente autenticado                             | Mostrar os dados de um usuário com o ID indicado |
| PATCH  | api/users/<int:user_id>/   | Somente autenticado e dono da conta ou admin     |  Atualizar os dados do usuário com o ID indicado |


### Movies
| Método | Rota                      | Permissão           | Responsabilidade |
| ------ | ------------------------- | ------------------- | ---------------- |
| GET    | api/movies/               | Livre para acesso   | Listar todos os filmes |
| POST   | api/movies/               | Somente employee    | Cadastrar um novo filme |
| GET    | api/movies/<int:movie_id>/| Livre para acesso   | Mostrar o filme com o ID indicado |
| DELETE | api/movies/<int:movie_id>/| Somente employee    | Excluir o filme com o ID indicado |

### Orders
| Método | Rota                      | Permissão           | Responsabilidade |
| ------ | ------------------------- | ------------------- | ---------------- |
| POST   | api/movies/<int:movie_id>/orders/  | Somente autenticado  | Criar um novo pedido |

<h2 id="Desenvolvedora">Desenvolvedora</h2>

<p align="center">
  <a href="https://github.com/Danielle-Luz">
    <img width="120px" src="https://avatars.githubusercontent.com/u/99164019?v=4" alt="foto de uma mulher parda com o cabelo castanho, sorrindo levemente na frente de um fundo verde com bits">
  </a>
</p>

<p align="center">
Danielle da Luz Nascimento
</p>

<p align="center">
<a href="https://www.linkedin.com/in/danielle-da-luz-nascimento/">@Linkedin</a>
</p>
