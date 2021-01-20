<template>
  <v-container class="contenedor" fluid>

    <v-row>
      <v-col cols="12">
        <v-container fluid>

          <v-card :loading="loading">
            <v-card-title><h3>Tal vez te interese</h3></v-card-title>
            <v-card-text>
              <VueHorizontalList :items="recomendados" :options="options">
                <template v-slot:nav-prev>
                  <div>👈</div>
                </template>

                <template v-slot:nav-next>
                  <div>👉</div>
                </template>

                <template v-slot:default="{ item }">

                  <div>
                    <div class="image-container">
                      <div class="image-content">
                        <img :src="item.recurso_img"  />

                        <div class="image-text">
                          <h2>{{ item.nombreRecurso }}</h2>
                        </div>
                      </div>
                    </div>

                    <div class="subtitle">{{item.estado}}</div>

                    <p>{{ item.descripcion }}</p>

                    <div>

                      <v-btn
                      color="orange"
                      text
                      @click="showRecursoDetail(item.id)"
                      
                    >
                      Explorar
                    </v-btn>

                    </div>

                    
                  </div>

                </template>
              </VueHorizontalList>
            </v-card-text>
          </v-card>
        </v-container>

      </v-col>

    </v-row>


    <v-row>
      <v-col cols="12" sm="12" md="6">

        <v-card
          class="mx-auto"
          outlined
        >
          <v-card-title>¿Que deseas Buscar?</v-card-title>

          <v-container>

            <v-text-field
              v-model="search"
              v-on:keyup.enter="GetDetalle()"
              prepend-icon="fas fa-search"
              single-line
            ></v-text-field>
          </v-container>

          <v-card-actions>
            <v-btn
              outlined
              rounded
              text
            >
              Button
            </v-btn>
          </v-card-actions>
        </v-card>


        <v-card></v-card>


      </v-col>
      <v-col cols="12" sm="12" md="6">

        <v-card
          class="mx-auto"
          outlined
        >
          <v-card-title>Acerca de Tu búsqueda</v-card-title>


          <v-container>
            Resultados para... <H3>{{search}}</H3>
            <h3></h3>

            <template v-for="r in rangos">
              <v-chip
                class="ma-2"
                label
                text-color="white"
                :color="r.color"

              >
                <v-icon left>
                  mdi-label
                </v-icon>
                {{r.valormax}}-{{r.valormin}}
              </v-chip>
            </template>
          </v-container>

          <v-card-actions>
            <v-btn
              outlined
              rounded
              text
            >
              Button
            </v-btn>
          </v-card-actions>
        </v-card>


        <v-card></v-card>


      </v-col>

    </v-row>

    <SvgPanZoom
      style="width: 100%; height: 800px; border:0px solid black; background-color:white;"

      :controlIconsEnabled="true"
      :fit="false"
      :center="true"
    >
      <svg
        version="1.1"
        id="Capa_1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        x="0px"
        y="0px"
        width="100%"
        height="100%"
        viewBox="0 0 1198 819"
        enable-background="new 0 0 1198 819"
        xml:space="preserve"

      >

    <g class="capa" id="dibujomapa" @click="handleStateClick"
       @mouseover="handleStateHover">

      <!-- quintana roo -->

       <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">


      <path
        id="QR"

        class="estado"
        data-name_estado="Quintana Roo"
        data-id_estado="23"

        d="M1168.658,498.584l1.519,4.777l-3.357,11.154l-15.423,20.41l-3.948,16.862l-0.011,8.716l-4.327,3.748
    l-2.85,0.23l-1.179,3.508l4.128,4.128l7.066-2.209l1.108,0.62l-1.01,2.879l-6.267,4.758l-2.209,4.888l1.499,2.229l6.038-3.538
    l0.358,1.438l-2.56,8.286l-8.456,32.325l-0.619,9.315l-0.062-0.011l0.212-9.176l-6.707-7.347l1.079-9.896l-2.14-3.668l-1.869,1.89
    l-1.52,3.688l-6.588,6.587l-8.846,6.638l-1.13,4.728l-9.194,17.552l-8.478-3.178l-3.737,3.318l-2.16-31.097l-1.698-47.388
    l48.856-37.443l10.275-16.432l-0.21-20.841l7.257-0.17l2.848-2.379l1.642-1.649l-1.84-1.659l4.188-1.608l5.417,2.809l6.367,7.807
    L1168.658,498.584z"
      >

      </path>

                  </template>
        <span>Tooltip</span>
      </v-tooltip>

      <!-- fin quintana roo -->

      <!-- Yucatán -->
      <path
        id="YUC"

        class="estado"
        data-name_estado="Yucatán"
        data-id_estado="31"
        :fill="this.color"
        d="M1142.75,491.067l0.21,20.38l-9.796,15.753l-48.637,37.271l-34.574-21.77l-4.288-1.159l-10.476-3.568
    l-3.769-12.563l0.72-3.378l2.688-4.888l19.871-10.896l4.067-0.649l37.973-9.976l0.14-0.04l8.146-6.007l36.843,1.509l0.03-0.749
    l0.01,0.749L1142.75,491.067z"
      >
        <title>Yucatán</title>
      </path>
      <!-- fin Yucatán -->

      <!-- Campeche -->
      <path
        id="CMP"
        class="estado"
        data-name_estado="Campeche"
        data-id_estado="4"
        :fill="this.color"
        d="M1088.096,649.903l-0.031,0.43l-0.608,0.53l-70.617,4.228l-1.479-5.527l-14.573-2.019l-9.336-1.6
    l-4.198,5.308l-7.217,0.602l-9.955-6.839l-1.689-7.167l-2.777-8.326l-8.646-0.209l-3.038-3.519l17.301-2.979l1.771,1.039
    l-2.249,4.697l5.729,1.898l1.628,3.269l13.755-2.519l9.665-7.417l0.84-2.828l-6.297-6.507l5.058-5.068l17.712-14.433l3.178-7.037
    v-12.884l8.728-9.815l-3.289-21.261l3.317-15.502l3.209,10.693l11.256,3.828l4.018,1.061l34.584,21.78l1.689,47.407l2.549,36.684
    L1088.096,649.903L1088.096,649.903z"
      >
        <title>Campeche</title>
      </path>
      <!-- fin Campeche -->

      <!-- Chiapas -->
      <path
        id="CHS"
        class="estado"
        data-name_estado="Chiapas"
        data-id_estado="5"
        :fill="this.color"
        d="M1041.146,716.021l0.601,12.925l-52.846,4.099l-18.842,35.703l6.316,8.936l-1.359,3.3l-0.93,11.795v6.637
    l-21.479-18.012l-4.567-6.087l-29.775-22.381l-15.622-13.233l-8.666-4.967l1.398-3.818l-3.719-8.727l2.319-10.686l4.768-6.957
    l1.948-10.365l8.146-9.234l1.539-2.159l0.01,0.01l0.63-0.89l0.3-0.42l7.946-11.294l4.838-14.004l10.235,3.668l-0.85,9.086
    l11.175,12.104l14.343-14.562l9.626-4.277l5.197-4.708h3.658l5.798,2.788l0.63,3.599l3.548,2.669l2.929,6.986h3.438l6.617,6.987
    l0.539,0.579l-1.119,1.568l15.263,13.244l14.022,8.216l3.709,7.837L1041.146,716.021z"
      >
        <title>Chiapas</title>
      </path>
      <!-- fin Chiapas -->

      <!-- Tabasco -->
      <path
        id="TAB"
        class="estado"
        data-name_estado="Tabasco"
        data-id_estado="27"
        :fill="this.color"
        d="M1015.529,655.99l0.629,22.24l-13.923,2.019l-7.768-8.206h-3.078l-2.698-6.447l-3.398-2.549l-0.67-3.778
    l-6.797-3.268h-4.577l-5.338,4.888l-9.775,4.349l-13.443,13.634l-9.646-10.455l0.89-9.576l-12.764-4.577l-5.197,15.162
    l-7.557,10.726l-1.439-2.158v-0.891l-6.967-9.226l-6.158-3.288l-4.815-4.028l0.609-4.118l-2.858-7.347l17.741-8.556l16.133-3.398
    l3.339,1.789l7.018-3.397l12.584-4.769l6.756-4.488l3.898,4.519l8.166,0.229h0.109l2.419,7.237l1.8,7.656l10.875,7.477l8.396-0.699
    l4.049-5.117l8.484,1.46l13.614,1.879L1015.529,655.99z"
      >
        <title>Tabasco</title>
      </path>
      <!-- fin Tabasco -->

      <!-- veracruz -->
      <path
        id="VER"
        class="estado"
        data-name_estado="Veracruz"
        data-id_estado="30"
        :fill="this.color"
        d="M907.479,678.45l2.021,3.009l-1.829,2.559l-6.717,7.566l-32.165,0.21l-14.434-1.669l-1.669-5.646
    l-7.236-4.898l0.42-5.768l-2.549-2.549l-19.751,8.465l-5.349-5.155l-0.97-3.688l3.06-8.307l-3.528-8.006l-12.056-2.629
    L791.653,636.3l-0.142-0.17l-7.775-2.499l-0.521,3.698l-2.608,2.949l-3.907-3.499l-2.521,1.01l-7.017,0.979l-0.812-4.019
    l-8.375-4.078v-4.128l5.407-1.119l-3.308-11.475l7.307-3.759l-1.35-2.368l-8.486-5.219l-5.428-8.046l4.998-5.208v-9.386
    l5.617-8.105l-1.999-2.289l-8.727-4.139l-7.735,4.089l-5.599-4.059v-6.367l6.087-1.05l1.891-5.108l-7.816-4.696l-0.42-3.148
    l-3.148-3.147l-4.059,1.89l-2.828,11.765l-2.07,1.209l0.69-4.678l-3.418-3.419l-3.958,4.208l-10.246,7.997l-0.939-1.09
    l-0.979-3.108l1.739-6.287l-1.449-4.558l3.147-3.139h7.656l2.85-11.896l-5.229-4.238l-3.548,1.109l-2.108-1.229l-3.539-7.916
    l-0.659-7.258l-2.828-3.447l4.458-6.787l-2.589-7.137l5.526-7.228l0.25-3.798l-6.098-6.479l6.617,0.352l4.026-2.549l15.765,4.558
    l4.498,17.142l5.917,6.019l-3.858-3.688l-1.239,0.75l3.738,12.524l6.167,6.826l1.669,2.089l8.847,21.37l20.271,28.146
    l13.613,18.603l9.516,21.188l12.265,14.703l6.576,5.458l24.569,1.311l8.726,5.537l6.237,1.538l8.865,13.194l8.984,3.458
    l10.625-5.207l2.67,6.856l-0.68,4.566l5.527,4.608l6.057,3.259l6.467,8.557v0.851H907.479z"
      >
        <title>Veracruz</title>
      </path>
      <!-- fin veracruz -->

      <!-- Oaxaca -->
      <path
        id="OAX"
        class="estado"
        data-name_estado="Oaxaca"
        data-id_estado="20"
        :fill="this.color"
        d="M899.652,693.083l-0.359,0.43l-1.959,10.445l-4.768,6.938l-2.47,11.442l3.658,8.626l-1.17,3.179
    l-12.443-3.867l-2.02,3.147l-7.207-0.399l-6.227-3.509l0.68-1.81l-5.737-2.349l-4.979,2.129l-18.001,18.002l-36.653,14.232
    l-7.966,1.26l-13.016-5.117l-7.586-3.379l-2.259-3.828l-27.418-0.891l-8.496-2.969l-10.335-6.467l-11.305-3.848l8.946-4.669
    l-0.74-2.988l1.38-5.117l6.337-3.068l2.52-16.021l-6.959-4.938l-2.077-3.947l-4.688-9.588l1.25-16.671l13.354-5.138l5.218,2.608
    l4.528-1.859l-0.7-6.087l1.389-6.146l1.569-0.399l5.067,10.136l4.367,1.799l7.497-6.396l8.855,0.43l10.186-7.236l2.409-7.467
    l3.309-3.738l0.329-2.379l5.679,1.829l13.252,15.873l11.815,2.579l2.979,6.747l-3.009,8.185l1.189,4.55l6.367,6.138l19.74-8.456
    l1.35,1.349l-0.439,5.947l7.518,5.088l1.799,6.067l15.453,1.789l0.05,0.01h0.04h0.01l20.223-0.14L899.652,693.083z"
      >
        <title>Oaxaca</title>
      </path>
      <!-- fin Oaxaca -->

      <!-- Puebla -->
      <path
        id="PUE"
        class="estado"
        data-name_estado="Puebla"
        data-id_estado="21"
        :fill="this.color"
        d="M779.799,641.577l-2.148,6.677l-9.355,6.647l-8.936-0.44l-7.258,6.188l-2.997-1.229l-5.35-10.705
    l-3.638,0.909l-1.649,7.297l0.601,5.208l-2.85,1.169l-5.196-2.599l-14.034,5.396l-4.628-3.367l-11.884-0.431l-11.086-10.035
    l-0.368-3.469l4.566-4.368l9.437-1.608l-1.619-7.626l1.959-3.278l-1.109-4.238l1.049-4.026l0.07,0.02l0.14-0.83l0.16-0.64
    l-0.05-0.021l0.109-0.669l0.42-18.932l4.498,1.04l7.217,8.694l6.217,4.568l6.146-4.328l3.959-0.63l13.063-5.667l-2.759-3.068
    l-7.097-2.919l-0.21-4.157l-3.38-3.39l-10.146-2.737l-1.608-9.246l4.567-7.848l-2.159-8.234l3.429-5.857l3.799-2.229l2.81-11.674
    l2.448-1.149l2.049,2.049l0.439,3.368l7.377,4.418l-1.149,3.139l-6.486,1.119v8.396l6.978,5.048l7.886-4.168l7.767,3.678
    l1.029,1.18l-5.217,7.526v9.256l-5.428,5.647l6.297,9.306l8.437,5.197l0.38,0.67l-7.007,3.607l3.198,11.104l-5.019,1.04v6.287
    l8.557,4.168l0.938,4.668l8.496-1.181l1.919-0.75L779.799,641.577z"
      >
        <title>Puebla</title>
      </path>
      <!-- fin Puebla -->

      <!-- Tamaulipas -->
      <path
        id="TMS"
        class="estado"
        data-name_estado="Tamaulipas"
        data-id_estado="28"
        :fill="this.color"
        d="M753.57,325.694l-6.366,22.27l-6.258,12.304l-3.27,15.015l2.699-14.443l5.218-11.104l-3.599-2.619
    l-1.851,3.678l-4.378-1.459l-4.366,4.368l1.619,3.938l-1.561,7.357l3.988,3.568l-2.619,4.438l0.43,8.246l-3.088,5.288l0.609,2.107
    l3.479,2.051l-1.839,8.806l-0.229,25.798l1.3,21.87v9.165l-5.038,10.945l2.559,9.835l-15.553-4.508l-4.197,2.658l-7.707-0.411
    l-0.09-0.089l-12.124,2.648l-13.674-5.257l-5.229-7.848l-4.717-1.238l-4.699,2.987l-16.83-7.916l4.397-6.406v-3.56l-6.627-7.267
    l2.099-6.877h5.397v-10.274l2.289-3.249l6.228-1.068l7.478-7.946l-4.698-9.187l0.659-12.725l-3.918-3.708l2.148-3.229l11.686-6.587
    l5.598-1.158l1.948-12.374l2.969-0.7l3.879,1.599l13.373-11.144l4.288-6.837l-4.896-9.116l-0.221-13.574l-3.118-3.128l-7.916,2.199
    l-6.566-4.238l-3.419-0.6l-2.988-7.688l-6.167-3.188l-0.66-9.825l-6.967-2.619l-0.858-6.207l-5.157-3.009l-0.21-10.035l-0.69-9.136
    l-5.287-2.209l-0.898-3.398l5.507-7.087l5.538,2.109l2.519,4.058l-1.51,5.837l4.149,7.867l-0.432,5.217l8.977,16.183l5.138,12.284
    l11.045,2.431l6.308,5.228l11.534,1.959l8.268,5.657l18.931,1.52l8.666,4.667l7.478-3.838L753.57,325.694z"
      >
        <title>Tamaulipas</title>
      </path>
      <!-- fin Tamaulipas -->

      <!-- Tlaxcala -->
      <path
        id="TLX"
        class="estado"
        data-name_estado="Tlaxcala"
        data-id_estado="29"
        :fill="this.color"
        d="M741.606,604.444l1.14,1.26l-10.886,4.758l-4.197,0.659l-5.567,3.919l-5.128-3.759l-7.485-9.017
    l-5.607-1.289l-0.76-1.06l0.55-4.948l9.936-0.64l1.539-2.188l5.817-0.8l10.075,2.729l2.688,2.688l0.23,4.528L741.606,604.444z"
      >
        <title>Tlaxcala</title>
      </path>
      <!-- fin Tlaxcala -->

      <!-- Guerrero -->
      <path
        id="GRO"
        class="estado"
        data-name_estado="Guerrero"
        data-id_estado="13"
        :fill="this.color"
        d="M728.433,703.299l-2.249,14.333l-6.246,3.028l-1.659,6.157l0.55,2.219l-8.996,4.688l-10.245-8.956h-7.996
    l-32.485-8.386l-9.154-8.286l-9.466-1.1l-35.193-13.594l-23.08-16.844l-10.735-10.953l-6.087-1.399l-2.099,0.839l2.139-8.396
    l10.655-4.448l-1.769-7.916l4.026-2.749l11.795,4.718l13.403-3.468l7.047,3.738l2.079-1.15l10.485,1.67l-4.647-14.634l0.771-3.668
    l2.559,2.027l3.778-2.657l1.528,0.76l7.438,17.282l4.008,0.54l9.596-8.509h6.718l6.217-5.365l6.048,1.368l4.268,6.827l4.738,2.998
    l3.818-3.369l1.959,0.491l4.947,6.786l0.619,0.86l0.449,4.208l11.915,10.785l11.974,0.43l4.248,3.099l-1.278,17.143l4.869,9.966
    l2.258,4.288L728.433,703.299z"
      >
        <title>Guerrero</title>
      </path>
      <!-- fin Guerrero -->

      <!-- Hidalgo -->
      <path
        id="HGO"
        class="estado"
        data-name_estado="Hidalgo"
        data-id_estado="14"
        :fill="this.color"
        d="M725.414,552.658l-0.79,5.338l-3.769,6.437l2.158,8.236l-4.538,7.776l1.66,9.496l-5.848,0.8l-1.51,2.139
    l-8.977,0.58l0.17-2.369l-2.889-6.247h-7.736l-2.839-0.898v-6.167l-3.238-1.891l-9.546,2.329l-2.987,6.577l-19.291-16.843
    l0.988-4.328l0.012-5.807l7.775-4.408l1.778-2.279v-5.797l8.387-8.186l1.68-7.519l10.256-1.329l-0.96-4.606l4.867,2.009
    l3.849,3.389l8.546-1.18l3.599-7.377l3.129,6.997l3.1,1.81l3.408-1.07l3.867,3.14l-2.349,9.825h-7.097l-4.229,4.219l1.589,5.008
    l-1.737,6.287l1.199,3.828l2.078,2.389l11.414-8.896l3.029-3.199L725.414,552.658z"
      >
        <title>Hidalgo</title>
      </path>
      <!-- fin Hidalgo -->

      <!-- San luis potosí -->
      <path
        id="SLP"
        class="estado"
        data-name_estado="San Luis Potosi"
        data-id_estado="24"
        :fill="this.color"
        d="M702.954,476.414l6.646,7.047l-0.181,2.698l-5.747,7.517l2.608,7.197l-4.647,7.086l3.238,3.948l0.609,6.717
    l-3.857,7.917l-7.066,0.969l-3.429-3.019l-6.217-2.608l-2.919-7.307l-5.397-5.957l-9.086,7.546l-8.267-3.488l-4.147,3.709
    l-24.509-8.677l-7.786,6.718l-4.248-1.739l-10.745-8.775h-5.646l-5.178-4.1l-7.986-0.759l5.198-6.728l-0.222-7.996l2.199-10.984
    l-2.438-5.848l-6.407-0.489l-7.407,6.308h-1.349l-16.952-17.572l-0.64-8.136l-2.479-4.938l4.148-6.117l2.907-0.62l15.363-11.854
    l16.922-15.182l5.737-8.577l10.636-14.313l9.925,15.593l-0.438,11.965l5.428,7.166l-0.441,20.552l3.949,2.619l5.407-2.479
    l4.718,0.4l6.327,6.937v2.52l-5.127,7.477l19.171,9.016l4.848-3.088l3.528,0.939l5.179,7.767l14.532,5.587L702.954,476.414z"
      >
        <title>San Luis Potosi</title>
      </path>
      <!-- fin San luis potosí -->

      <!-- Nuevo León -->
      <path
        id="NL"
        class="estado"
        data-name_estado="Nuevo León"
        data-id_estado="19"
        :fill="this.color"
        d="M698.996,336.709l4.658,8.686l-3.619,5.817l-12.584,10.477l-3.488-1.431l-4.408,1.039l-1.947,12.345
    l-4.698,0.979l-12.306,6.896l-3.059,4.578l4.328,4.1l-0.64,12.442l4.407,8.606l-6.417,6.807l-6.347,1.09l-2.919,4.148v9.245h-5.008
    l-2.369,7.767l-4.808-0.398l-5.009,2.288l-2.559-1.709l0.43-20.24l-5.417-7.157l0.431-11.894l-10.605-16.674l1.47-10.715
    l2.089-5.578l-3.089-3.088l0.7-3.329l12.444-4.718l2.527-4.288l-3.688-6.457l-11.444-11.482l-1.52-9.938l-6.638-8.186l-3.479-2.221
    l-3.328-6.467l13.084-12.064l3.088,1.539l6.139-6.847l2.309-8.336l-3.049-4.068h-4.067l-2.438-4.128l0.93-3.519l11.915-6.716
    l2.828-9.606l5.646-4.268l6.737,5.208l7.836-6.147l1.648,2.548l-5.969,7.687l1.262,4.838l5.128,2.139l0.618,8.176l0.221,10.835
    l5.258,3.069l0.88,6.366l6.906,2.599l0.649,9.696l6.417,3.318l3.089,7.946l3.959,0.688l6.865,4.438l7.728-2.141l2.068,2.079
    L698.996,336.709z"
      >
        <title>Nuevo León</title>
      </path>
      <!-- fin Nuevo León -->

      <!-- Estado de México -->
      <path
        id="MEX"
        class="estado"
        data-name_estado="Estado de México"
        data-id_estado="11"
        :fill="this.color"
        d="M701.564,600.316l1.109,1.56l-0.431,19.431l-0.069,0.399l-7.707-2.509l-3.348-2.76l-1.479-12.283
    l-3.019-6.127l-7.776-3.509l-3.777,14.844l2.487,3.938l-3.518,4.357l0.21,5.867l-6.917,9.166l-6.627-1.499l-6.367,5.496h-6.727
    l-9.508,8.427l-2.487-0.34l-7.316-17.003l-1.679-0.84l12.744-20.271l3.838-4.737l0.869-14.783l2.39-3.328l-2.379-2.809l6.037-7.707
    l0.398-2.988l3.919-1.238l20.829,18.171l3.529-7.736l8.246-2.019l1.969,1.148v6.417l3.998,1.249l7.127,0.04l2.318,5.019
    l-0.21,2.818L701.564,600.316z"
      >
        <title>Estado de México</title>
      </path>
      <!-- fin Estado de México -->

      <!-- Morelos -->
      <path
        id="MOR"
        class="estado"
        data-name_estado="Morelos"
        data-id_estado="17"
        :fill="this.color"
        d="M701.875,623.176l-1.17,4.498l1.05,4.008l-1.938,3.238l1.42,6.678l-8.356,1.43l-4.538,4.338l-5.507-7.546
    l-3.249-0.82l-3.568,3.147l-3.498-2.219l-3.979-6.355l7.227-9.565l-0.21-5.838l3.108-3.848l5.918,3.258h5.566l3.589,2.949
    L701.875,623.176z"
      >
        <title>Morelos</title>
      </path>
      <!-- fin Morelos -->

      <!-- distrito federal -->
      <path
        id="CMX"
        class="estado"
        data-name_estado="Ciudad De México"
        data-id_estado="9"
        :fill="this.color"
        d="M688.161,604.465l1.409,11.614h-4.607l-5.947-3.288l-2.328-3.688l3.166-12.485l5.669,2.559L688.161,604.465
    z"
      >
        <title>Ciudad De México</title>
      </path>
      <!-- fin distrito federal -->

      <!-- queretaro -->
      <path
        id="QRO"
        class="estado"
        data-name_estado="Querétaro"
        data-id_estado="22"
        :fill="this.color"
        d="M683.613,522.673l0.908,4.349l-9.694,1.26l-1.81,8.104l-8.517,8.316v5.917l-1.279,1.63l-8.275,4.697v6.428
    l-0.971,4.268l-4.816,1.529l-0.47,3.528l-5.607,7.155l-7.127-8.115l-7.326-18.111l-3.479-4.548l5.188-9.006l11.885-1.299
    l5.009-6.628l1.559-2.709l7.807-1.09l2.55-4.338l-2.97-6.577l3.358-3.008l8.227,3.468l8.695-7.207l4.198,4.578L683.613,522.673z"
      >
        <title>Querétaro</title>
      </path>
      <!-- fin queretaro -->

      <!-- Guanajuato -->
      <path
        id="GTO"
        class="estado"
        data-name_estado="Guanajuato"
        data-id_estado="12"
        :fill="this.color"
        d="M654.717,517.845l2.738,6.077l-1.789,3.049l-7.807,1.079l-1.869,3.278l-4.567,6.027l-11.994,1.31
    l-6.088,10.535l3.938,5.088l7.195,17.812l-3.237,6.277l-4.078,3.298l-6.146-2.528l-6.116,2.108l-3.79-3.788l-6.985-3.309
    l-8.646,2.589l-2.277-1.229l-2.59-8.186l-4.798-3.528l-5.066,4.367l-6.327,1.02l-3.508-1.288l-0.41-3.56l-4.468-3.239l0.14-0.209
    l3.357-5.138l-3.469-11.064l9.046-13.894l5.947-4.038l4.758-4.498l-1.76-6.827l2.56-3.618l-0.649-8.876l1.959-2.487l8.477,0.81
    l5.237,4.147h5.638l10.425,8.507l5.389,2.238l7.826-6.736L654.717,517.845z"
      >
        <title>Guanajuato</title>
      </path>
      <!-- fin Guanajuato -->

      <!-- Coahuila -->
      <path
        id="COA"
        class="estado"
        data-name_estado="Coahuila"
        data-id_estado="7"
        :fill="this.color"
        d="M642.133,233.357l9.105,14.473l-7.037,5.518l-6.717-5.198l-6.946,5.267l-2.81,9.486l-11.935,6.737
    l-1.25,4.728l3.188,5.407h4.179l2.159,2.879l-2.021,7.286l-5.138,5.738l-2.988-1.499l-14.692,13.542l4.038,7.857l3.549,2.199
    l6.297,7.774l1.529,10.026l11.604,11.604l3.198,5.608l-1.81,3.078l-12.725,4.828l-1.029,4.918l2.968,2.986l-1.777,4.748
    l-1.479,10.677l-3.219,0.51l-10.772-9.696l-7.277-0.67l-8.127,0.21l-0.979-2.758l-14.663-10.216l-17.092-2.438l-8.695,3.658
    l-0.399,0.17l0.14,0.37l-6.048,12.474l-14.743-7.467v-4.178l-7.836-8.276l-0.818-8.876l5.188-11.902l-0.21-12.636l3.329-11.784
    l-14.444-17.282l-2.147-11.315l-7.536-39.651l25.288-46.069l5.587-0.649l10.825-15.243l4.776-12.524l6.147-4.099l5.268-0.43
    l4.658-4.238l15.232,4.009l12.925,0.459l16.682,13.684l13.993,15.273l13.804,30.406l1.601,5.018L642.133,233.357z"
      >
        <title>Coahuila</title>
      </path>
      <!-- fin Coahuila -->

      <!-- Michoacan -->
      <path
        id="MCH"
        class="estado"
        data-name_estado="Michoacán"
        data-id_estado="16"
        :fill="this.color"
        d="M642.542,581.505l2.021,2.379l-1.959,2.739l-0.87,14.732l-3.589,4.438l-13.153,20.92l-3.118,2.199
    l-1.439-1.119l-1.09-1.09l-1.259,0.38l-1.13,5.396l4.038,12.704l-8.605-1.369l-1.818,1.011l-6.848-3.629l-13.482,3.479
    l-12.085-4.828l-5.519,3.77l1.709,7.687l-10.185,4.248l-2.589,10.165l-3.061,1.08l-49.457-17.632l-11.005-13.504l6.697-9.746
    l3.188-1.119l0.012,0.03l0.897-0.351l0.562-0.189l-0.01-0.021l2.299-0.88l4.758-3.889l1.849,1.31l6.928,0.95l5.316-7.537
    l13.164-3.729l2.169-7.477l-1.929-2.739l-4.458-0.42l-3.6-8.195l3.05-7.188l-1.439-2.857l-7.007-0.46l-3.198-1.499l-0.33-2.351
    l2.43-3.558h7.217l5.316-3.759l8.786-3.22l14.163-4.646l4.199,3.049l0.449,3.818l4.736,1.749l7.139-1.159l4.477-3.858l3.449,2.528
    l2.619,8.297l3.356,1.818l8.706-2.608l6.128,2.858l4.357,4.357l6.467-2.229l6.447,2.659l5.018-4.06l3.039-5.887L642.542,581.505z"
      >
        <title>Michoacán</title>
      </path>
      <!-- fin Michoacan -->

      <!-- Zacatecas -->
      <path
        id="ZAC"
        class="estado"
        data-name_estado="Zacatecas"
        data-id_estado="32"
        :fill="this.color"
        d="M612.566,385.716l-10.205,13.744l-5.588,8.386l-16.812,15.083l-15.053,11.604l-3.168,0.68l-4.97,7.347
    l2.739,5.458l0.659,8.376l17.762,18.422h2.55l7.348-6.268l4.878,0.38l1.909,4.567l-2.15,10.705l0.21,7.637l-5.377,6.967
    l-14.254-6.787l-0.639,0.801l-4.76-6.298l-1.339-4.207l-11.104-9.036l-5.578,5.566l-6.518,2.479l-0.778,3.647l1.929,5.168
    l-0.85,2.56l-3.248,0.399l-4.849,4.617l3.647,12.095l3.539,3.958l-0.94,4.148l-6.347,5.327l-9.274,0.68l-0.859,8.196h-2.259
    l-21.472-6.317l0.4-10.404l6.137-2.108l2.159-5.758l-1.05-4.378l16.882-17.973l-0.499-4.308l-8.267-7.776l-3.488,5.967
    l-7.806,9.865l-1.659-0.959l0.429-17.262l-3.198-2.879l-5.138,11.983l-1.159-1.398l2.629-14.224l-5.518-3.858l-3.288,8.326
    l2.409,5.418l-12.176,4.498l0.101-0.65l0.21-1.459l0.021-0.17l4.027-28.637l1.869-2.898l3.509-11.515l8.966-9.405l0.859-17.713
    l20.151-15.063l29.904-1.979l1.181-9.695l-5.679-15.763l7.397-3.118l16.322,2.339l13.973,9.735l1.19,3.318l9.126-0.229l6.695,0.62
    l10.936,9.845L612.566,385.716z"
      >
        <title>Zacatecas</title>
      </path>
      <!-- fin Zacatecas -->

      <!-- Jalisco -->
      <path
        id="JAL"
        class="estado"
        data-name_estado="Jalisco"
        data-id_estado="15"
        :fill="this.color"
        d="M586.349,500.013l-1.93,2.459l0.66,8.927l-2.649,3.737l1.71,6.636l-3.979,3.779l-6.147,4.168l-9.596,14.743
    l3.459,11.065l-3.349,5.128l-14.313,4.707l-8.896,3.249l-5.188,3.638h-7.525l-3.209,4.688l0.528,3.729l4.189,1.969l6.437,0.42
    l0.739,1.469l-3.028,7.147l4.208,9.595l4.648,0.431l1.119,1.6l-1.739,5.977l-12.874,3.649l-5.098,7.226l-5.657-0.778l-2.489-1.76
    l-5.338,4.419l-1.779,0.688l-1.447-17.502l-6.237-6.477l-6.967,4.058l-5.418-1.409l-4.688-3.527l-10.016,8.245h-4.168l-6.349,6.559
    l-12.584-6.188l-21.52-29.706l-4.727-13.323l-1.302-4.089l6.429-2.339l7.944-2.269l2.289-5.508l4.64-9.695l13.282-4.778
    l7.456,4.148l11.745,8.984l0.84-1.688l2.39-17.053l1.858-0.369l8.526-8.057l-8.087-8.088l1.729-10.374l-5.798-6.917l-2.879-6.156
    l2.639-8.916l14.494-5.349l-2.799-6.307l2.359-5.978l3.168,2.209l-2.578,13.974l3.168,3.818l5.277-12.314l1.14,1.02l-0.44,17.452
    l3.55,2.079l8.646-10.936l2.628-4.468l6.487,6.106l0.358,3.068l-16.95,18.052l1.118,4.718l-1.749,4.668l-6.437,2.22l-0.48,12.594
    l22.689,6.678l3.928,0.029l0.87-8.296l8.506-0.62l7.107-5.957l1.229-5.407l-3.838-4.278l-3.289-10.895l3.828-3.639l2.459-0.301
    l1.062,11.005l6.797,2.101l8.476,2.299l12.714-14.414l0.03,0.04l0.6-0.749l0.379-0.439l-0.01-0.021l0.131-0.17L586.349,500.013z"
      >
        <title>Jalisco</title>
      </path>
      <!-- fin Jalisco -->

      <!-- Aguascalientes -->
      <path
        id="AGS"
        class="estado"
        data-name_estado="Aguascalientes"
        data-id_estado="1"
        :fill="this.color"
        d="M566.258,487.099l5.167,6.897l-12.304,13.943l-7.557-2.05l-5.817-1.8l-1.02-10.615l1.118-3.367
    l-1.969-5.247l0.521-2.419l6.065-2.311l4.838-4.837l9.716,7.896L566.258,487.099z"
      >
        <title>Aguascalientes</title>
      </path>
      <!-- fin Aguascalientes -->


      <!-- Chihuahua -->
      <path
        id="CHI"
        class="estado"
        data-name_estado="Chihuahua"
        data-id_estado="6"
        :fill="this.color"
        d="M521.079,195.734l-25.409,46.289l9.606,50.597l-19.103-3.789l-13.794,17.662l-5.307-2.749l-16.595-4.658
    l-7.466,1.7l-13.294-8.936l-3.018,1.289l-10.506-7.876l-4.327,3.058l-4.548,12.984l-4.34,2.689l-2.979,2.959l0.86,9.265
    l-3.369,2.521l-1.529,7.877L389.57,333l-13.324,2.26l-10.975-21.74l-6.587-1.368l-8.846-3.498l-1.699-14.903l-4.768-7.796
    l-0.439-5.678l-2.629-3.588l-9.396-4.128l-6.507,3.148l-5.097-6.277l-0.22-15.553l-2.709-4.748l-7.767-12.733l-4.817-13.594
    l4.138-4.518l13.433,4.548l2.739-2.749l-1.759-19.611l-0.86-26.827l3.649-4.079l2.419-27.796l0.01-0.101l-3.918-22.359l-1.33-22.38
    l-3.249-1.419l2.189-6.197l23.18,0.879l-0.39-4.877l0.41-12.924l60.542,1.269l9.595,10.875l8.438,7.786l13.684,13.904l9.406,8.956
    l15.213,11.145l4.048,12.144l4.308,6.297l0.65,13.004l8.686,13.793l6.388,3.089l8.346,7.467l6.317,0.659l7.985,6.258l4.81,1.089
    L521.079,195.734z"
      >
        <title>Chihuahua</title>
      </path>
      <!-- fin Chihuahua -->

      <!-- Colima -->
      <path
        id="COL"
        class="estado"
        data-name_estado="Colima"
        data-id_estado="8"
        :fill="this.color"
        d="M506.366,605.874l1.438,17.382l-4.018,1.399l-6.717,9.774l-4.229-5.378l-21.87-12.894l-5.587-2.799
    l5.577-5.758h4.068l9.516-7.837l3.988,2.999l6.297,1.64l6.487-3.778L506.366,605.874z"
      >
        <title>Colima</title>
      </path>
      <!-- fin Colima -->

      <!-- Nayarit -->
      <path
        id="NAY"
        class="estado"
        data-name_estado="Nayarit"
        data-id_estado="18"
        :fill="this.color"
        d="M489.094,520.703l-7.097,6.697l-2.479,0.488l-2.438,17.702l-10.325-7.905l-8.196-4.559l-14.492,5.207
    l-4.537,9.477l-7.099-4.719l-2.389-0.729l1.5-3.158l7.416-6.117l2.459-7.355l1.609-10.977l-9.086-7.097l-7.866-18.481l0.568-2.809
    l4.538,4.139l2.458-2.459l-6.275-9.406l0.6-8.186l4.02-1.68l1.3-3.908l-3.789-6.316l4.628-4.838l-0.66-4.588l1.65-1.979
    l13.453,3.519l5.598,5.388l-1.811,5.667l-1.488,5.179l2.777,1.229l4.868-1.1l4.878,0.938v1.859l6.866,6.867l4.218-1.779
    l3.391,2.129l-0.36,2.509l-0.53,1.799l-2.357,7.968l3.159,6.767l5.525,6.627l-1.739,10.455L489.094,520.703z"
      >
        <title>Nayarit</title>
      </path>
      <!-- fin Nayarit -->

      <!-- Sinaloa -->
      <path
        id="SIN"
        class="estado"
        data-name_estado="Sinaloa"
        data-id_estado="25"
        :fill="this.color"
        d="M423.494,434.913l10.354,11.415l-1.969,2.349l0.65,4.528l-4.918,5.138l4.026,6.706l-0.868,2.609l-3.6,1.509
    l-4.677-0.979l-6.768-10.155l-4.079-3.897l1.079-2.568l-24.369-25.688l-11.654-18.342l-4.238-7.586l-11.045-5.418l-6.387-12.766
    h-7.087l-7.416-7.825l-0.62-5.607l-3.038-5.957v-3.488l-10.716-6.917l-7.516-5.576l-7.357-7.128l-4.098-4.356l-2.739,3.888
    l-13.083-7.275l-1.57-0.37v-3.27l-3.838-7.686l2.459-6.947l5.757-7.097l-0.42-3.129l17.642-12.534l13.244-13.223l6.297-3.059
    l8.396,3.688l2.139,2.929l0.43,5.597l4.778,7.827l1.769,15.473l9.745,3.85l6.068,1.269l10.784,21.352l-3.248,15.562l5.327,16.853
    l11.485,11.274l3.279,11.575l5.417,3.448l6.647-4.078l11.515,10.285l1.489,12.732l5.438,11.405L423.494,434.913z"
      >
        <title>Sinaloa</title>
      </path>
      <!-- fin Sinaloa -->

      <!-- sonora -->
      <path
        id="SON"
        class="estado"
        data-name_estado="Sonora"
        data-id_estado="26"
        :fill="this.color"
        d="M322.161,119.48l3.879,22.249l-2.359,27.208l-3.709,4.158l0.87,27.467l1.709,18.951l-1.599,1.6
    l-13.464-4.558l-5.407,5.897l5.137,14.523l7.866,12.914l2.509,4.398l0.22,15.683l5.378,6.627l-12.714,12.704l-16.893,12.014
    l-0.769-8.256l-7.177-9.026l-5.877,1.59l-6.146-2.379l-3.448-12.515l-8.497-5.137l-5.827-1.969l-7.097-7.507l-2.538-13.543
    l1.609-9.656l-10.066-2.639l-2.219,1.23l-0.829,0.789l-5.288-3.318l-6.567-6.367l-5.647-12.174l-12.854-10.885l-3.928-4.338v-5.168
    l-8.496-11.315l-1.1-9.695l-5.147-3.429l0.209-4.987l-12.164-22.82l-0.429-10.235l-3.969-10.255l-5.767-12.814l1.919-12.144
    l0.01-5.718l-7.207-5.108l-4.677-0.429l-12.055-13.334l-5.677-2.849l-6.227,3.439l-11.985-8.626l-7.876-4.048l-1.05-2.529
    l-9.265-7.537l-1-4.778l2.939-11.114l5.957-5.358l6.517,3.249l128.65,57.923l0.13,0.06l77.024,3.648l-1.699,4.808l-0.799,2.279
    l3.688,1.609L322.161,119.48z"
      >
        <title>Sonora</title>
      </path>
      <!-- fin sonora -->

      <!-- Baja California Sur -->
      <path
        id="BCS"
        class="estado"
        data-name_estado="Baja California Sur"
        data-id_estado="3"
        :fill="this.color"
        d="M269.706,414.703l8.956,11.354l-3.469,10.216l-8.906,5.928l-4.727,4.498l-2.41,0.51l-5.867-6.268
    l-4.997-21.521l-7.127-6.228l-7.397-4.589l-21.42-21.641l-16.492-16.042h-1.859l-1.19-5.917l-2.868,1.909l-3.429-5.837
    l-2.959-1.062l-3.498-9.895l4.778-28.657l-9.305-23.029l-5.818-2.689l-30.666-26.058l-3.548,1.649l-5.118,0.2l-7.706-9.855
    l-4.848-1.55l-5.737-5.087l-10.346-5.418l-2.068-4.128L83.852,225.44l0.51-0.279l11.394,2.788l9.046-2.518l3.978,4.807l4.958,1.13
    l6.977,2.888l1.499-4.497l-2.249-1.96l-4.518-1.079l-4.538-4.918l3.758-3.398l32.286,2.029l18.331,1.159v1.9l3.328,12.734
    l9.556,10.215l2.609,8.476l7.626,7.387l2.269,0.949v5.957l2.639,5.718l1.769,7.946l3.838,3.848l1.28-0.53v-6.296l-1.649-4.479
    l0.379-0.609l7.167,7.376l0.44,5.638l2.469,2.478l-1.03,3.099l3.758,7.966l0.83,7.467l-2.668,5.337l7.186,15.043l5.538,3.839
    l1.469,9.655l7.206,14.034l2.529,6.757l-2.389,12.983l2.739,9.114l11.125,7.417l3.258-2.979l0.38-4.617l3.009,0.789l9.086,11.904
    l3.928,1.448l1.439,7.396L269.706,414.703z"
      >
        <title>Baja California Sur</title>
      </path>
      <!-- fin Baja California Sur -->

      <!-- Baja California -->
      <path

        @click="cambiaColor"
        id="BC"
        class="estado"
        active-class="active"
        data-name_estado="Baja California"
        data-id_estado="2"
        :fill="this.color"
        d="M165.284,218.434v1.649l-49.957-3.148l0.9-3.958l1.289-7.697l3.829-8.136l-10.926-14.494l-7.816-9.125
    l-16.932-19.301l-7.216-5.488l-13.644-12.364v-4.018l-3.029-4.338l0.22-14.393l-7.187-7.187l-1.299-18.262l-6.287-5.207
    l-0.65-10.276l-6.367-10.524l-2.528-4.858l-0.4-4.848l3.328-6.667l-2.889-5.527l-4.477-2.549l-2.729-10.115l-5.788-10.326
    l1.08-4.098l-0.11-0.22l84.7,2.319l-3.768,7.727l-6.567,5.907l-3.138,11.884l1.179,5.638l9.386,7.646l0.26,0.62l-3.709-0.65
    l-5.157,27.767l1.11,6.417l2.608,4.868l2.389,34.924l5.927,11.204l5.528,5.358l14.923,16.433l8.996,15.422l0.689,5.088l7.877,2.619
    l4.748,16.832l8.436,5.187l1.669,8.567L165.284,218.434z"
      >
        <title>Baja California</title>
      </path>
      <!-- fin Baja California -->
      <!-- durango -->
      <path
        id="DGO"
        class="estado"
        data-name_estado="Durango"
        data-id_estado="10"
        :fill="this.color"
        d="M543.218,365.136l5.198,14.435l-0.99,8.096l-29.104,1.929l-21.08,15.753l-0.87,17.862l-8.826,9.256
    l-3.488,11.564l-1.987,3.088l-3.979,28.297l-3.479-2.188l-4.02,1.699l-5.707-5.718v-2.479l-6.405-1.229l-4.68,1.06l-1.139-0.5
    l1.119-3.907l2.099-6.526l-6.557-6.308l-14.073-3.688l-10.315-11.364l-1.06-9.306l-5.437-11.415l-1.541-13.174l-12.773-11.404
    l-6.807,4.168l-4.14-2.639l-3.228-11.415l-11.505-11.285l-5.098-16.122l3.109-14.933l13.834-2.339l7.056-7.059l1.511-7.756
    l3.577-2.679l-0.868-9.396l2.289-2.289l4.706-2.919l4.568-13.034l3.038-2.159l10.326,7.746l3.066-1.309l13.164,8.846l7.718-1.77
    l16.013,4.489l6.347,3.289l13.984-17.922l19.031,3.769l13.893,16.632l-3.178,11.226l0.22,12.533l-5.218,11.954l0.91,9.776
    l7.774,8.226v4.498l16.934,8.576L543.218,365.136z"
      >
        <title>Durango</title>
      </path>

      <!-- fin durango -->
    </g>

  </svg>
    </SvgPanZoom>


    <!-- <Modal ref="modal" headModal='texto desde props' contentModal='SADSDASDASDASD props'></Modal> -->
    <ModalFullscreen ref="modal" headModal='texto desde props' :busqueda="search"
                     contentModal='SADSDASDASDASD props'></ModalFullscreen>


  </v-container>


