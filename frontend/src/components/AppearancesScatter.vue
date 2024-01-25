<template>
  <div class="container">
    <Bar v-if="loaded" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Scatter } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LinearScale, PointElement } from 'chart.js';
import axios from 'axios';

ChartJS.register(Title, Tooltip, Legend, LinearScale, PointElement);

export default {
  name: 'AppearancesScatter',
  extends: Scatter,
  data: () => ({
    loaded: false,
    chartData: {
      labels: [],
      datasets: [{
        label: 'Investigators',
        backgroundColor: ['#f87979', '#f8c879', '#79f8f8'],
        data: [],
      }],
    },
    chartOptions: {
      responsive: true,
      scales: {
        x: {
          type: 'linear',
          position: 'bottom',
          title: {
            display: true,
            text: 'Number of Appearances',
          },
        },
        y: {
          type: 'linear',
          position: 'left',
          title: {
            display: true,
            text: 'Personal Trope Counts',
          },
        },
      },
    },
  }),
  async mounted () {
    this.loaded = false
    try {
      const response = await axios.get('http://localhost:8080/appearances');
      const responseData = response.data;
      this.chartData.datasets[0].data = response.data.map(entry => ({
          x: entry.investigatorAppearances,
          y: entry.catchphraseCount,
      }));
      this.chartData.labels = responseData.map(entry => entry.name);

      console.log(response);

      this.loaded = true;
    } catch (e) {
      console.error(e);
    }
  }
}
</script>