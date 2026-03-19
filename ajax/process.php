<?php

echo 'processing....';

if(isset($_GET['name'])){
    echo 'GET : Your Name is '.$_GET['name'];
}


if(isset($_POST['name'])){
    echo 'POST : Your Name is '.$_POST['name'];
}