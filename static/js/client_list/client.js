let remover = document.querySelectorAll('.remover');
let modificar = document.querySelectorAll('.modificar');
let form = document.querySelector('form');
let concluir = document.querySelector('.concluir-modificacao');
const objeto = formobject();
let visita =  document.querySelectorAll('.visita');

let buscar_button = document.querySelector(".bbuscar")

console.log(form)


window.onload=()=>{
    adicionar_eventos();
};





function formobject(){
    let paciente = {
        'nome':form[0].value,
        'data_nascimento':form[1].value,
        'telefone':form[3].value,
        'email':form[4].value,
        'endereco':form[5].value,
        'bairro':form[5].value,
        };
    return paciente;
}

function adicionar_eventos(){
    let addClientes = document.querySelector('.addClientes');
    for(i=0 ;i < remover.length; i++ ){
        botao = remover[i]
        botao.addEventListener("click",(e)=>{
            idcliente = {
            'id' : e.target.parentNode.parentNode.dataset.id,
            }
            console.log(idcliente)
             $.post('/excluir/paciente',idcliente,()=>{
             let excluir = e.target.parentNode.parentNode;
             excluir.remove()
             })
          });
    }
    for(i=0 ;i < modificar.length; i++ ){
        botaom = modificar[i];  
        botaom.addEventListener("click",(e)=>{
            let id = e.target;
            let attr = {
                'id': id.getAttribute("data-id"),
            }
            console.log(id)   
            console.log(attr)     
            $.get('/verificar/paciente/', attr ,function(data){
                // console.log(data)
                let dado = formatardata(data.nascimento);
                form.setAttribute('data-id',attr['id']);
                // console.log(dado);
                form[0].value = data.nome_completo;
                form[1].value = dado;
                form[2].value = data.telefone;
                form[3].value = data.email; 
                form[4].value = data.endereco;
                form[5].value = data.bairro;
            })
        })
    }
    concluir.addEventListener('click',()=>{
        dados ={
            'id':form.getAttribute("data-id"),
            'nome':form[0].value,
            'data_nascimento':form[1].value,
            'telefone':form[2].value,
            'email':form[3].value,
            'endereco':form[4].value,
            'bairro':form[5].value,
        }
        console.log(dados)
        $.post("/modificar/pacientes",dados,()=>{
            console.log('feito')
            form.reset();
        })
    })
    addClientes.addEventListener('click',()=>{
        window.location.href = "main";
    });
    for(i=0;i<visita.length;i++){
        bvisita = visita[i]
        bvisita.addEventListener('click',(e)=>{
            id = e.target.parentNode.parentNode.dataset.id
            window.location.href = "/visita/"+id
        })
    }
}

function formatardata(data){
    var date = new Date(data);
    var dia  = date.getDate()+1;
    var mes = "0"+(date.getMonth()+1);
    if (mes>=10){
        var mes = date.getMonth()+1;
    }
    var ano = date.getFullYear();
return ano+"-"+mes+"-"+dia
}

