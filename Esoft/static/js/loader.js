var criaLoader;

function functionLoader() {
    criaLoader = setTimeout(showPage, 2500); // tempo de resposta para o loader
}

function showPage() {
   document.getElementById("loader").style.display = "none";
   document.getElementById("divprincipal").style.display = "block";
}