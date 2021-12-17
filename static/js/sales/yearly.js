const ctx__yearly = document
  .getElementById("sales_chart__yearly")
  .getContext("2d");

const options = {
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
};

function removeAnimation(data, config) {
  // don't show the animation when the no of 0 sales is greater than or equal to 6.
  if (countOccurences(data, 0) >= 6) {
    delete config.options.animation;
  }
}

(async function createYearChart() {
  const year = new Date().getFullYear();
  const salesDataYearly = await (
    await fetch(`/api/v1/get_sales/${year}`, { cache: "force-cache" })
  ).json();

  const data = {
    labels: salesDataYearly.labels,
    datasets: [
      {
        label: `Sales ${year}`,
        backgroundColor: createGradient(ctx__yearly),
        pointBackgroundColor: "#87e4b6",
        fill: true,
        data: salesDataYearly.data,
      },
    ],
  };

  const config = {
    type: "bar",
    data: data,
    options,
  };

  removeAnimation(salesDataYearly.data, config);

  const sales_chart__yearly = new Chart(ctx__yearly, config);
})();
