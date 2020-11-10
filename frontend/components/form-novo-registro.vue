
<template>
  <v-container>
    <v-form 
      ref="form"
      v-model="valid"
      lazy-validation
    >
    <!-- <v-container v-if="logged_user" > -->
        <v-layout row wrap>
          <v-text-field
            v-model="name"
            :counter="30"
            :rules="nameRules"
            label="Seu nome"
            required
          ></v-text-field>
          <v-spacer>
          </v-spacer>
       </v-layout>
        <v-layout row wrap>
          <v-text-field
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
            :rules="[v => !!v || 'Item is required']"
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
          v-model="nameProp"
          :counter="30"
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
      >
        Registrar
      </v-btn>

      <v-btn
        color="error"
        class="mr-4"
        @click="reset"
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
  /*const routes = [
    {
      name: "foo",
      path: "/foo",
      component: Foo
    }, 
    {
      name: "bar",
      path: "/bar",
      component: Bar
    }
  ];

  const router = new VueRouter({
    routes
  });*/

  import AppApi from '~apijs'
  export default {
    computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),
    props: ['toggle_registro'],
    data: () => ({
      adding :false,
      getting : false, 
      valid: false,
      name: '', 
      nameRules: [ 
        v => !!v || 'Nome é necessário',
        v => (v && v.length <= 30) || 'Nome deve conter menos do que 30 caracteres',
      ],
      email: '',
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
      nameProp: '',
      checkbox: false,

      novoachado : null, //tem que ter todos os parametros do form

      id_registro : '',
      idRules : [
        v => !!v || 'ID é necessário',
      ]
    }),

    methods: {

      
      validate () {
        this.$refs.form.validate() //precisa de cadastro?
        //preenche novoachado -> não dá pra preencher enquanto preenche o form? vamos tentar 
        //TODO : falta isso aqui!!!!!!!
        //caso de estar na aba achado
        this.novoachado = {
          name : this.name , 
          email : this.email , 
          select : this.select , 
          numero : this.numero ,
        }

        //adiciona documento perdido no servidor
        this.adding = true
        AppApi.add_achado(this.novoachado).then(response => {
          //const todos = response.data.todos
          //this.items = todos
          this.adding = false
        })

        this.getting = true 
        
        var id = null 
        var perdedor = null 
        var documento = null

        //verifica no servidor se o dono desse documento já está lá
        AppApi.get_perdido(this.novoachado).then(response => {
          //pode inclusive voltar uma lista de registros de perdidos ou de achados
          id = response.data.id
          perdedor = response.data.perdedor
          documento = response.data.documento //volta alguma coisa se esse documento já foi dado como
          //perdido
          this.getting = false
        })
        //se foi encontrado, tem que dar um jeito de passar o registro encontrado
        //pode ser pela propria store
        this.$router.push({ name: 'encontrado-respostaachado', params: { encontrado: Boolean(documento) } });
        //form-achado deveria compartilhar as informações de documento com resposta_achado 
        //documento deveria estar em uma store



        //redireciona para página adequada -> nesse momento é hora de usar um _$variavel para
        //saber para que tipo de pagina devemos redirecionar, dependendo sem usuário está logado ou não
        //e se documento adicionado foi encontrado ou não -> passar na query pararmetros encontrados

         
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
