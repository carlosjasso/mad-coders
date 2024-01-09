![logo](../../assets/logo-text.png)

# Challenge: 100 doors

There are 100 doors in a row that are all initially closed.

You make 100 passes by the doors.

The first time through, visit every door and *toggle* the door (if the door is closed, open it; if it is open, close it).

The second time, only visit every 2<sup>nd</sup> door  (door #2, #4, #6, ...), and toggle it.

The third time, visit every 3<sup>rd</sup> door (door #3, #6, #9, ...), etc, until you only visit the 100<sup>th</sup> door.

Write a function that prints to the console the state of the doors after the last pass. Show the result in an aray with *only* the number of those doors that remain open.

*Expected output:*

```js
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## The setup

To run this challenge, it's recommended to installl [nodejs](https://nodejs.org/en) on your system. Once installed, you can simply open your terminal into the challenge directory and run: 
```bash
npm run start
```
