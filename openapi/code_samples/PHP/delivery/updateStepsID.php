<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('https://staging-api.tizo.co/api/v1/delivery/update-steps/?idDelivery=3884');
$request->setMethod(HTTP_Request2::METHOD_PUT);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Authorization' => 'eyJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoibWFuYWdlciIsInR5cGUiOiJhY2Nlc3MiLCJ1c2VybmFtZSI6Im1fcGVyZXppdG8yIiwiaWF0IjoxNjk1ODMzMDQ2LCJleHAiOjE2OTU4MzY2NDZ9.Lt7n5GDh6gb7Usg9Ek8BNnQnYLzX5FtPinmMMUUup53NUkluUCpqjTdcZpRFmDfzU56aeDidSdN4WsKYaVVqDg',
  'Content-Type' => 'application/json'
));
$request->setBody('{
\n    "stepsCode": "ANNULLED",
\n    "name": "Orden anulada",
\n    "description": "Envio de ejemplo, anular"
\n}');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}