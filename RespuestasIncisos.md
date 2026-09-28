## 1. Escriba un ejemplo de la respuesta JSON al consultar una tarea.
{
    id: 1,
    titulo: tarea1,
    curso: programacionWeb,
    fechaEntrega: 28/9/2026
    estado: completada
}

## 2. Indique el código HTTP que devolvería si la tarea solicitada no existe y escriba una respuesta de error adecuada.

Devuelve error 404 (No se encontró) y la respuesta de error es: "La tarea solicitada no existe (404)"

## 3. Indique un cambio posterior que podría romper este contrato (Breaking Change).
Por medio de un cambio en el nombre de los archivos, donde se cambie de "tarea" a "asignación" y la API espere "tarea".