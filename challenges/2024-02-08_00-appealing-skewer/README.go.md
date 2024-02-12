![logo](../../assets/logo-text.png)

# Challenge: The appealing skewer 🍡

Let’s think of ingredients to assemble a not only tasty but also appealing BBQed skewer. To make it appealing, the ingredients must be placed in a way that two pieces of the very same kind are never found consecutively repeated.

### 📋 The task

Design a function that takes an array of $n$ ingredients (strings) and returns the number of possible combinations that don’t have repeated consecutive values.

*Constraints:*

> $n > 0$

*Example:*

- input: `["🥔", "🥩", "🥩"]`

- possible combinations:

    ```js
    // p = potato
    // m<x> = meat

    // p     m1    m2    ❌
    ["🥔", "🥩", "🥩"]

    // p     m2    m1    ❌
    ["🥔", "🥩", "🥩"]

    // m1    p     m2    ✔
    ["🥩", "🥔", "🥩"]

    // m2    p     m1    ✔
    ["🥩", "🥔", "🥩"]

    // m1    m2    p    ❌
    ["🥩", "🥩", "🥔"]

    // m2    m1    p    ❌
    ["🥩", "🥩", "🥔"]
    ```

*Expected output:*

```js
["🥔", "🥩", "🥩"] => 2
```

## ⚙ The setup

To execute the challenge code, it's recommended to installl [go](https://go.dev/) on your system. Once installed, you can simply open your terminal into the challenge root directory and run the `go run .` command to execute your code. You may also run the `go test -v` command for your code to get tested.
