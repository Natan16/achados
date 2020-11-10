import Vuex from 'vuex'

const store = () => new Vuex.Store({

  state: {
    registro_atual : undefined, //não tem problemas ter informações aninhadas
    registros_correspondentes : undefined , 
  },
  //id
  mutations: {
    SET_REGISTRO(state , novoRegistro ){
        state.registro_atual = novoRegistro
    },
    //é uma lista com todos os registros achados correspondentes a um perdido ou vice-versa
    SET_REGISTROS_CORRESPONDENTES(state , novosRegistrosCorrespondentes){
      state.registros_correspondentes = novosRegistrosCorrespondentes
    }
    //pode criar um método para compor registro em algum ponto!!!
  },
  getters: {
    registro_atual(state) {
      return state.registro_atual
    },
    registros_correspondentes(state){
      return state.registros_correspondentes
    }, 

  }
})

export default store