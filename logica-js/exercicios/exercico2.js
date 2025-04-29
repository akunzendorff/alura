// Pergunte ao usuário qual é o dia da semana. Se a resposta for "Sábado" ou "Domingo", mostre "Bom fim de semana!". Caso contrário, mostre "Boa semana!".

dia_semana = prompt("Qual é o dia da semana?");
if (dia_semana == "Sábado") {
  alert("Bom final de semana!");
} else if (dia_semana == "Domingo") {
  alert("Bom final de semana!");
} else {
  alert("Boa semana!");
}

// Verifique se um número digitado pelo usuário é positivo ou negativo. Mostre um alerta informando.

numero = prompt("Digite um número: ");
if (numero > 0) {
  alert("O número digitado é positivo.");
} else {
  alert("O número digitado é negativo.");
}

// Crie um sistema de pontuação para um jogo. Se a pontuação for maior ou igual a 100, mostre "Parabéns, você venceu!". Caso contrário, mostre "Tente novamente para ganhar.".

pontuacao = 104;
if (pontuacao >= 100) {
  alert("Parabéns, você venceu!");
} else {
  alert("Tente novamente para ganhar.");
}

// Crie uma mensagem que informa o usuário sobre o saldo da conta, usando uma template string para incluir o valor do saldo.

saldo = 1000;
alert(`O saldo é R$${saldo}`);

// Peça ao usuário para inserir seu nome usando prompt. Em seguida, mostre um alerta de boas-vindas usando esse nome.

nome = prompt("Digite seu nome: ");
alert(`Boas vindas, ${nome}!`);
