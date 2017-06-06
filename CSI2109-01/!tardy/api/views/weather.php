<html>
  <body>

  <?php
  header('Content-Type: text/plain; charset=utf-8;');
  $file = file_get_contents("https://weathers.co/api.php?city=New+York");
  print_r(json_decode($file));
  ?>
  
  </body>
</html>
