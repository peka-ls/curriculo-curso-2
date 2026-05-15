CREATE TABLE usuario (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

/*adiciona nova coluna na tabela usuario*/
ALTER TABLE usuario ADD salario INT;

INSERT INTO usuario (nome, cpf, email, senha) VALUES 
('Enzo', '123.123.123-12', 'enzo@gmail.com', '123'),
('Admin', '111.111.111-11', 'admin@gmail.com', '111'); 

--atualiza o salario do usuario com id 1 para 3000
UPDATE usuario SET salario = 3000 WHERE id = 1; 

--busca somente o desejado pelo programador
SELECT * FROM usuario WHERE salario > 2000;