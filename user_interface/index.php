<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="style/css/bootstrap.css">
        <link rel="stylesheet" type="text/css" href="style/style.css">
        <link href="style/css/bootstrap.min.css" rel="stylesheet">
        <link rel="shortcut icon" href='./img/logo.ico' />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title></title>
    </head>
    <body>
        <img src='./img/logo.png' weight='200' height='200'/>
        <div class="page-header">
            <h1>DATA EVAL</h1>
        </div>
        <?php
        include './classes/Form_Manager.php';
        include './classes/Data_Validation.php';
        require './classes/userValidation.php';
        ?>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="style/js/bootstrap.min.js"></script>
    </body>
</html>
