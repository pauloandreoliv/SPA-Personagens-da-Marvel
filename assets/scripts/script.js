window.onload = redirecionar();

function redirecionar(){
  var caminho = window.location.pathname;
  
  if (caminho == "/advance"){
    window.location.href = "/advance#1";
  }

  if (caminho == "/list_all"){
    window.location.href = "/list_all#1";
  }
  
  if (caminho == "/search_for"){
    window.location.href = "/search_for#2";
  }
}