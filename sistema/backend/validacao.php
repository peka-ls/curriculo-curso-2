<?php 
//iniciar sessão
session_start();

#$aviso = ""

//se não houver variavel de sessão cpf e senha
if (!isset($_SESSION['email']) or !isset($_SESSION['senha'])) {
    //destruir sessão anterior
    session_destroy();

    //limpar variaveis da sessão
    unset($_SESSION['email']);
    unset($_SESSION['senha']);

    //manda login
    header('location:../sistema/login.php');

    $senhaIncorreta = true;
    exit;
}

#if ($senhaIncorreta == true) {
#    $aviso = "Email ou senha incorreto";
#}

?>