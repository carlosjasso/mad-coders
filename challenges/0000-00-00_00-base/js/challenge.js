export function doSomething() {
    // write your code here -----------------------------



    // --------------------------------------------------
}

(_ => {
    console.time("took");
    doSomething();
    console.log();
    console.timeEnd("took");
})();
