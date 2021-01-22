<template>
  <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="red lighten-2"
          dark
          v-bind="attrs"
          v-on="on"
        >
          Política de privacidad
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline grey lighten-2">
          Terminos y condiciones
        </v-card-title>

        <v-card-text>
          <h4>Información que es recogida</h4>
          El sistema podrá recoger información personal, por ejemplo: Nombre, información de
          contacto como su dirección de correo electrónica e información demográfica. Así
          mismo cuando sea necesario podrá ser requerida información específica para
          procesar una solitud de información.

          <h4>Uso de la información recogida</h4>
          El sistema emplea la información con el fin de proporcionar el mejor servicio posible,
          particularmente para mantener un registro de usuarios, de solicitudes de información
          en caso de que aplique, y mejorar nuestros productos y servicios. Es posible que
          sean enviados correos electrónicos periódicamente a través de nuestro sitio
          información que pueda resultarle de interés, estos correos electrónicos serán
          enviados a la dirección que usted proporcione, está altamente comprometido para
          cumplir con el compromiso de mantener su información segura. Usamos los sistemas
          seguros y los actualizamos constantemente para asegurarnos que no exista ningún
          acceso no autorizado.

          <h4>Control de su información personal</h4>
          No se venderá, cederá ni distribuirá la información personal que es recopilada sin su
          consentimiento, salvo que sea requerido por un juez con un orden judicial.
          Nos reservamos el derecho de cambiar los términos de la presente Política de
          Privacidad en cualquier momento.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            Cerrar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tituloModal: "Politicas de privacidad",
      tituloContenido: "",
      dialog: false,
    };
  },
  methods: {
    
  },
};
</script>