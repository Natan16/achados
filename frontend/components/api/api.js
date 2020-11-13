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
        return post('api/adiciona_registro', {solicitante: solicitante, documento: documento, tipo_reg:tipo_reg});
    },
    lista_correspondencias(documento , tipo_reg){ 
        return get('api/lista_correspondencias', {documento: documento , tipo_reg: tipo_reg});
    },
    //PARA FAZER A APLICAÇÃO COMPLETA
    //cria_usuario
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
