
<template>
  <v-container>
    <v-form 
      ref="form"
      v-model="valid"
    >
    <!-- <v-container v-if="logged_user" > -->
        <v-layout row wrap>
          <v-text-field 
            :disabled="this.autenticated"
            v-model="nome"
            :rules="nameRules"
            label="Seu nome"
            required
          ></v-text-field>
          <v-spacer>
          </v-spacer>
       </v-layout>
        <v-layout row wrap>
          <v-text-field
            :disabled="this.autenticated"
            v-model="email"
            :rules="emailRules"
            label="Seu e-mail"
            required
          ></v-text-field>
          <v-spacer>
          </v-spacer>
        </v-layout>
        <v-divider></v-divider>
      <!-- </v-container> -->
      <v-layout row wrap>
          <v-layout row wrap>
          <v-select
            v-model="select"
            :items="documentos"
            :rules="[v => !!v || 'Documento é necessário']"
            label="Documento"
            required
          ></v-select>  
          </v-layout>
          <v-spacer>
          </v-spacer>
          <v-text-field
          v-model="numero"
          label="Numero"
          :rules="numeroRules"
          required
        ></v-text-field>
 
      </v-layout>
      <v-layout row wrap>
      <v-text-field
        v-model="outro"
        label="Tipo"
        v-if="select && select == 'Outro'" 
        > <!-- --> 
      
      </v-text-field>  
      <v-spacer>
          </v-spacer>

          <v-spacer>
          </v-spacer>   
      </v-layout>

      <v-layout row wrap>
      <v-text-field
          v-model="nomeProp"
          :rules="nameRules"
          label="Nome do Proprietário"
          required
      ></v-text-field>
      
      <v-spacer>
      </v-spacer>

      </v-layout>


      <v-checkbox
        v-model="checkbox"
        :rules="[v => !!v || 'Você deve concordar para continuar!']"
        label="Você concorda em receber e-mails do Achados & Perdidos?"
        required
      ></v-checkbox>
      <!-- <router-link :to="{name: 'encontrado', params:{encontrado: this.encontrado}}"></router-link> -->
      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="validate"
        style="border-radius:28px;"
      >
        Registrar
      </v-btn>

      <v-btn
        color="error"
        class="mr-4"
        @click="reset"
        style="border-radius:28px;"
      >
        Limpar
      </v-btn>

    </v-form>
    <login-dialog ref="login_dialog"/>
  </v-container>
</template>
<!-- é necessário ter algo relativo à localização -->
<!-- se a opção selecionada for Outros, é necessário abrir um campo a mais -->
<!-- se o item foi encontrado, fechar requisição -->
<script>
  //TODO : fazer melhor validação do formulário
  import Vuex from 'vuex'
  import AppApi from '~apijs'
  import loginDialog from '~/components/login-dialog.vue'

  export default {
    components: {
      loginDialog
    },
    computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),
    
    //form precisa capturar login
    data () {

      return {
        nome:'',
        email:'',
        tipoRegistro: this.$route.params.tipoRegistro,
        autenticated:false,
        adding :false,
        getting : false,
        valid: false, 
        nameRules: [ 
          v => !!v || 'Nome é necessário',
        ],
        emailRules: [
          v => !!v || 'E-mail é necessário',
          v => /.+@.+\..+/.test(v) || 'E-mail deve ser válido',
        ],
        select: null,
        documentos: [
          'RG',
          'CPF',
          'CNH',
          'RA',
          'Passaporte',
          'Carteira de Trabalho',
          'Carteira de Estudante',
          'Certidão de Nascimento',
          'Cartao de credito',
          'Cartao de debito',
          'Outro', 
        ],
        outro : '' ,
        outroRules : [ 
          v => !!v  || "Tipo do documento é necessário" 
        ],
        //cada tipo de documento tem suas próprias regras
        //talvez um objeto que consista no tipo de documento e nas regras para o seu número
        //ou um mapa que mapeie tipo em conjunto de regras , vai ser bom pois aqui aprendo Regex em javascript 
        numero : '',
        numeroRules : [
          v => !!v || "Numero do documento é necessário"//por enquanto está aceitando qualquer coisa, a regra que se aplica certamente depende de qual documento é selecionado
        ],
        nomeProp: '',
        checkbox: false,

      }
    },
    mounted(){
      if (this.logged_user){
        this.nome = this.logged_user.first_name + " " + this.logged_user.last_name
        this.email = this.logged_user.email
      }
    },

    methods: {
      //open_login_dialog (evt) {
       
      //  evt.stopPropagation();
      //}

      checkCorrespondencia(registro){
        const tipoOposto = this.tipoRegistro == 'achado' ? 'perdido' : 'achado'
        return registro.status == 0 && registro.tipoRegistro == tipoOposto  

      },
      
      validate () {
        this.$refs.form.validate() 
        
        const solicitante = {
          nome : this.nome , 
          email : this.email,
        }
        
        const documento = {
           tipo : this.select , 
           numero : this.numero ,
           outro : this.outro,
           nomeProp : this.nomeProp,  
        }
        
        //TODO : podia ter um loading aqui, pra colocar no botão 
        AppApi.adiciona_registro(solicitante, documento , this.tipoRegistro).then(response => {
            console.log("Resposta do adiciona_registro")
            console.log(response)
            if (!response.data){
              this.$refs.login_dialog.open(); 
            } 
            else {
              this.$store.commit('SET_SOLICITANTE', solicitante);
              this.$store.commit('SET_DOCUMENTO', documento);
        
              this.$router.push({ name: 'tipoRegistro-resposta', params:{tipoRegistro:this.tipoRegistro} });

            }  
        })  
        
      
      },
      reset () {
        this.$refs.form.reset()
      },
      //resetValidation () {
      //  this.$refs.form.resetValidation()
      //},
    },
  }
</script>

<style scoped>

</style>
