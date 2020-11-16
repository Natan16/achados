import axios from '~/helpers/axios';

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const api = {
    login(username, password){
        return post('/api/login', {username: username, password: password});
    },
    logout(){
        return post('/api/logout');
    },
    whoami(){
        return get('/api/whoami');
    },
    adiciona_regsitro(solicitante , documento , tipo_reg){
        let solicitante_nome = solicitante.nome
        let solicitante_email = solicitante.email
        let doc_tipo = documento.tipo
        let doc_numero = documento.numero
        let doc_outro = documento.outro
        let doc_nome_prop = documento.nomeProp
        return post('/api/adiciona_registro', {solicitante_nome: solicitante_nome, solicitante_email: solicitante_email,
         doc_tipo:doc_tipo , doc_numero:doc_numero , doc_outro:doc_outro , doc_nome_prop:doc_nome_prop, tipo_reg:tipo_reg});
    },
    lista_correspondencias(documento, tipo_reg){
        let doc_tipo = documento.tipo
        let doc_numero = documento.numero
        let doc_outro = documento.outro
        let doc_nome = documento.nomeProp
        //e se bater o nome do usuário apenas ? -também tem que retornar, mas com alguma flag avisando que não é uma
        //correspondência perfeita
        return get('/api/lista_correspondencias', {doc_tipo:doc_tipo , doc_numero:doc_numero , doc_outro:doc_outro , doc_nome:doc_nome, tipo_reg:tipo_reg});
    },
    //PARA FAZER A APLICAÇÃO COMPLETA
    //cadastra_usuario
    //lista_registros
    //envia_email
    //resolve_registro
    //reabre_registro etc


}
export default api;

function get(url, params){
    return axios.get(url, {params: params});
}

function post(url, params){
    var fd = new FormData();
    params = params || {}
    Object.keys(params).map((k) => {
        fd.append(k, params[k]);
    })
    return axios.post(url, fd);
}
