import assert from "node:assert";
import { doSomething } from "./challenge.js";

(_ => {
    try {
        assert.deepEqual([1, 2, 3], [1, 2, 3], "this is just a test")
        console.log("success!");
    } catch (error) {
        console.error("failed");
    }
})()