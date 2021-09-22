const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout
});

function add(a, b) {
    return +a + +b
}

readline.question("numbers:", (numbers) => {
    // 10 30

    const a = numbers.split(" ")[0];
    const b = numbers.split(" ")[1];

    const result = add(a, b);

    console.log(result);

    readline.close();
});
