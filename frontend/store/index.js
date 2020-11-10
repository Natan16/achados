import Vuex from 'vuex'

const store = () => new Vuex.Store({

  state: {
    logged_user: undefined,
    snack: {}, 
    documento : undefined, //  
    id_registro : undefined //id do último registro  c
    //registro tem que ter uma tag ( finalizado ), o usuário vai marcar se foi finalizado
  },
  //id
  mutations: {
    SET_LOGGED_USER(state, logged_user) {
      console.log('set logged user: '+JSON.stringify(logged_user))
      state.logged_user = logged_user
    },
    SET_SNACK_STATE(state, newstate) {
      state.snack = newstate
    },


  },
  getters: {
    logged_user(state) {
      return state.logged_user
    },
    snack (state) {
      return state.snack
    },

  }
})

export default store