function createGradient(ctx) {
  const gradient = ctx.createLinearGradient(0, 0, 0, 400);
  gradient.addColorStop(1, "rgba(81,230,196, 0.4)");
  gradient.addColorStop(0, "rgb(37,218,145)");

  return gradient;
}

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
