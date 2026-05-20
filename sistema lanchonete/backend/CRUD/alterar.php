<?php 
    include '../conexao.php';

    $id = $_REQUEST['id'];
    $nome = $_REQUEST['nome'];
    $cpf = $_REQUEST['cpf'];
    $email = $_REQUEST['email'];
    $senha = $_REQUEST['senha'];

    $sql = "UPDATE usuario SET nome='$nome', cpf='$cpf', email='$email', senha='$senha' WHERE id='$id'";

    mysqli_query($conexao, $sql);

    header('location:../../principal.php')
?>