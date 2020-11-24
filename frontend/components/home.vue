<template>
 <div>
   
    <div class="text-xs-center" style="margin:100px;">
         <v-btn  color="success" style="border-radius:50px; width:300px ;height: 100px" :to="{name: 'tipoRegistro-novo-registro', params:{tipoRegistro: 'achado'} }" ><h1>Achei</h1>&nbsp; um documento</v-btn>
      
         <v-btn style="border-radius:50px; width:300px ;height: 100px" color="error"   :to="{name: 'tipoRegistro-novo-registro', params:{tipoRegistro:'perdido'}}"><h1>Perdi</h1>&nbsp; um documento</v-btn>   
    </div>
    
    
  
  <p></p>
  <div>    

    <div style="width: 400px; margin-left:100px">
      <h2>Nossa missão</h2> 
    Dezenas de milhares de documentos são perdidos todo ano no Brasil. Muitas vezes, a pessoa que achou não se dá ao trabalho de levar o documento até o setor de achados e perdidos do orgão público resposável. E, ainda assim, a pessoa que perdeu tem que pagar alguma taxa. Essa plataforma tem como objetivo facilitar esse processo, oferencendo um serviço GRATUITO para conectar quem perdeu a quem achou um documento.  
    </div> 
   </div>


</div>
</template>

<script>

export default {
  data () {
    return {}
  }
}
</script>

<style>
</style>
