# Introducción


Esta API contiene todas las funcionalidades de envíos que usted necesita para integrarla en su negocio, en caso de que usted no tenga un sistema existente, le recomendamos que use las apps pronto disponibles en Play Store, Apple Store o se contacte con nosotros y les proveeremos sus credenciales. Entre las principales funcionalidades se encuentran:

- Seguimiento en tiempo real, así como el historial de los envíos realizados.
- Cambiar los estados de los envios

Además, en el contexto de nuestro sistema, trabajamos con dos entornos distintos: desarrollo y producción. Estos entornos se utilizan para realizar pruebas y desplegar la aplicación final, respectivamente. Para acceder a la funcionalidad de la API en cada uno de estos entornos, es necesario utilizar los enlaces adecuados. 
 1. staging-api.tizo.co: Este enlace está configurado para apuntar al entorno de desarrollo de nuestra API. Cuando accedes a staging-api.tizo.co, estás interactuando con una versión de la API que se encuentra en desarrollo activo. Este entorno es utilizado principalmente por los desarrolladores y el equipo de pruebas para probar nuevas funcionalidades, realizar pruebas exhaustivas y detectar posibles errores o problemas antes de implementar los cambios en el entorno de producción. Es importante tener en cuenta que el entorno de desarrollo (staging-api.tizo.co) puede ser inestable en comparación con el entorno de producción, ya que se encuentra en constante desarrollo. Por lo tanto, si estás trabajando con staging-api.tizo.co, ten en cuenta que podrías encontrar errores o comportamientos no deseados que aún no han sido corregidos.

 2. api.tizo.co: Este enlace está configurado para apuntar al entorno de producción de nuestra API. Cuando accedes a api.tizo.com, estás interactuando con la versión estable y finalizada de nuestra API que se utiliza en producción. Este entorno se utiliza para brindar servicio a los usuarios finales y a las aplicaciones en producción que dependen de la API. En el entorno de producción (api.tizo.co), se espera que la API sea estable y libre de errores graves. Se realizan pruebas exhaustivas en el entorno de desarrollo antes de desplegar los cambios en producción, con el objetivo de garantizar la calidad y confiabilidad de la API en este entorno.

Es crucial tener en cuenta la diferencia entre estos dos enlaces y utilizar el enlace correcto según tus necesidades. Si estás desarrollando o realizando pruebas en tu aplicación, deberías utilizar staging-api.tizo.co para interactuar con la API en el entorno de desarrollo. Sin embargo, si estás utilizando tu aplicación en un entorno de producción, asegúrate de utilizar api.tizo.co para acceder a la API estable en producción y proporcionar un servicio confiable a tus usuarios finales.



# Comúniquese con nosotros

- Correos: Para contactarse con el equipo de tizo, escriba un correo a los siguientes e-mails rcastano@tizo.app  y a axel.garcia@tizo.app en caso de algún inconveniente con la API.
- Síguenos en las siguientes plataformas para estar al tanto de las últimas mejoras y novedades: [Facebook](https://www.facebook.com/profile.php?id=100086144095910), [Twitter](https://twitter.com/AppTizo), [Instagram](https://www.instagram.com/tizo.app/).


 [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/19319757-13ea3bc8-bfe2-4ffd-87ee-f2d3bb439c62?action=collection%2Ffork&collection-url=entityId%3D19319757-13ea3bc8-bfe2-4ffd-87ee-f2d3bb439c62%26entityType%3Dcollection%26workspaceId%3D957b370e-bb6a-4235-b1a9-43894e2c51eb#?env%5BTizo%20Vendors%5D=W3sia2V5IjoiYmFzZV91cmwiLCJ2YWx1ZSI6Imh0dHBzOi8vYXBpLnRpem8uY28iLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoiYXV0aF90b2tlbiIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6ImVudmlyb25tZW50IiwidmFsdWUiOiJkZXYiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoiZGVmYXVsdCJ9LHsia2V5IjoibGFuZ3VhZ2UiLCJ2YWx1ZSI6ImVzIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)