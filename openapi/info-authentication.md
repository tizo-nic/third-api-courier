
## Headers

Para un mejor uso de nuestra API, debes de tomar en cuenta que cada request que se haga, se recibe los siguientes headers.

| Clave  | Valor |
|-------|-------|
| **Authorization** | Token | 
| **Content-Type** | application/json |
| **Accept-Language** | es, en |
| **User-Agent** | Navegador donde procede la solicitud |

## Autenticación.

Para obtener el valor del token necesitas realizar un POST request hacia https://staging-api.tizo.co/api/v1/auth/login con el siguiente body: <br>
{<br>
"username": "your_username",<br>
"password": "your_password",<br>
"typeUser": "logistics"<br>
}<br>