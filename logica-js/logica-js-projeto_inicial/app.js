alert('Boas vindas ao jogo do número secreto');
let numeroSecreto = 4;
let chute = prompt('Escolha a um número entre 1 e 30: ');

// se o chute foi igual ao número secreto
if (chute == numeroSecreto){
    alert('Você descobriu o número secreto!')
} 
// se o chute foi diferente do número secreto
else {
    alert('Você errou... Tente novamente!')
}
