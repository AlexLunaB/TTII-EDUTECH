import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css'
import "@fortawesome/fontawesome-free/css/all.css"
import "material-design-icons-iconfont/dist/material-design-icons.css"
import colors from "vuetify/lib/util/colors";
Vue.use(Vuetify);

export default new Vuetify({
  icons:{
    iconfont: 'md' || 'fa' ||  'mdiSvg' || 'mdi'
  },

  theme:{
    themes:{
      light:{
        background: "#e8ded2"
      },
      dark: {
        background: colors.grey.lighten1
      }
    }
  }

});
