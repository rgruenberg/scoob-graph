<template>
  <v-app>
    <v-app-bar color="#7BC74C">
      <v-toolbar-title>Scooby Doo Data</v-toolbar-title>
    </v-app-bar>
    <v-main>
      <v-container>
        <v-row>
          <v-col class=".v-col-4">
            <TotalsBar />
          </v-col>
          <v-col class=".v-col-6">
            <AppearancesScatter />
          </v-col>
        </v-row>
        <v-row>
          <v-col class=".v-col-6">
            <CaughtBar />
          </v-col>
          <v-col class=".v-col-6">
            <UnmaskedBar />
          </v-col>
        </v-row>
        <v-row>
          <v-col class=".v-col-6">
            <StatusPolar />
          </v-col>
          <v-col class=".v-col-6">
            <MotiveDonut />
          </v-col>
        </v-row>
        <v-row>
          <v-col class=".v-col-6">
            <TropeRadar />
          </v-col>
          <v-col class=".v-col-6">
            <VillainTypePie />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>

  //
</script>
