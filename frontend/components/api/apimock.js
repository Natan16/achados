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
    /*
    add_todo(newtask){
        return mockasync({description: newtask, done: false});
    },
    list_todos(){ //na verdade, vem de uma consulta sql
        return mockasync({
            todos: [
                {description: 'Do the laundry', done: true},
                {description: 'Walk the dog', done: false}
            ]
        });
    },*/
    //no caso de ter perdido em um estabelecimento, já vai saber onde que é pra buscar
    //recebe um registro e retorna os registros correspondentes
    get_correspondencias(registro){
       return mockasync({})
    },
  
    add_usuario(nome , email , lista_registros , possui_login){
        return mockasync({})
    },
    add_registro(){
        return mockasync({})
    },
    add_documento( tipo , numero , nome_proprietario , outro){
        return mockasync({})
    }, 
  
};

export default api;
