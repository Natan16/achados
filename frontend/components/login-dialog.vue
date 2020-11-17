<template>
  <v-dialog v-model="visible" max-width="500px">
    <script src="https://apis.google.com/js/platform.js" async defer></script>
    <meta name="google-signin-client_id" content="649795675193-qiheujqkem1i9k0r7boqr0o0c9n5rk83.apps.googleusercontent.com" >
    

    <v-card>
        
        <!-- <v-card-title>Log in</v-card-title>
        <v-card-text>
          <v-container fluid>
            <v-text-field label="Email" required v-model="username"/>
            <v-text-field label="Senha" type="password" required v-model="password" @keyup.enter="login()"/>
            <small style="color: red;" v-if="error">Wrong user or password</small>
          </v-container>
        </v-card-text>
        <v-btn class="blue--text darken-1" flat @click="close()">Cancelar</v-btn>
        <v-btn class="blue--text darken-1" flat @click="login()" :loading="loading" :disabled="loading">Login</v-btn> -->
          <v-card-text>
            <p>Faça login usando um dos serviços abaixo</p>
            <v-layout row wrap>
              <v-flex xs12><div class="g-signin2" data-onsuccess="onSignIn"></div></v-flex>
            <!--   <v-flex xs12><v-btn block round color="info" href="/login/facebook">Facebook</v-btn></v-flex> -->
            </v-layout>
          </v-card-text>
       <!--  <p>
          Não tem uma conta?
          <router-link to="/cadastro" @click="close()">
           Cadastre-se </router-link> 
        </p> -->
        <!--  -->
        <!-- LdFeNFIZ72E3JAqRGUnElwIz -->
    </v-card>
  </v-dialog>
</template>

<script>

import AppApi from '~apijs'

export default {
  data () {
    console.log('data');
    return {
      visible: false,
      loading: false,
      username: '',
      email:'',
      emailRules: [
        v => !!v || 'E-mail é necessário',
        v => /.+@.+\..+/.test(v) || 'E-mail deve ser válido',
      ],
      password: '',
      error: false,
      img_url: '',
    };
  },
  methods: {
    open(){
      this.visible = true;
      console.log('Open');
    },
    close(){
      this.visible = false;
      console.log('Close');
    },
    login(){
      this.loading = true;
      this.error = false;

      AppApi.login(this.username, this.password).then((result)=>{
        var user = result.data;
        if(user){
          this.$store.commit('SET_LOGGED_USER', user);
          this.visible = false;
          console.log('logged')
        } else {
          this.error = true;
        }
        this.loading = false;
      });
    },
    onSignIn(googleUser){ 
      var profile = googleUser.getBasicProfile();
      if(profile){
        this.loading = true;
        this.error = false;
        var id_token = googleUser.getAuthResponse().id_token
        AppApi.google_login(id_token).then((result)=>{ 
          var user = result.data;
          if(user){
            this.$store.commit('SET_LOGGED_USER', user);
            this.visible = false;
            console.log('logged')
          } else {
            this.error = true;
          }
          this.loading = false;
        });
      }
    },
  }
}

</script>

<style type="text/css">
  p {
    padding: 35px;
  }
</style>
