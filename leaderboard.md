# 🧪 Mad Coders - leaderboard

## 2024-01-12 - [Challenge: 100 doos](./challenges/2024-01-08_00_100-doors) - Isaac Tzab

```js
function main() {
    const sqtDoors = Math.sqrt(100);
    const openDoors = new Set();
    const toggleFn = (i) => i <= sqtDoors && ( openDoors.add(i * i), toggleFn(i + 1));
    toggleFn(1);
    console.log(openDoors);
}

(_ => {
    console.time("took");
    main();
    console.log();
    console.timeEnd("took");
})();
```