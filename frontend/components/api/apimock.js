import Vue from 'vue'

var logged_user = null;
//table documentos 
//table registro_achado
//table registro_perdido ?

function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve({data: data}), 600)
  })
}

const api = {
    login(email, password){
        if(password){
            logged_user = {
                username: 'zuckbrau',
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                notifications_enabled: true,
                permissions:{
                    ADMIN: 'zuckbrau' == 'admin',
                    STAFF: 'zuckbrau' == 'admin',
                }
            };
        }
        console.log(logged_user)
        return mockasync(logged_user);
    },
    logout(){
        logged_user = null;
        return mockasync({});
    },
    whoami(){
        return mockasync(logged_user ? {
            authenticated: true,
            user: logged_user,
        } : {authenticated: false});
    },
   
    adiciona_registro(solicitante , documento , tipo){
        return mockasync({});
    },
    lista_correspondencias(documento , tipo){ 
        return mockasync({
            correspondencias: [
                {usuario : {nome: 'Natan Viana' , email:'natanvianat16@gmail.com'} , data:"10/11/12" , tipoRegistro:"achado"},
                {usuario : {nome: 'Mariana Inara' , email:'marianainaradacosta@gmail.com'} , data:"10/12/12", tipoRegistro:"achado"}
            ]
        });
    },

    
    //envia_email(email , texto){
    //    return mockasync({})  
    //},
    //lista_registros(usuario){
    //  return mockasync({});  
    //}
    //resolve_registro()//pelo id ?  

  
};

export default api;
