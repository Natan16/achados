<template>
  <v-toolbar color="#1565C0" dark fixed app clipped-right>
    <!-- <v-toolbar-side-icon @click.stop="state.drawer = !state.drawer"></v-toolbar-side-icon> -->
    <v-btn :to="{ name: 'index'}" x-large flat dark ripple class="ma-0 ml-5" >
      <img src="home_icon.png" style="height: 40px; width: 80px;" />
    </v-btn><v-spacer></v-spacer>
    <v-btn v-if="logged_user" :to="{ name :'consulta'}" flat dark ripple class="ma-0 ml-5" > <!-- se o usuário não está logado vai abrir o form de login , se ele está, vai abrir a lista de registros-->
      Consultar Registros
    </v-btn>
    <v-btn  v-if="!logged_user" flat dark ripple class="ma-0 ml-5" @click="open_login_dialog($event)"> <!-- se o usuário não está logado vai abrir o form de login , se ele está, vai abrir a lista de registros-->
      Consultar Registros
    </v-btn>
    
  
    <v-btn v-if="!logged_user" flat dark ripple class="ma-0 ml-5"  @click="open_login_dialog($event)">Login</v-btn>
    <v-menu v-if="logged_user" offset-y>
      <v-btn icon slot="activator" class="ma-0 ml-5">
        <v-avatar size="36px">
          <img :src="logged_user.avatar">
        </v-avatar>
      </v-btn>
      <v-card class="no-padding">
        <v-list two-line>
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <v-avatar>
                <img :src="logged_user.avatar">
              </v-avatar>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>{{logged_user.first_name}} {{logged_user.last_name}}</v-list-tile-title>
              <v-list-tile-sub-title>{{logged_user.email}}</v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
        <v-divider></v-divider>
        <!-- o loggout ainda não foi implementado -->
        <v-list>
          <v-list-tile @click="logout()">
            <v-list-tile-content>
              <v-list-tile-title>Sair</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-menu>
   <!--  <v-toolbar-side-icon @click.stop="state.drawerRight = !state.drawerRight"></v-toolbar-side-icon> -->
    <login-dialog ref="login_dialog"/>
  </v-toolbar>
</template>

<script>
  import Vuex from 'vuex'
  import loginDialog from '~/components/login-dialog.vue'
  import Snacks from '~/helpers/Snacks.js'
  import AppApi from '~apijs'
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
    props: ['state'],
    methods: {
      open_login_dialog (evt) {
        this.$refs.login_dialog.open();
        evt.stopPropagation();
      },
      logout(){
        var auth2 = gapi.auth2.getAuthInstance();
        auth2.signOut().then(function () {
          console.log('User signed out.');
        });

        AppApi.logout().then(()=>{
          this.$store.commit('SET_LOGGED_USER', null);
          //Snacks.show(this.$store, {text: 'Até logo!'})
        });
      }
    }
  }
</script>