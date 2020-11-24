
<template>
  <div>
    <template v-for="reg in sortedRegs" >  
      <v-card
          class="mx-auto"
          color="#FFFFFF"
          max-width="900"
        >
            
            <p class="display-1 text--primary">
                  id: {{reg.id}}
                  <br>
                  tipo : {{reg.tipo_doc}}
                    &nbsp;
                  numero :&nbsp;{{reg.numero_doc}}
                  <br>
                  proprietario:&nbsp;{{reg.nomeProprietario_doc}}
                  <br>
                  status : em aberto
                  <br>
                  {{reg.tipo_reg}} {{reg.criado_em | timeago}}
            </p> 
                <v-divider></v-divider>
                
                  <template v-if="reg.correspondencias.length > 0">
                
                  
                    <v-list  subheader three-line>
                      
                      <v-subheader inset>
                        {{reg.correspondencias.length}} correspondencia(s) encontrada(s):
                      </v-subheader>
                      <template v-for="corr in reg.correspondencias" >
                        <v-list-item  
                          :key="corr.nome" >
                          
                          <v-avatar class="ma-0 ml-4" >
                            <v-img :src="corr.avatar"></v-img>
                          </v-avatar>
                          {{corr.nome}} ({{corr.criado_em | timeago}})
              
                          <br>
                          <p>Entre em contato através do e-mail <b>{{corr.email}}</b> para combinar os detalhes da devolução.</p>
                        </v-list-item>

                      </template>
                    </v-list>
                  </template>
                  <template v-else>
                    <p>
                    Por enquanto, não foram encontradas correspondencias  
                    </p>
                  </template> 

        
          <!-- a edição, por equando, não vai ser implementada -->
          <div style="padding:20px">
          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="mx-2"
              fab
              dark
              v-bind="attrs"
              v-on="on"
              color="success"
            >
              <v-icon dark>
                mdi-check
              </v-icon>
            </v-btn>
            </template>
            <span>Marcar como resolvido</span>
          </v-tooltip>

          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="mx-2"
              fab
              dark
              v-bind="attrs"
              v-on="on"
              color="yellow"
            >
              <v-icon dark>
                mdi-alert
              </v-icon>
            </v-btn>
            </template>
            <span>Marcar como em aberto</span>
          </v-tooltip>

          <v-tooltip bottom>
            <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="mx-2"
              fab
              dark
              v-bind="attrs"
              v-on="on"
              color="red"
              @click="exclui(reg.id)"
            >
              <v-icon dark>
                mdi-delete
              </v-icon>
            </v-btn>
            </template>
            <span>Excluir registro</span>
          </v-tooltip>

          

        
          </div>
          
        </v-card>
         <v-divider></v-divider>
      </template>   
  
  </div>
  
</template>

<script>

import AppApi from '~apijs'

export default {
  props: ['registros'],
  data () {
    return {}
  },
  mounted(){
    var i
    for(i=0; i<this.registros.length ; i++){   
      var registro = this.registros[i]
      const tipoRegistro = registro.tipo_reg
      const tipoRegistroCorr = tipoRegistro === 'achado' ? 'perdido' : 'achado'
      var documento = {}
      if (registro.outro_doc){
        documento.tipo == 'Outro'
        documento.outro = registro.tipo_doc
      } else {
        documento.tipo = registro.tipo_doc
        documento.outro = ''
      }
      documento.numero = registro.numero_doc
      documento.nomeProp = registro.nomeProprietario_doc    
      this.altera_correspondencia_registro(i , documento , tipoRegistroCorr)
    }
  },
  computed: {
    sortedRegs() {
      return this.registros.concat().sort((t1, t2) => new Date(t2.criado_em) - new Date(t1.criado_em))
    },
  }, 
  methods: {
    altera_correspondencia_registro(indice , documento , tipoRegistroCorr){
      AppApi.lista_correspondencias(documento , tipoRegistroCorr).then(result => {
          this.registros[indice].correspondencias = result.data
          console.log(this.registros[indice])
      })
    },
    exclui(id_registro){
      AppApi.exclui_registro(id_registro).then(result => { 
        var i 
        for (i = 0; i < this.registros.length ; i++){
          if (this.registros[i].id === id_registro){
            this.registros.splice(i , 1)
          }
        }
        return {}  
      })
    }
  },

}
</script>

<style>
</style>
