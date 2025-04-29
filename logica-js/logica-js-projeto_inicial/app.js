alert('Boas vindas ao jogo do número secreto');
let chute = prompt('Escolha a um número entre 1 e 10: ');
console.log("Verificando o chute: " + chute)

let numeroSecreto = 4;
console.log("Comparando o chute com o número secreto: " + chute == numeroSecreto)

// se o chute foi igual ao número secreto
if (chute == numeroSecreto){
    console.log("Você acertou! O número secreto é: " + numeroSecreto)
    alert(`Isso aí! Você acertou o número secreto ${numeroSecreto}`)
} 
// se o chute foi diferente do número secreto
else {
    console.log("O número secreto é: " + numeroSecreto)
    alert('Você errou... Tente novamente!')
}
