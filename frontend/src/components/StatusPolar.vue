<template>
  <div class="container">
    <PolarArea v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { PolarArea } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PolarAreaController, RadialLinearScale } from 'chart.js'
import axios from 'axios'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  PolarAreaController,
  RadialLinearScale,
)

export default {
  name: 'MotivePolar',
  components: { PolarArea },
  data: () => ({
    loaded: false,
    type: 'polarArea',
    chartData: {
      labels: [],
      datasets: [{
        label: 'Counts',
        backgroundColor: ['#d28d30', '#b9d61c', '#fff56c', '#f26722', '#01a59c', '#faa954', '#702f90', '#f8dd2f'],
        borderColor: ['#d28d30', '#b9d61c', '#fff56c', '#f26722', '#01a59c', '#faa954', '#702f90', '#f8dd2f'],
        borderWidth: 1,
        data: []
      }]
    },
    chartOptions: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Suspect Status Polar Chart - Alive or Incarcerated?',
        }
      }
    }
  }),
  async mounted() {
    this.loaded = false
    try {
      const response = await axios.get('http://localhost:8080/status')
      const responseData = response.data
      this.chartData.datasets[0].data = responseData.map(entry => entry.statusCount);
      this.chartData.labels = responseData.map(entry => entry.status);

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
