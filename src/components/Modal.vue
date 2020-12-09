<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="290"
    >
      <!-- <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Open Dialog
        </v-btn>
      </template> -->
      <v-card>
        <v-card-title class="headline">
          {{headModalProp}}
        </v-card-title>
        <v-card-text> {{contentModalProp}} </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Disagree
          </v-btn>
          <v-btn
            color="green darken-1"
            text
            @click="dialog = false"
          >
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>


<script>
  export default {
    props: {
      
    },
    data () {
      return {
        dialog: false,
        headModalProp: String,
        contentModalProp: String
        
       
      }
    },
    methods: {
      showModal: function() {
      this.dialog = true;
      },

      setTextModal: function (headModal, contentModal) {
        // let myHeadModal = this.headModalProp
        // let myContentModal = this.contentModalProp
        
        this.headModalProp =  headModal;
        this.contentModalProp = contentModal;
      }
    },
    computed: {
      
    }
  }
</script>


