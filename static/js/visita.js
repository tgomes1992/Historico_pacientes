let nvisita = document.querySelector('.cadastrar-visitas');
let cadastrovisitas = document.querySelector("#cadastro-visitas");
let url = window.location.href
idClient = url.split("/")[4]
let dvisita = document.querySelector('#dataVisita');
let einicial = document.querySelector('#inicial');
let efinal = document.querySelector('#final');
let listaVisitas = document.querySelector('#lista_visitas');
let visitas = document.querySelectorAll(".data-visita");


alert("oi");


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
    li.textContent = formatardata(dados_visita['data'])
    listaVisitas.appendChild(li)
    console.log(dados_visita)
    cadastrovisitas.reset()
    $.post('/visita/paciente/'+idClient+'/registrar',dados_visita);
}


function formatardata(data){
    var date = new Date(data);
    var dia  = date.getDate()+1;
    var mes = "0"+(date.getMonth()+1);
    if (mes>=10){
        var mes = date.getMonth()+1;
    }
    var ano = date.getFullYear();
    master = dia+"/"+mes+"/"+ano
return master
}



nvisita.addEventListener('click',cadastrar_visita)

