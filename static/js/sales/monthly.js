const ctx__monthly = document
  .getElementById("sales_chart__monthly")
  .getContext("2d");

(async function createMonthChart() {
  const year = new Date().getFullYear();
  const month = new Date().getMonth() + 1; // jan starts at 0
  const salesDataMonthly = await (
    await fetch(`/api/v1/get_sales/${year}/${month}`)
  ).json();

  let labels = [];

  for (i = 1; i <= salesDataMonthly.data.length; i++) {
    labels.push(i);
  }

  const data = {
    labels,
    datasets: [
      {
        label: `Sales ${month}/${year}`,
        backgroundColor: createGradient(ctx__monthly),
        pointBackgroundColor: "#87e4b6",
        borderColor: "rgb(35,67,36, 0.3)",
        fill: true,
        data: salesDataMonthly.data,
      },
    ],
  };

  const config = {
    type: "bar",
    data: data,
    options,
  };

  removeAnimation(salesDataMonthly.data, config);

  const sales_chart__monthly = new Chart(ctx__monthly, config);
})();
