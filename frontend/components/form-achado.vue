<template>
  <v-form
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-text-field
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Nome"
      required
    ></v-text-field>

    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
      required
    ></v-text-field>

    <v-select
      v-model="select"
      :items="documentos"
      :rules="[v => !!v || 'Item is required']"
      label="Documento"
      required
    ></v-select>  

    <v-text-field
      v-model="outro"
      label="Tipo"
      v-if="select && select == 'Outro'"> 
    </v-text-field>
    

    <v-checkbox
      v-model="checkbox"
      :rules="[v => !!v || 'Você deve concordar para continuar!']"
      label="Você concorda em compartilhar seu email com quem alegue ter perdido o documento?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
    >
      Validar
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Limpar
    </v-btn>

  </v-form>
</template>
<!-- é necessário ter algo relativo à localização -->
<!-- se a opção selecionada for Outros, é necessário abrir um campo a mais -->
<!-- se o item foi encontrado, fechar requisição -->
<script>
  import AppApi from '~apijs'
  export default {
    data: () => ({
      loading: false,
      valid: true,
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
      checkbox: false,
    }),

    methods: {
      validate () {
        this.$refs.form.validate() //precisa de cadastro?
        //verifica no servidor se o dono desse documento já está lá
        /*this.loading = true
        AppApi.list_todos().then(response => {
          const todos = response.data.todos
          this.items = todos
          this.loading = false
        })
        //adiciona documento perdido no servidor
        AppApi.add_todo(this.newtask).then(response => {
          const todo = response.data
          this.items.push(todo)
          this.newtask = ''
          this.adding = false
        })*/
         
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
      resetValidation () {
        this.$refs.form.resetValidation()
      },
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
