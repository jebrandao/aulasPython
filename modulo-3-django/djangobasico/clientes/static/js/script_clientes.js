// Aula 29 – JavaScript em arquivo estático.
// Em vez de onclick="teste();" no HTML, o evento é ligado aqui (JS separado do HTML).
function teste() {
    alert("Beleza! Você clicou.");
}

document.addEventListener("DOMContentLoaded", () => {
    const botao = document.getElementById("botao-teste");
    if (botao) {
        botao.addEventListener("click", teste);
    }
});
