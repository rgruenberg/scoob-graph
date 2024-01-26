<template>
  <div class="container">
    <Pie v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PieController } from 'chart.js'
import axios from 'axios'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  PieController
)

export default {
  name: 'MotivePie',
  components: { Pie },
  data: () => ({
    loaded: false,
    type: 'pie',
    chartData: {
      labels: [],
      datasets: [{
        label: 'Counts',
        backgroundColor: ['#f26722','#d28d30', '#b9d61c', '#fff56c', '#01a59c', '#faa954', '#702f90', '#f8dd2f'],
        borderColor: ['#f26722','#d28d30', '#b9d61c', '#fff56c', '#01a59c', '#faa954', '#702f90', '#f8dd2f'],
        borderWidth: 1,
        data: []
      }]
    },
    chartOptions: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'What Disguises Did the Villains Use?',
        }
      }
    }
  }),
  async mounted() {
    this.loaded = false
    try {
      const response = await axios.get('http://localhost:8080/villainType')
      const responseData = response.data
      this.chartData.datasets[0].data = responseData.map(entry => entry.typeCount);
      this.chartData.labels = responseData.map(entry => entry.type);

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
