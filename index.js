
function laCajaDePandora(numero){

    let resultado;

    // Verificar si el número es par o impar
    if (n % 2 === 0) {
        // Si es par, convertir a binario
        resultado = "";
        let numero = n;

        // Convertir a binario manualmente
        if (numero === 0) return "0"; // Manejar el caso de 0
        while (numero > 0) {
            resultado = (numero % 2) + resultado; // Agregar el bit más significativo
            numero = Math.floor(numero / 2); // Dividir por 2
        }
    } else {
        // Si es impar, convertir a hexadecimal
        resultado = "";
        let numero = n;

        // Convertir a hexadecimal manualmente
        const hexChars = "0123456789abcdef"; // Caracteres hexadecimales
        if (numero === 0) return "0"; // Manejar el caso de 0
        while (numero > 0) {
            resultado = hexChars[numero % 16] + resultado; // Agregar el carácter hexadecimal
            numero = Math.floor(numero / 16); // Dividir por 16
        }
    }

    return resultado; // Retornar el resultado final
}
function obtenerInformacion() {
    return {
        nombre: "Maximiliano",
        edad: 19,
        nacionalidad: "Argentino"
    };
