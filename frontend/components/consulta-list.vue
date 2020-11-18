
<template>
  <div>
    <template v-for="reg in registros" >  
      <v-card
          class="mx-auto"
          color="#FFFFFF"
          dark
          max-width="900"
        >
            
            <p class="display-1 text--primary">
              <v-container >
                  {{reg.id}}
              </v-container>
            </p>
          <!-- a edição, por equando, não vai ser implementada -->
          <div style="padding:20px">
              <v-btn
            class="mx-2"
            fab
            dark
            color="cyan"
          >
            <v-icon dark>
              mdi-pencil
            </v-icon>
          </v-btn>

          <v-btn
              class="mx-2"
              fab
              dark
              color="red"
              @click="exclui(reg.id)"
            >
              <v-icon dark>
                mdi-delete
              </v-icon>
          </v-btn>
          </div>
          
        </v-card>
         <v-divider></v-divider>
      </template>   
  
  </div>
  <!-- <div>
    <template v-for="reg in registros">
       {{reg.nome}}
       <v-btn > excluir </v-btn> 
    </template>
  </div> -->
</template>

<script>

import AppApi from '~apijs'

export default {
  props: ['registros' , 'correspondencias'],
  data () {
    return {}
  },
  computed: {
    //sortedCorrs() {
    //  return this.correspondencias.concat().sort((t1, t2) => new Date(t2.criado_em) - new Date(t1.criado_em))
    //},
  }, 
  methods: {
    exclui(id_registro){
      AppApi.exclui_registro(id_registro).then(result => { 
        return {}  
      })
    }
  },

}
</script>

<style>
</style>
