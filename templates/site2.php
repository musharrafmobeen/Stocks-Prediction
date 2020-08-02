<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<?php
  $_Open = $_GET['Open'];
  $_High = $_GET['High'];
  $_Low = $_GET['Low'];
  $_Close = $_GET['Close'];
  $_Volume = $_GET['Volume'];
  $imgUrl = "graph.jpg";
?>
<center>
<Table>
    <tr>
        <th>Open</th>
        <th>High</th>
        <th>Low</th>
        <th>Close</th>
        <th>Volume</th>
    </tr>
    <tr>
        <td><?= $_Open; ?></td>
        <td><?= $_High; ?></td>
        <td><?= $_Low; ?></td>
        <td><?= $_Close; ?></td>
        <td><?= $_Volume; ?></td>
    </tr>
</Table>
</center>
<center><img src="<?= $imgUrl; ?>"/></div></center>
</body>
</html>
