<?php 
    include './conexao.php';

    $id = $_REQUEST['id'];
    $nome = $_REQUEST['nome'];
    $cpf = $_REQUEST['cpf'];
    $email = $_REQUEST['email'];
    $senha = $REQUEST['senha'];

    $sql = "INSERT INTO usuario (nome, cpf, email, senha) VALUES ('$nome', '$cpf', '$email', '$senha')";

    $resultado = mysqli_query($conexao, $sql);
    header ('location:../../principal.php')
?>