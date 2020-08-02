<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
  $_State = $_POST['Authentication'];
  if ($_State == "SignUp")
  { 
    //echo $_State;   
    echo shell_exec("python FR.py '$_State' ");
  }
  elseif ($_State == "SignIn") 
  {
    //echo $_State;   
    echo shell_exec("python FR.py '$_State' ");
  }
?>
</body>
</html>
