<?php
// Assuming your Microsoft SQL Server database credentials
$serverName = "SMEDINA-DELL"; // or IP address
$connectionOptions = array(
    "Database" => "master",
    "TrustServerCertificate" => true // You might need this if using SSL
);

// Establishes the connection using Windows Authentication
$conn = sqlsrv_connect($serverName, $connectionOptions);

if ($conn === false) {
    die(print_r(sqlsrv_errors(), true));
}

// Prepare SQL statement to insert data into the database
$sql = "INSERT INTO Contacts (firstName, lastName, phoneNumber) VALUES (?, ?, ?)";

// Prepare the statement
$stmt = sqlsrv_prepare($conn, $sql, array(&$firstName, &$lastName, &$phoneNumber));

// Set parameters
$firstName = $_POST["firstName"];
$lastName = $_POST["lastName"];
$phoneNumber = $_POST["phoneNumber"];

// Execute the statement
if (sqlsrv_execute($stmt)) {
    echo "New record created successfully";
} else {
    echo "Error: " . print_r(sqlsrv_errors(), true);
}

// Free the statement and close the connection
sqlsrv_free_stmt($stmt);
sqlsrv_close($conn);
?>
