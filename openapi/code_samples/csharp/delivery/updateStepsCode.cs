var client = new RestClient("https://staging-api.tizo.co/api/v1/delivery/update-steps/?codeDelivery=93EFFF0F-0FB6-4FC9-858B-9C63C522A818");
client.Timeout = -1;
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "eyJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoibWFuYWdlciIsInR5cGUiOiJhY2Nlc3MiLCJ1c2VybmFtZSI6Im1fcGVyZXppdG8yIiwiaWF0IjoxNjk1ODMzMDQ2LCJleHAiOjE2OTU4MzY2NDZ9.Lt7n5GDh6gb7Usg9Ek8BNnQnYLzX5FtPinmMMUUup53NUkluUCpqjTdcZpRFmDfzU56aeDidSdN4WsKYaVVqDg");
request.AddHeader("Content-Type", "application/json");
var body = @"{
" + "\n" +
@"    ""stepsCode"": ""ANNULLED"",
" + "\n" +
@"    ""name"": ""Orden anulada"",
" + "\n" +
@"    ""description"": ""Envio de ejemplo, anular""
" + "\n" +
@"}";
request.AddParameter("application/json", body,  ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);