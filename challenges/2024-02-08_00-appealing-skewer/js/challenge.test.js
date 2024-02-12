import { calculateValidCombinations } from "./challenge.js";

const testCases = [
    {
        arg: ["x", "x", "y"],
        expected: 2,
    },
    {
        arg: ["x", "x", "x"],
        expected: 0,
    },
    {
        arg: ["x", "x", "y", "y"],
        expected: 8,
    },
    {
        arg: ["x", "y", "z", "a", "b", "c", "x"],
        expected: 3600,
    },
    {
        arg: ["x", "y", "z", "a", "b", "x", "y"],
        expected: 2640,
    },
    {
        arg: ["z", "z", "z", "z", "z", "z", "z", "z"],
        expected: 0,
    },
    {
        arg: ["x"],
        expected: 1,
    },
    {
        arg: ["x", "x", "x", "y"],
        expected: 0,
    },
    {
        arg: ["x", "x", "x", "y", "y"],
        expected: 12,
    }
]

process.env.npm_lifecycle_event === "test" && (_ => {
    for (let i = 0; i < testCases.length; i++) {
        const test = testCases[i];
        const actual = calculateValidCombinations(test.arg);
        
        if (test.expected === actual)
            console.log(`SUCCESS | expected: ${test.expected} | got: ${actual}`);
        else
            console.log(`FAILED | expected: ${test.expected} | got: ${actual}`);
    }
})();