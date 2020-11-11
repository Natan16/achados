import Vue from 'vue'

var logged_user = null;
var documentos_achados = [{id:1, nome : 'Natan Viana' , tipo: 'RG' , numero : 585291 ,email:'natanvianat16@gmail.com' , encontrado : false } , 
        {id:2, nome : 'Mariana Inara' , tipo: 'PIU' , numero : 47213084 , encontrado : true ,email:'marianapiupiupiu@gmail.com' }]
var documentos_perdidos = [{id:1, nome : 'Natan Viana' , tipo: 'RG' , numero : 585291 ,email:'natanvianat16@gmail.com' , encontrado : false } , 
        {id:2, nome : 'Mariana Inara' , tipo: 'PIU' , numero : 47213084 , encontrado : true ,email:'marianapiupiupiu@gmail.com' }]
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
    get_achado(perdido){//passando um perdido
        //inserir aqui uma lista de achados achados : [{} , {} , ... ]
        
        //pode ser que mais de um item corresponda à pesquisa, nesse caso, retornar uma lista de 
        //documentos
        if ( (perdido.numero == 585291 && perdido.tipo == 'RG')|| perdido.nome == 'Natan Viana' ){//primeiro nome e iniciais dos outros nomes iguais
            return mockasync({
                documento: documentos_achados[0]
            })    
        }
        return mockasync({
            documento: null //caso não seja encontrado
        })
    },
  
    add_usuario(nome , email , lista_registros , possui_login){
        return mockasync({})
    },
    add_registro(){
        return mockasync({})
    },
    add_document(){
        return mockasync({})
    }, 
  
};

export default api;
