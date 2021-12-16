const ctx = document.getElementById("sales_chart").getContext("2d");

// Gradient Fill
let gradient = ctx.createLinearGradient(0, 0, 0, 400);
gradient.addColorStop(0, "#51e6c4");
gradient.addColorStop(1, "#25da91");

let delayed;

function addCurrencySign(value) {
  if (value == 0) {
    return value;
  }
  return "₹" + value;
}

let animation = {
  onComplete: () => {
    delayed = 0;
  },
  delay: (context) => {
    let delay = 0;
    if (context.type === "data" && context.mode == "default" && !delayed) {
      delay = context.dataIndex * 300 + context.datasetIndex * 100;
    }

    return delay;
  },
};

function countOccurences(arr, val) {
  return arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
}

(async function createYearChart() {
  const year = new Date().getFullYear();
  const salesData = await (await fetch(`/api/v1/get_sales/${year}`)).json();

  const data = {
    labels: salesData.labels,
    datasets: [
      {
        label: `Sales ${year}`,
        backgroundColor: gradient,
        pointBackgroundColor: "#87e4b6",
        tension: 0.4,
        fill: true,
        data: salesData.data,
      },
    ],
  };

  const config = {
    type: "bar",
    data: data,
    options: {
      radius: 3,
      hoverRadius: 5,
      hitRadius: 30,
      responsive: true,
      animation,
      scales: {
        y: {
          ticks: {
            callback: (value) => addCurrencySign(value),
          },
        },
      },
    },
  };

  // don't show the animation when the no of 0 sales is greater than or equal to 6.
  if (countOccurences(salesData.data, 0) >= 6) {
    delete config.options.animation;
  }

  const sales_chart = new Chart(ctx, config);
})();
