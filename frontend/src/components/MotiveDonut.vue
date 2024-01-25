<template>
  <div class="container">
    <Doughnut v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, DoughnutController, CategoryScale, LinearScale, ArcElement } from 'chart.js'
import axios from 'axios'

ChartJS.register(Title, Tooltip, Legend, DoughnutController, CategoryScale, LinearScale, ArcElement)

export default {
  name: 'MotiveDonut',
  components: { Doughnut },
  data: () => ({
    loaded: false,
    type: 'doughnut',
    chartData: {
      labels: [],
      datasets: [{
        label: 'Counts',
        backgroundColor: ['#f87979', '#f8c879', '#79f8f8'], // Example colors
        data: []
      }]
    },
    chartOptions: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'What is the Most Popular Motive Among Villains?',
        }
      }
    }
  }),
  async mounted () {
    this.loaded = false
    try {
      const response = await axios.get('http://localhost:8080/motives')
      const responseData = response.data
      this.chartData.datasets[0].data = responseData.map(entry => entry.motiveCount);
      this.chartData.labels = responseData.map(entry => entry.motive);

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