</template>


<script>
  import {getAPI} from "../Api/axios-base";
  import Vue from "vue";
  import VueHorizontalList from "vue-horizontal-list";


  import Modal from "./Modal";
  import ModalFullscreen from "./ModalFulscreen"
  import SvgPanZoom from 'vue-svg-pan-zoom';

  export default {


    name: "MapaComponent",
    components: {
      Modal,
      ModalFullscreen,
      SvgPanZoom,
      VueHorizontalList

    },
    data: () => {
      return {
        options: {
          responsive: [
            {end: 576, size: 1},
            {start: 576, end: 768, size: 2},
            {start: 768, end: 992, size: 3},
            {size: 4},
          ],
          list: {
            // 1200 because @media (min-width: 1200px) and therefore I want to switch to windowed mode
            windowed: 1200,

            // Because: #app {padding: 80px 24px;}
            padding: 10,
          },
          position: {
            start: 2,
          },
          autoplay: {play: true, repeat: true, speed: 2500},
        },
        recomendados: [
          {
            title: "Sed non ante non cras amet",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas non sagittis leo. Vestibulum sit amet metus nec neque dignissim dapibus.",
            image: "https://picsum.photos/id/1015/600/600",
          },
          {
            title: "Curabitur sit amet nunc",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec id mollis erat. Aliquam erat volutpat. Nunc erat lacus, rhoncus nec.",
            image: "https://picsum.photos/id/1019/600/600",
          },
          {
            title: "Proin pharetra, ante metus",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi ac diam ac ex efficitur posuere. Pellentesque cursus pellentesque risus, non.",
            image: "https://picsum.photos/id/1039/600/600",
          },
          {
            title: "Cras pharetra non enim a",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi malesuada varius nibh, a malesuada nisi feugiat eget. Aenean convallis semper.",
            image: "https://picsum.photos/id/1042/600/600",
          },
          {
            title: "Proin vulputate, augue eu accumsan",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas fringilla tempor libero sit amet mollis. Praesent quis leo erat. Integer.",
            image: "https://picsum.photos/id/1044/600/600",
          },
          {
            title: "Maecenas feugiat magna sapien in",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sit amet fringilla ante. Quisque at ipsum non lacus consequat dictum.",
            image: "https://picsum.photos/id/1057/600/600",
          },
          {
            title: "Donec commodo sed enim at",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eu condimentum risus. Praesent dignissim, neque nec pharetra vestibulum, libero odio.",
            image: "https://picsum.photos/id/1063/600/600",
          },
          {
            title: "In bibendum urna et turpis",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vitae ante volutpat leo vulputate volutpat et sed ex. Vivamus eu.",
            image: "https://picsum.photos/id/1076/600/600",
          },
          {
            title: "Phasellus iaculis dignissim erat at",
            content:
              "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla mattis quam scelerisque, eleifend purus gravida, scelerisque orci. Ut et turpis.",
            image: "https://picsum.photos/id/1083/600/600",
          },
        ],

        rangos: [],

        rango: {
          valormax: 0,
          valormin: 0,
          color: []
        },
        search: "",
        items: [],
        color: "black",
        with: 2,
        radius: 10,
        padding: 8,
        lineCap: "round",
        date2: new Date().toISOString().substr(0, 19),
        servicios: [],


        user: {},

        cantRecursos: {'DGO': 95, 'BC': 50, 'BCS': 20},
        cantDurango: 95,
        cantBC: 50,
        cantBCS: 20,


        totales: [],

        loading: false


      };
    },
    methods: {

      GetPrediccion: function () {
        var self= this
        getAPI.get("/Recursos/api/Articulos/recommend/").then((res) => {
          self.recomendados = res.data.recursos_list



          for(var obj in self.recomendados){
            self.recomendados[obj].recurso_img=self.recomendados[obj].recurso_img[0].archivo

          }

        })
      },
      GetDetalle: function () {
        self = this
        self.rangos = []
        getAPI.get("/Recursos/api/Articulos/", {
          "params": {
            "search": self.search
          }
        }).then((res) => {
          self.items = res.data.recursos
          self.totales = res.data.conteo


          self.obtenNumeroMayor(self.totales).then(e => {
            //e.value es el estado con mas datos
            const maximo = e.value
            var c = document.getElementById("dibujomapa").children;
            for (var i = 0; i < c.length; i++) {


              let color5 = "#ff0027";

              var id = c[i].id
              if (self.totales[id]) {


                var porcentaje = (((self.totales[id].conteo / maximo)))
                var rango = {
                  valormax: 0,
                  valormin: 0,
                  color: []
                }
                if (porcentaje == 1) {
                  porcentaje = -.5;
                  rango.valormax = maximo * 1
                  rango.valormin = maximo * 1

                } else if (porcentaje >= .75) {
                  porcentaje = -.25;
                  rango.valormax = maximo * 1
                  rango.valormin = maximo * .75
                } else if (porcentaje >= .5) {
                  porcentaje = 0;
                  rango.valormax = maximo * .75
                  rango.valormin = maximo * .5
                } else if (porcentaje >= .25) {
                  rango.valormax = maximo * .5
                  rango.valormin = maximo * .25
                  porcentaje = .25;
                } else {
                  porcentaje = .4
                  rango.valormax = maximo * .25
                  rango.valormin = 1
                }

                var color = this.pSBC(porcentaje, color5)
                rango.color = color
                if (!this.containsObject(rango, this.rangos))
                  self.rangos.push(rango)
                c[i].setAttribute("fill", color)
              } else {


                var color = this.pSBC(.6, color5)
                var rango = {
                  valormax: 0,
                  valormin: 0,
                  color: color
                }
                if (!this.containsObject(rango, this.rangos))
                  self.rangos.push(rango)


                c[i].setAttribute("fill", color)
              }
            }


          })


        });


      },
      containsObject: function (obj, list) {
        var i;
        for (i = 0; i < list.length; i++) {
          if (list[i].color == obj.color) {
            return true;
          }
        }

        return false;
      },
      cambiaColor: function (a) {
        alert(a.target.id)
        this.auxiliar(a.target.id)
      },


      handleStateClick: function (e) {
        if (e.target.tagName === 'path') {
          // console.log(e.target.id);

          // alert(`Presionando el ${e.target.id}`);

          this.$refs.modal.showModal();
          this.$refs.modal.setTextModal(e.target.id, 'Este es un texto como prop desde el mapa');


        }
      },
      handleStateHover: function (e) {
        if (e.target.tagName === 'path') {

        }
      },

      // Version 4.0
      pSBC: (p, c0, c1, l) => {
        let r, g, b, P, f, t, h, i = parseInt, m = Math.round, a = typeof (c1) == "string";
        if (typeof (p) != "number" || p < -1 || p > 1 || typeof (c0) != "string" || (c0[0] != 'r' && c0[0] != '#') || (c1 && !a)) return null;
        if (!this.pSBCr) this.pSBCr = (d) => {
          let n = d.length, x = {};
          if (n > 9) {
            [r, g, b, a] = d = d.split(","), n = d.length;
            if (n < 3 || n > 4) return null;
            x.r = i(r[3] == "a" ? r.slice(5) : r.slice(4)), x.g = i(g), x.b = i(b), x.a = a ? parseFloat(a) : -1
          } else {
            if (n == 8 || n == 6 || n < 4) return null;
            if (n < 6) d = "#" + d[1] + d[1] + d[2] + d[2] + d[3] + d[3] + (n > 4 ? d[4] + d[4] : "");
            d = i(d.slice(1), 16);
            if (n == 9 || n == 5) x.r = d >> 24 & 255, x.g = d >> 16 & 255, x.b = d >> 8 & 255, x.a = m((d & 255) / 0.255) / 1000;
            else x.r = d >> 16, x.g = d >> 8 & 255, x.b = d & 255, x.a = -1
          }
          return x
        };
        h = c0.length > 9, h = a ? c1.length > 9 ? true : c1 == "c" ? !h : false : h, f = this.pSBCr(c0), P = p < 0, t = c1 && c1 != "c" ? this.pSBCr(c1) : P ? {
          r: 0,
          g: 0,
          b: 0,
          a: -1
        } : {r: 255, g: 255, b: 255, a: -1}, p = P ? p * -1 : p, P = 1 - p;
        if (!f || !t) return null;
        if (l) r = m(P * f.r + p * t.r), g = m(P * f.g + p * t.g), b = m(P * f.b + p * t.b);
        else r = m((P * f.r ** 2 + p * t.r ** 2) ** 0.5), g = m((P * f.g ** 2 + p * t.g ** 2) ** 0.5), b = m((P * f.b ** 2 + p * t.b ** 2) ** 0.5);
        a = f.a, t = t.a, f = a >= 0 || t >= 0, a = f ? a < 0 ? t : t < 0 ? a : a * P + t * p : 0;
        if (h) return "rgb" + (f ? "a(" : "(") + r + "," + g + "," + b + (f ? "," + m(a * 1000) / 1000 : "") + ")";
        else return "#" + (4294967296 + r * 16777216 + g * 65536 + b * 256 + (f ? m(a * 255) : 0)).toString(16).slice(1, f ? undefined : -2)
      },

      obtenNumeroMayor: function (lista) {
        return new Promise((resolve, reject) => {

          var numero = 0
          for (let a in lista) {
            if (lista[a].conteo > numero)
              numero = lista[a].conteo
          }
          resolve({
            error: false,
            value: numero
          })

        });
      },

      showRecursoDetail (idRecurso) {
        this.loading = true

        setTimeout( () => {

          this.loading = false
          this.$router.push({name: 'RecursoDetail', params: { id: idRecurso}})
        }, 2000)
      },


    },
    computed: {
      theme() {
        return this.$vuetify.theme.dark ? "dark" : "light";
      }
      ,
      colorCantidad(e) {
        // let id = e.target.id;

        const idEstados = Object.keys(this.cantRecursos)
        const valEstados = Object.values(this.cantRecursos)
        console.log(idEstados)
        console.log(valEstados)
        for (let id of idEstados) {


        }

        // for(let i=0; i < this.cantRecursos.length; i++){
        //   if(e.target.tagName === 'path' && 'path' === i) {
        //     return (this.i <= 100 && this.i > 70)  ? '#17FF00' : (this.i <= 70 && this.i > 30) ? '#FFFF00' : (this.i <= 30 && this.i > 0) ? '#FF0000' : this.color;
        //   }
        // }

      }
    }
    ,
    mounted() {

      this.GetDetalle()
      this.GetPrediccion()


      let color1 = "rgb(20,60,200)";
      let color2 = "rgba(20,60,200,0.67423)";
      let color3 = "#67DAF0";
      let color4 = "#5567DAF0";
      let color5 = "#F3A";
      let color6 = "#F3A9";
      let color7 = "rgb(200,60,20)";
      let color8 = "rgba(200,60,20,0.98631)";
      // Tests:

    }
    ,
  }
  ;
