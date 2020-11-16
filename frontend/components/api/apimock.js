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
        const d = new Date()
        return mockasync(
            [
                {nome_solicitante: 'Natan Viana' , email_solicitante:'natanvianat16@gmail.com' ,
                avatar_solicitante:'http://1.bp.blogspot.com/-A9_ROvP0efw/TZI9dUsXAKI/AAAAAAAAGCI/rD_-a3ZBF3U/s1600/Isaac_Newton_Biography%255B1%255D.jpg',
                criado_em:d.toISOString() , tipo_reg:"achado"},
                {nome_solicitante: 'Mariana Inara' , email_solicitante:'marianainaradacosta@gmail.com' ,
                avatar_solicitante:'http://1.bp.blogspot.com/-A9_ROvP0efw/TZI9dUsXAKI/AAAAAAAAGCI/rD_-a3ZBF3U/s1600/Isaac_Newton_Biography%255B1%255D.jpg',
                criado_em:d.toISOString(), tipo_reg:"achado"}
            ]
        );
        //return mockasync([])
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
