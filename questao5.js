/*
Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
*/

let string = "Oi, eu sou o Rodrigo";

function inverter(){
    let invertido = "";
    for(let i = string.length - 1; i >= 0; i--){
        invertido += string[i];
    }
    console.log(invertido);
}

inverter(string);