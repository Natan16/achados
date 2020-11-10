
<template>
  <v-container>
    <v-progress-linear :indeterminate="true" v-if="loading"></v-progress-linear> <!-- colocar alguns desses caras enquanto
    esperar a consulta no banco de dados -->
    <v-form 
      ref="form"
      lazy-validation
    >
      <v-layout row wrap>
      <v-text-field
          v-model="id_registro"
          :rules="idRules"
          label="ID"
          required
        ></v-text-field>
         <v-btn
          class="mx-2"
          fab
          dark
          small
          color="primary"
          @action="search"
        >
          <v-icon dark>
            mdi-magnify
          </v-icon>
        </v-btn>
          <v-spacer>
          </v-spacer>
          <v-spacer>
          </v-spacer>
        </v-layout>
    </v-form>
    <v-btn
      class="blue--text darken-1"
    >
    Esqueceu o ID? <!-- redirecionar para uma página de recuperação de ID -->
    </v-btn>
      <v-layout row wrap>
        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>
        
        <v-spacer>
        </v-spacer>
        
        <v-spacer>
        </v-spacer>
         
      
      </v-layout>

    <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="success"
          dark
          v-bind="attrs"
          v-on="on"
          @click="validate"
        >
          REENVIAR ID
        </v-btn>
      </template>

      <v-card>
      

        <v-card-text>
          Um e-mail foi enviado para {{email}} com o ID da solicitação 
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
    <br>

    Nenhuma solicitação com esse ID foi encontrada
  </v-container>
</template>
<!-- é necessário ter algo relativo à localização -->
<!-- se a opção selecionada for Outros, é necessário abrir um campo a mais -->
<!-- se o item foi encontrado, fechar requisição -->
<script>
  //se o ID é diferente para cada registro, não faz sentido pedir somente o email 

  import AppApi from '~apijs'
  export default {
    props: ['tipoRegistro'],
    data: () => ({
      getting : false, 
      dialog : false,
      email : '',
      emailRules: [
        v => !!v || 'E-mail é necessário',
        v => /.+@.+\..+/.test(v) || 'E-mail deve ser válido',
      ],
      id_registro : '',
      idRules : [
        v => !!v || 'ID é necessário',
      ]
    }),

    methods: {

      
      search () {
       //this.$refs.form.validate() //precisa de cadastro?
        //preenche novoachado -> não dá pra preencher enquanto preenche o form? vamos tentar 
        //TODO : falta isso aqui!!!!!!!
        
        var id = this.id_registro
        var solicitante = null 
        var documento = null
        this.getting = true 
        //verifica no servidor se o dono desse documento já está lá
        //achado ou perdido tem de ser passado adiante
        if (this.props.tipoRegistro == 'achado'){
          AppApi.getRegistroAchadoByID(this.id_registro).then(response => {
            solicitante = response.data.solicitante
            documento = response.data.documento
            this.getting = false
          })
        }
        else {
          AppApi.getRegistroPerdidoByID(this.id_registro).then(response => {
            solicitante = response.data.solicitante
            documento = response.data.documento
            this.getting = false
          })
        }

        if ( solicitante == null && documento == null){
          //mudar variavel que vai mostrar que nenhuma solicitação foi encontrada com esse id
        }
        else {
          //redirecionar para uma página usando id como parâmetro ( passar tudo de solicitante e documento também ?)
          //talvez o certo fosse redirecionar para nova página ( talvez a mesma depois de ser criado um registro)
          //colocar os parametros numa store
          this.$store.commit('registro/SET_REGISTRO' , ) //construir o objeto
          //redirecionar para página que vai mostrar o registro e oferecer as opções
        }
        //v-for desse novo component ( solicitante e documento  passados como prop)
        //se retornou alguma coisa, então mostrar na tela ( dados mock )
        //component com botões para resolver, editar e excluir


        //this.$router.push({ name: 'encontrado-respostaachado', params: { encontrado: Boolean(documento) } });

         
        window.open('mailto:natanvianat16@gmail.com?subject=documento_encontrado&body=Aqui está seu documento');
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
