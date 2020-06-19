<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "covid";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
//if($link === false){
//    die("ERROR: Could not connect. " . mysqli_connect_error());
//}
$sql = "SELECT * FROM covid where lat != '' and lon != '';";
$result = $conn->query($sql);
$count = 0;
$count2 = 0;

echo "<input type = 'hidden' id = 'lat_1'></input><input type = 'hidden' id = 'lon_1'></input><input type = 'hidden' id = 'test_1'></input><br>";

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        $count++;
        echo "<input type = 'hidden' id = 'lat".$count."' value = ".$row["lat"] ."></input><input type = 'hidden' id = 'lon".$count."' value =" . $row["lon"]. "></input><input type = 'hidden' id = 'test".$count."' value = ".$row['test']."></input><br>";
        
    }
    echo "<input type = 'hidden' id = 'count' value = '".$count."'></input>";
} else {
    echo "0 results";
}


?>
<!DOCTYPE html>
<html>
<head>
  <title>COVID</title>

  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

  <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />

  <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>

  <style>
    body {
      padding: 0;
      margin: 0;
    }
    html, body, #map {
      height: 100%;
    }
  </style>
</head>
<body>
  <div id="map"></div>

  <script>
    var map = L.map('map');
var j = 1;
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(map);
      var xyz = 0;
      for(xyz = 0; xyz <= 0.001; xyz += 0.001) {
      var marker = L.marker([26.9112632 + xyz, 75.7324745]).addTo(map);
      }
    // placeholders for the L.marker and L.circle representing user's current position and accuracy    
    var current_position, current_accuracy;

    function onLocationFound(e) {
      // if position defined, then remove the existing position marker and accuracy circle from the map
      if (current_position) {
          map.removeLayer(current_position);
          map.removeLayer(current_accuracy);
      }

      var radius = e.accuracy / 2;
        
      current_position = L.marker(e.latlng).addTo(map)
        .bindPopup("You are within " + radius + " meters from this point").openPopup();

      current_accuracy = L.circle(e.latlng, radius).addTo(map);
        console.log(Object.values(e.latlng)[0]);
        console.log(Object.values(e.latlng)[1]);
        
        document.getElementById("lat_1").value = Object.values(e.latlng)[0];
        
    }

    function onLocationError(e) {
      alert(e.message);
    }

    map.on('locationfound', onLocationFound);
    map.on('locationerror', onLocationError);

    // wrap map.locate in a function    
    function locate() {
      map.locate({setView: true, maxZoom: 22});
        j++;
    }
    
    // call locate every 3 seconds... forever
    setInterval(locate, 3000);

  </script>
 <?php 
//$lat = mysqli_real_escape_string($link, $_REQUEST['lat_1']);
//$sql = "INSERT INTO covid (lat, lon, test) VALUES ('".$lat."', '11', 'neg')";

//if ($conn->query($sql) === TRUE) {
//  echo "New record created successfully";
//} else {
//  echo "Error: " . $sql . "<br>" . $conn->error;
//}
    
    ?>
</body>
</html>