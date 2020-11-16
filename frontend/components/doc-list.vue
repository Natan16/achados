<!-- z4KyPHfHfJd3 -->
<template>
<div>

  <v-list two-line>
    <template v-for="corr in sortedCorrs">
      {{corr.nome_solicitante}} alega ter {{corr.tipo_reg}} o documento registrado em {{corr.criado_em}}.
      você pode contactá-lo através do e-mail {{corr.email_solicitante}} para que a devolução do
      documento seja efetivada.
      <v-divider></v-divider>
    </template>
  </v-list>
</div>
</template>

<script>

export default {
  props: ['correspondencias'],
  data () {
    return {}
  },
  computed: {
    sortedCorrs() {
      return this.correspondencias //por enquanto não ordenados
      //return this.tweets.concat().sort((t1, t2) => new Date(t2.created_at) - new Date(t1.created_at))
    },
    documento(){
      return this.$store.getters.documento
    },
    //logged_user() {
    //  return this.$store.getters.logged_user
    //},
  }
}
</script>

<style>
</style>
