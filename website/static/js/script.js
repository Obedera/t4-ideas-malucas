let itensFormulario = document.querySelectorAll('input');
function checarOpcao(){
    let opcao = document.querySelector('select').value;
    if(opcao == 'OUTROS'){
        for(let i of itensFormulario){
            if(i.name == 'categoria_outros'){
                i.type = 'text';
            }
        }
    }
    else if(opcao != 'OUTROS'){
        for(let i of itensFormulario){
            if(i.name == 'categoria_outros'){
                i.type = 'hidden';
            }
        }
    }
}