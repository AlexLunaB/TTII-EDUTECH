<template>
<v-container fluid>
</v-container>
</template>

<script>



  // Import this component
  import Trumbowyg from 'vue-trumbowyg';
  
  // Import editor css
  import 'trumbowyg/dist/ui/trumbowyg.css';
   
export default {

    
    name: "AddPost",
    data() {
        return {
            visible: false
        }
    },

    components: {
      Trumbowyg
    },

    methods: {
        handleStateClick: function () {

            this.$refs.addResource.showAddResource();
        }, 
    }
};
</script>

<style scoped>

</style>