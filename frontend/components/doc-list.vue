<!-- z4KyPHfHfJd3 -->
<template>
  <v-list two-line>
    <template v-for="doc in sortedDocs">
      <!-- TODO : adicionar outros dados depois, vamos tentar fazer o básico -->
      <!-- </v-list-tile> --> 
      <!-- talvez não precise do doc.vue -->
        {{doc.tipo}}
        <br>
        {{doc.numero}} 
        <br>
        marcar como resolvida
        <br>
        excluir
        <br>
        <!-- se houver, listar emails das pessoas que dizem ter encontrado ( ou perdido o item ) -->
      <v-divider></v-divider>
    </template>
  </v-list>
</template>

<script>

export default {
  props: ['docs'],
  data () {
    return {}
  },
  computed: {
    sortedDocs() {
      return this.docs //por enquanto não ordenados
      //return this.tweets.concat().sort((t1, t2) => new Date(t2.created_at) - new Date(t1.created_at))
    }
  }
}
</script>

<style>
</style>
