<template>
  <div class="container">
    <Scatter v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Scatter } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LinearScale, PointElement, ScatterController } from 'chart.js';
import axios from 'axios';

ChartJS.register(Title, Tooltip, Legend, LinearScale, PointElement, ScatterController);

export default {
  name: 'AppearancesScatter',
  components: { Scatter },
  data: () => ({
    loaded: false,
    chartData: {
      labels: [],
      datasets: [{
        label: 'Catchphrases',
        backgroundColor: ['#fff56c', '#b9d61c', '#01a59c', '#f26722', '#faa954', '#d28d30', '#702f90', '#f8dd2f'],
        data: [],
      }],
    },
    chartOptions: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'What Are the Most Used Catchphrases?',
        },
      },
      scales: {
        x: {
          type: 'linear',
          position: 'bottom',
          title: {
            display: true,
            text: 'Number of Villains Caught',
          },
        },
        y: {
          type: 'linear',
          position: 'left',
          title: {
            display: true,
            text: 'Tropes/Catchphrase Use Count',
          },
        },
      },
    },
  }),
  async mounted() {
    this.loaded = false;
    try {
      const response = await axios.get('http://localhost:8080/tropeCaught');
      const responseData = response.data;
      this.chartData.datasets[0].data = responseData.map(entry => ({
        x: entry.caught,
        y: entry.tropeCount,
      }));
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

      this.loaded = true;
    } catch (e) {
      console.error(e);
    }
  },
};
</script>
