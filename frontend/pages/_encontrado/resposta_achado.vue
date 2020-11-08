<template>
  <div>

    <h1 >
      O documento que você encontrou foi registrado com sucesso.
    </h1>
    <br> 
    <h1>
      Por equanto, não existem correspondências.
    </h1>
    <br>
    <h1>
       Entraremos em contato caso o documento seja encotrado.
    </h1>
    <br>
    <h1>
       Obrigado!
    </h1>
  </div>
</template>
<script>

// user/_username/index.vue
//  - ViewUser.vue
//    - UserCard.vue
//    - Timeline.vue


//import viewuser from '~/components/ViewUser.vue'
import AppApi from '~apijs'

export default {
  components: {
    //viewuser
  },
  asyncData (context) {
    const encontrado = context.params.encontrado
    console.log("entrou aqui")
    return {encontrado ,} 
    //serve para fazer várias promessas
    /*return Promise.all([
      AppApi.get_user_details(username),
      AppApi.list_tweets(username)
    ]).then(results => {
      //isso aqui é adiciona à data de maneira assíncrona 
      return {
        
        tweets: results[1].data
      }
    })*/
    //dar a possibilidade de apagar ou de editar o registro
    //mandar por email um código para acessar o registro 
    //dar a possibilidade de reenviar o código 
  },
  data () {
    
    return {
    }
  }
}
</script>

<style>
  h1 {text-align: center;color:blue;}


</style>
