
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
  </v-container>
</template>
<!-- é necessário ter algo relativo à localização -->
<!-- se a opção selecionada for Outros, é necessário abrir um campo a mais -->
<!-- se o item foi encontrado, fechar requisição -->
<script>
  //TODO : fazer melhor validação do formulário
  import Vuex from 'vuex'
  import AppApi from '~apijs'

  export default {
    computed: {},
    
    /*asyncData() {
      return AppApi.whoami().then(response => { 
        var user = response.data.user
        console.log(response)
        if( response.data.autenticated ) 
          return {name: user.name, email :user.email , autenticated : true }
        return {name:'' , email :'' , autenticated : false}

      })
  
    },*/
 

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

    methods: {
      checkCorrespondencia(registro){
        const tipoOposto = this.tipoRegistro == 'achado' ? 'perdido' : 'achado'
        return registro.status == 0 && registro.tipoRegistro == tipoOposto  

      },
      
      validate () {
        this.$refs.form.validate() //precisa de cadastro?
        //preenche novoachado -> não dá pra preencher enquanto preenche o form? vamos tentar 
        //TODO : falta isso aqui!!!!!!!
        //caso de estar na aba achado
        

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
        
        //EM_ABERTO , RESOLVIDO etc
        //const status = { //outra coisa que vai ser bom ficar numa Store???
        //  EM_ABERTO: 0,
        //  RESOLVIDO: 1,
        //} //pra isso vai adicionar à api função resolver, que resolve uma solicitação baseada no id dela
        AppApi.adiciona_registro(solicitante, documento , this.tipoRegistro).then(response => {
        
        }) //é esta a query que está falhando 
        
        this.$store.commit('SET_SOLICITANTE', solicitante);
        this.$store.commit('SET_DOCUMENTO', documento);
        
        //em vez de setar correspondências, poderia fazer várias chamadas de Api em respostas.vue para 
        //recuparar as correspondências essa página faria simplesmente os adds, faz sentido?
        this.$router.push({ name: 'tipoRegistro-resposta', params:{tipoRegistro:this.tipoRegistro} });

        
        
         
        // window.open('mailto:natanvianat16@gmail.com?subject=documento_encontrado&body=Aqui está seu documento');
        //guardar os dados do formulário no banco
        //a ação do validate é redirecionar para uma página que fala 
        // :enviaremos um email para você se o item for encontrado
        //window.open('mailto:test@example.com'); ou fazer uma chamada ajax para o servidor enviar o email
        //autenticação vai ser necessária se a pessoa quiser cancelar busca
        //no futuro, integrar reconhecimento facial ( dar opção de upload da foto )
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
<!-- <script>
import AppApi from '~apijs'
export default {
  data () {
    return {
      newtask: '',
      adding: false,
      loading: false,
      items: [
      ]
    }
  },
  mounted () {
    this.loading = true
    AppApi.list_todos().then(response => {
      const todos = response.data.todos
      this.items = todos
      this.loading = false
    })
  },
  methods: {
    add () {
      this.adding = true
      AppApi.add_todo(this.newtask).then(response => {
        const todo = response.data
        this.items.push(todo)
        this.newtask = ''
        this.adding = false
      })
    }
  }
}
</script>
 -->
<style scoped>

</style>