</script>

<style scoped>
  .contenedor {
    position: relative;
    overflow: hidden;

  }

  .tooltip {
    position: relative; /* making the .tooltip span a container for the tooltip text */
    border-bottom: 1px dashed #000; /* little indicater to indicate it's hoverable */
  }

  path:hover {
    color: tomato;
    fill: yellowgreen;
    z-index: -1;


    /* transform: scale(1.5,1.5); Igual que: scaleX(0.7) scaleY(0.7) */
    /* transform: scale(1.5); Igual que: scaleX(2) scaleY(0.5) */
    transform: translate(-20, -40) scale(4)

  }

  path {
    transition: 1s all;
    transform-origin: 50% 50%;
    transform-box: fill-box;

  }

  g {
    position: relative;
    overflow: hidden;
    transition: transform .2s ease-in-out;

  }

  .overflow-hidden {
    overflow: hidden;
  }


  p,
  h3,
  h2 {
    margin-top: 4px;
    overflow: hidden;
    display: -webkit-box;
    text-overflow: ellipsis;
    word-break: break-word;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
  }

  .subtitle {
    margin-top: 10px;
    font-size: 12px;
    font-weight: 600;
    color: black;
    margin-bottom: 8px;
  }

  .image-container {
    border-radius: 3px;
    overflow: hidden;
    position: relative;
    width: 100%;
    padding-top: 13em;
  }

  .image-content {
    height: 3em;
    width: 3em;
  }

  .image-text {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    padding: 32px 24px;
    display: flex;
    align-items: flex-end;
    background: rgba(0, 0, 0, 0.4);
  }

  .image-text h2 {
    margin: 0;
    color: white;
    text-align: center;
  }

  img {
    object-fit: cover;
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }


</style>

