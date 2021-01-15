var submeter = document.querySelector(".submeter");
var saudeform = document.querySelector("#saude");
let pacientes = document.querySelectorAll('#pacientes');

submeter.addEventListener("click",function(){
    event.preventDefault();
    let paciente = {
        'nome':pacientes[0][0].value,
        'data_nascimento':pacientes[0][1].value,
        'telefone':pacientes[0][3].value,
        'email':pacientes[0][4].value,
        'endereco':pacientes[0][5].value,
        'bairro':pacientes[0][6].value
    };
    console.log(paciente);
    fetch("/cadastrar/paciente",{
        method:'POST',
        body: JSON.stringify({
            'nome':paciente.nome,
            'nascimento':paciente.data_nascimento,
            'telefone':paciente.telefone,
            'email':paciente.email,
            'endereco':paciente.endereco,
            'bairro':paciente.bairro,
        }),
        headers:{
            'Content-type':'application/json'
        }
    })
    .then(()=>{
        alert("Cliente Cadastrados");
        zerarform();
    });
});


function zerarform(){
    pacientes[0][0].value="";
    pacientes[0][1].value="";
    pacientes[0][2].value="";
    pacientes[0][3].value="";
    pacientes[0][4].value="";
    pacientes[0][5].value="";
    pacientes[0][6].value="";
}

