<?php 
    include '../conexao.php';

    //receber os dados dos names do front end
    $nome = $_REQUEST['nome'];
    $email = $_REQUEST['email'];
    $cpf = $_REQUEST['cpf'];
    $senha = $_REQUEST['senha'];

    //inserção em sql

    $sql = "INSERT INTO usuario( nome, cpf, email, senha) VALUES ('$nome', '$cpf', '$email', '$senha')";
    $resultado = mysqli_query($conexao, $sql);
    header('location:../../ecolote.php');

?>
