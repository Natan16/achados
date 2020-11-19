<template>
  <v-dialog v-model="visible" max-width="500px">
   
    

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
              <v-flex xs12><div id="google-signin-button"></div></v-flex>
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

  mounted() {
        setTimeout(() => {
          gapi.signin2.render('google-signin-button', {
          onsuccess: this.onSignIn
        })
      })
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
      // console.log('invoking onSignin...')
      // const profile = user.getBasicProfile()
      // console.log('ID: ' + profile.getId()) // Don't send this directly to your server!
      // console.log('Full Name: ' + profile.getName())
      // console.log('Given Name: ' + profile.getGivenName())
      // console.log('Family Name: ' + profile.getFamilyName())
      // console.log('Image URL: ' + profile.getImageUrl())
      // console.log('Email: ' + profile.getEmail())

      // // The ID token you need to pass to your backend:
      // var id_token = user.getAuthResponse().id_token
      // console.log('ID Token: ' + id_token)

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
          //o loggedUser nunca está voltando pra Null
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

