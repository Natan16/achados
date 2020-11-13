export const state = () => ({
    logged_user: undefined,
    snack: {},    
    solicitante : {},
    documento : {},    
})

export const mutations = {
    SET_LOGGED_USER(state, logged_user) {
      console.log('set logged user: '+JSON.stringify(logged_user))
      state.logged_user = logged_user
    },
    SET_SNACK_STATE(state, newstate) {
      state.snack = newstate
    },
    SET_SOLICITANTE(state, novoSolicitante){
      state.solicitante = novoSolicitante 
    },
    SET_DOCUMENTO(state, novoDocumento){
      state.documento = novoDocumento 
      console.log(state.documento)
    },

}

export const getters = {
    logged_user(state) {
      return state.logged_user
    },
    snack (state) {
      return state.snack
    },
    solicitante(state) {
      return state.solicitante
    },
    documento(state){ //o que não funcionou foi o SET_DOCUMENTO
      return state.documento
      //return state.documento
  }, 
}

