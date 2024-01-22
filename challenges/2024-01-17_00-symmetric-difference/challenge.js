function main(...arrays) {
    // write your code here -----------------------------
    return [];
    // --------------------------------------------------
}

(_ => {
    const iteration = (index, arrays, expected) => {
        !!index && console.log(`test case ${ `00${index}`.slice(-2) } -------------------------------------`);
        console.time("took");
        const result = main(...arrays);
        console.timeEnd("took");
        const isSuccess = Array.isArray(result) && result.length === expected.length && JSON.stringify(expected.sort()) === JSON.stringify(result.sort());
        const testCaseText = `${isSuccess ? "SUCCESS" : "FAILED"} | input: ${JSON.stringify(arrays)} | expected: ${JSON.stringify(expected)} | got: ${JSON.stringify(result)}`;
        console.log(testCaseText);
        !!index && console.log("--------------------------------------------------");
        console.log();
    }
    
    const args = process.argv.slice(2);
    if (args.length === 0) {
        iteration(null, [[1, 2, 3], [2, 3, 4]], [1, 4]);
    } else {
        require("./challenge.tests").forEach((test, index) => iteration(index + 1, test.arrays, test.expected));
    }
})();