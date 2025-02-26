import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
cursor.execute('INSERT INTO alunos(id, nome, idade,curso) VALUES (1, "Ananda", 28, "Arquitetura")')
cursor.execute('INSERT INTO alunos(id, nome, idade,curso) VALUES (2, "Mayla", 26, "Ciência da computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade,curso) VALUES (3, "Bárbara", 25, "Sistemas de Informação")')
cursor.execute('INSERT INTO alunos(id, nome, idade,curso) VALUES (4, "Gianne", 27, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade,curso) VALUES (5, "Verônica", 27, "Enfermagem")')
cursor.execute('INSERT INTO alunos(id, nome, idade,curso) VALUES (6, "Julia", 23, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade,curso) VALUES (7, "Caroline", 23, "Administração")')


# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
  print(aluno)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for aluno in dados:
  print(aluno)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
for aluno in dados:
  print(aluno)

# d) Contar o número total de alunos na tabela
qnt = cursor.execute('SELECT COUNT(*) FROM alunos')
for num in qnt:
  print(num)

# 4. Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 29 WHERE nome = "Ananda"')
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
  print(aluno)

# b) Remova um aluno pelo seu ID.
dados = cursor.execute('DELETE FROM alunos where id = 7')
for aluno in dados:
  print(aluno)


# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros declientes na tabela.

#cursor.execute('CREATE TABLE clientes(id PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Marcela", 35, 1100.20)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Joana", 20, 500.75)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Gabriela", 29, 5000)')



# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados_cliente = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
for cliente in dados_cliente:
  print(cliente)

# b) Calcule o saldo médio dos clientes.
saldo_medio = cursor.execute('SELECT AVG(saldo) FROM clientes')
for saldo in saldo_medio:
  print(saldo)

# c) Encontre o cliente com o saldo máximo.
cliente_max = cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
for cliente in cliente_max:
  print(cliente)

# d) Conte quantos clientes têm saldo acima de 1000.
acima_100 = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
for cliente in acima_100:
  print(cliente)


# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 1000 WHERE id =2')
dados_cliente = cursor.execute('SELECT * FROM clientes')
for cliente in dados_cliente:
  print(cliente)

# b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id = 3')
dados_cliente = cursor.execute('SELECT * FROM clientes')
for cliente in dados_cliente:
  print(cliente)



# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o idda tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

# cursor.execute('CREATE TABLE compras(id PRIMARY KEY, cliente_id INTEGER, produto VARCHAR(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 2, "Livro", 35.9)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 2, "Caderno", 20.90)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 1, "Caneta", 2.50)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 1, "Mochila", 120.00')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5, 2, "Estojo", 15.00)')

consulta = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')

for dado in consulta:
  print(dado)

conexao.commit()
conexao.close
