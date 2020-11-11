<!-- lembrar do middleware pra garantir que usuário está logado -->
<template>
 <doc-list :docs="docs"></doc-list>
 <!-- pode listar em 2 elementos. Os achados, e os perdidos -->
</template>

<script>

//aidiconar na parte de baixo qual é nossa missão ( o objetivo do site )
export default {
   computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),
   asyncData() { //tem que passar o usuário logado
    return AppApi.list_docs(this.logged_user).then(result => {
      return {
        docs: result.data //
      }
    })
  },
  data () {
    return {}
  }
}
//baixar dependências pelo 3g!
//psycopg deu erro
</script>

<style>
</style>
