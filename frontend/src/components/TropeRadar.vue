<template>
  <div class="container">
    <Radar v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Radar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, RadarController, LineElement } from 'chart.js'
import axios from 'axios'

ChartJS.register(Title, Tooltip, Legend, CategoryScale, LinearScale, RadarController, LineElement)

export default {
  name: 'TropeRadar',
  components: { Radar },
  data: () => ({
    loaded: false,
    type: 'radar',
    chartData: {
      labels: [],
      datasets: [{
        label: 'Counts',
        backgroundColor: '#702f90',
        borderColor: '#702f90',
        pointBackgroundColor: '#702f90',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: '#702f90',
        data: []
      }]
    },
    chartOptions: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'What Are the Most Used Catchphrases?',
        }
      }
    }
  }),
  async mounted() {
    this.loaded = false
    try {
      const response = await axios.get('http://localhost:8080/catchphrase')
      const responseData = response.data
      this.chartData.datasets[0].data = responseData.map(entry => entry.tropeCount);
      this.chartData.labels = responseData.map(entry => entry.phrase);

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
