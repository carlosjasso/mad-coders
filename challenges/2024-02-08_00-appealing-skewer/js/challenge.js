export function calculateValidCombinations(ingredients) {
    // write your code here -----------------------------
    
    // --------------------------------------------------
}

process.env.npm_lifecycle_event === "start" && (_ => {
    const ingredients = ["🥔", "🥩", "🥩"];
    const expected = 2;
    const actual = calculateValidCombinations(ingredients);

    if (expected === actual)
        console.log(`SUCCESS | expected: ${expected} | got: ${actual}`);
    else
        console.log(`FAILED | expected: ${expected} | got: ${actual}`);
})();
