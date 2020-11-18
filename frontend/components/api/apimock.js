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

    
    envia_email(email , texto){
        return mockasync({})  
    },

    google_login(id_token){
        logged_user = {
                username: 'zuckbrau',
                first_name: 'Mark',
                last_name: 'Zuckerberg',
                email: 'zuck@facebook.com',
                avatar: 'http://1.bp.blogspot.com/-A9_ROvP0efw/TZI9dUsXAKI/AAAAAAAAGCI/rD_-a3ZBF3U/s1600/Isaac_Newton_Biography%255B1%255D.jpg',
                notifications_enabled: true,
                permissions:{
                    ADMIN: 'zuckbrau' == 'admin',
                    STAFF: 'zuckbrau' == 'admin',
                }
            };
        return mockasync(logged_user)  
    },


        
    consulta_registros(){
        var d = new Date()
        return mockasync([{
            id: "1",
            nome:"Natan",
            email: "natanvianat16@gmail.com",
            avatar: "http://1.bp.blogspot.com/-A9_ROvP0efw/TZI9dUsXAKI/AAAAAAAAGCI/rD_-a3ZBF3U/s1600/Isaac_Newton_Biography%255B1%255D.jpg",
            tipo_doc: "RG",
            outro_doc: "",
            numero_doc: "1234",
            nomeProprietario_doc: "Natan Lima Viana",
            criado_em: d.toISOString(),
            status: 0,
            tipo_reg: "perdido"
        },{
            id: "2",
            nome:"Natan",
            email: "natanvianat16@gmail.com",
            avatar: "http://1.bp.blogspot.com/-A9_ROvP0efw/TZI9dUsXAKI/AAAAAAAAGCI/rD_-a3ZBF3U/s1600/Isaac_Newton_Biography%255B1%255D.jpg",
            tipo_doc: "RG",
            outro_doc: "",
            numero_doc: "1234",
            nomeProprietario_doc: "Natan Lima Viana",
            criado_em: d.toISOString(),
            status: 0,
            tipo_reg: "perdido"
        }])
    },

    exclui_registro(id){
        return mockasync({})
    },
    
    /*toggle_status(){

    }*/ 

  
};

export default api;
