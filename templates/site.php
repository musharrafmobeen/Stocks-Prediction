<?php
  $_name = $_POST['Company_Name'];
  $_date = $_POST['Date'];
  echo shell_exec("python StocksData.py '$_name' '$_date' ");
?>