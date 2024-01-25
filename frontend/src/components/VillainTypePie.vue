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
  name: 'UnmaskedBar',
  components: { Bar },
  data: () => ({
    loaded: false,
    chartData: {
      labels: [],
      datasets: [{
        label: 'Counts',
        backgroundColor: [], // Example colors
        data: []
      }]
    },
    chartOptions: {
     responsive: true,
     title: {
        display: true,
        text: 'Who Unmasked the Most Villains?',
      }
    }
  }),
  async mounted () {
    this.loaded = false
    try {
      const response = await axios.get('http://localhost:8080/unmasked')
      const responseData = response.data
      this.chartData.datasets[0].data = responseData.map(entry => entry.unmaskerCount);
      this.chartData.labels = responseData.map(entry => entry.name);

      let names = responseData.map(entry => entry.name);
      let barColor = [];
      names.forEach(name => {
        switch (name) {
        case 'Velma Dinkley':
          barColor.push('#F98B08');
          break;
        case 'Fred Jones':
          barColor.push('#0081DF');
          break;
        case 'Daphne Blake':
          barColor.push('#6F1BA1');
          break;
        case 'Norville Rogers':
          barColor.push('#D1FF49');
          break;
        default:
          barColor.push('#B57530');
          break;
        }
      });
      this.chartData.datasets[0].backgroundColor = barColor;

      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
