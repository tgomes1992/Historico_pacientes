let nvisita = document.querySelector('.cadastrar-visitas');
let cadastrovisitas = document.querySelector("#cadastro-visitas");
let url = window.location.href
idClient = url.split("/")[4]
let dvisita = document.querySelector('#dataVisita');
let einicial = document.querySelector('#inicial');
let efinal = document.querySelector('#final');
let listaVisitas = document.querySelector('#lista_visitas');
let visitas = document.querySelectorAll(".data-visita");



 for(i=0;i<visitas.length;i++){
     console.log(visitas[i].innerText)
     visitas[i].innerText = formatardata(visitas[i].innerText)
 }

function cadastrar_visita(){
    dados_visita={
        'id' : idClient,
        'data' : dvisita.value,
        'inicial' : inicial.value,
        'final' : final.value,
    }
    let li = document.createElement("LI")
    li.textContent = dvisita.value
    listaVisitas.appendChild(li)
    console.log(dados_visita)
    cadastrovisitas.reset()
    $.post('/visita/paciente/'+idClient+'/registrar',dados_visita);
}


function formatardata(data){

    let ano = data.substring(0,4);
    let mes = data.substring(5,7);
    let dia = data.substring(8,10);
    master = dia + "/" + mes + "/" + ano
return master
}



nvisita.addEventListener('click',cadastrar_visita)

