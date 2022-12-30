const table = document.querySelector(".overview-table");
let calories = 0,
    fat = 0,
    carbohydrates = 0,
    protein = 0;

for (let i = 1; i < table.rows.length; i++) {
    calories += parseFloat(table.rows[i].cells[1].innerHTML);

    fat += parseFloat(table.rows[i].cells[2].innerHTML);
    fat = Math.round(fat);

    carbohydrates += parseFloat(table.rows[i].cells[3].innerHTML);
    carbohydrates = Math.round(carbohydrates);

    protein += parseFloat(table.rows[i].cells[4].innerHTML);
    protein = Math.round(protein);
}

let total = fat + carbohydrates + protein;

let fatPercentage = Math.round((fat / total) * 100);
let carbohydratesPercentage = Math.round((carbohydrates / total) * 100);
let proteinPercentage = Math.round((protein / total) * 100);

fatPercentage = fatPercentage ? fatPercentage : 0;
carbohydratesPercentage = carbohydratesPercentage ? carbohydratesPercentage : 0;
proteinPercentage = proteinPercentage ? proteinPercentage : 0;

Chart.defaults.global.defaultFontFamily = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"';
Chart.defaults.global.defaultFontColor = "#1a1a1a";

const ctx = document.getElementById("foodlogGraph");
const foodlogGraph = new Chart(ctx, {
    type: "pie",
    data: {
        labels: ["Fat " + fatPercentage + "%", "Carbs " + carbohydratesPercentage + "%", "Protein " + proteinPercentage + "%"],
        datasets: [
            {
                data: [fatPercentage, carbohydratesPercentage, proteinPercentage],
                backgroundColor: ["#7982B9", "#A5C1DC", "#E9F6FA"],
            },
        ],
    },
    options: {
        responsive: false,
        maintainAspectRatio: false,
        animation: {
            animateScale: true,
        },
        plugins: {
            legend: {
                display: true,
                position: "bottom",
            },
            title: {
                display: true,
                text: "Macro Breakdown",
                font: {
                    size: 20,
                },
            },
            datalabels: {
                display: true,
                color: "#fff",
                font: {
                    weight: "bold",
                    size: 16,
                },
                textAlign: "center",
            },
        },
    },
});
