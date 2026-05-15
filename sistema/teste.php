<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>teste</title>
</head>
<body>
    
    <h2> Trabalhando com PHP</h2>

    <?php 

    $nome = "Osnir";
    $operadora = "claro";

    if ($operadora == "claro") {
        echo "Não usar, operadora ruim";

    }
    else {
        echo "Vai na fé";
    }

    for ($contador = 0; $contador <10; $contador++) {
        echo "<p> Olá, $nome. O contador está em $contador </p>";
    }
    
    $numero = 0;

    while ($numero < 10) {
        echo "<br> O número é $numero </br>";
        echo "<hr>";
        $numero++;
    }


    ?>

</body>
</html>