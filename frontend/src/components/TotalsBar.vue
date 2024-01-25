<template>
  <div class="container">
    <Bar v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'TotalsBar',
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: {
      labels: ['Investigators', 'Suspects', 'Villains'],
      datasets: [{
        label: 'Count',
        backgroundColor: ['#f87979', '#f8c879', '#79f8f8'], // Example colors
        data: []
      }]
    },
    chartOptions: {
      responsive: true,
      title: {
        display: true,
        text: 'Database Node Counts',
      }
    },
  }),
  async mounted () {
    this.loaded = false
    try {
      const response = await axios.get('http://localhost:8080/totals')
      const responseData = response.data
      this.chartData.datasets[0].data = [
        responseData.investigators,
        responseData.suspects,
        responseData.villains
      ]
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
