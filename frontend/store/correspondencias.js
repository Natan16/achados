import Vuex from 'vuex'

const store_correspondencias = () => new Vuex.Store({
 
  state: {
    formulario : {},
    correspondencias : [], 
  },
  //id
  mutations: {

    SET_FORMULARIO(novo_formulario){
        state.formulario = novo_formulario //tem que tomar o cuidado que apagar esses caras na hora adequada
    },
    SET_CORRESPONDENCIAS(novas_correspondencias){
        state.correspondencias = novas_correspondencias
    },
    //ADD_CORRESPONDENCIAS(){

    //}
    //é uma lista com todos os registros achados correspondentes a um perdido ou vice-versa
    
  },
  getters: {
    formulario(state) {
      return state.formulario
    },
    correspondencias(state){
      return state.correspondencias
    }, 

  }
})

export default store_correspondencias