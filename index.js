
function laCajaDePandora(numero) {
    if (numero % 2 === 0) { // Verificar si el número es par
        return numero.toString(2); // Convertir a binario
    } else { // Si es impar
        return numero.toString(16); // Convertir a hexadecimal
    }
}

function obtenerInformacion() {
    return {
        nombre: "Sarita",
        edad: 25,
        nacionalidad: "Colombiana"
    };
}

