
<!-- z4KyPHfHfJd3 -->
<template>
<div>

    <template v-for="corr in sortedCorrs">
      <v-card
        style="margin-top:20px"
        class="mx-auto"
        color="#2196F3"
        dark
        max-width="900"
        >
        <div >
          <div style="text-align:left;color:#FFFFFF;padding:20px" class="display-1">
            <v-avatar>
              <img :src="corr.avatar_solicitante">
            </v-avatar>
            {{corr.nome_solicitante}}
            ({{corr.criado_em | timeago}})
          </div>
           <!-- padding e alinhar à esquerda -->
        
        </div>
      </v-card>
      <v-card
        class="mx-auto"
        color="#90CAF9"
        dark
        max-width="900"
      >
       
          <p class="display-1">
            <v-container v-if="tipoRegistro=='achado'" >
                Olá, você achou o meu documento!
            </v-container>
            <v-container v-if="tipoRegistro=='perdido'" >
                Olá, achei o seu documento!
            </v-container>
          </p>
        <div style="padding:20px">
          Entre em contato através do e-mail <b>{{corr.email_solicitante}}</b> para combinar os detalhes da devolução.
          
        </div>
      </v-card>

    </template>
  </div>
</template>

<script>
import colors from 'vuetify/lib/util/colors'

export default {
  props: ['correspondencias' , 'tipoRegistro'],
  data () {
    return {}
  },
  computed: {
    sortedCorrs() {
      return this.correspondencias.concat().sort((t1, t2) => new Date(t2.criado_em) - new Date(t1.criado_em))
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
   {
    background-color: #000000;
  }

</style>
