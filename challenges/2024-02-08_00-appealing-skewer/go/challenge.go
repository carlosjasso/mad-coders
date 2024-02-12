package main

import "fmt"

func calculateValidCombinations(ingredients []string) int {
	// write your code here -----------------------------

	// --------------------------------------------------
}

func main() {
	ingredients := []string{"🥔", "🥩", "🥩"}
	expected := 2
	actual := calculateValidCombinations(ingredients)

	if expected == actual {
		fmt.Printf("SUCCESS | expected: %d | got: %d", expected, actual)
	} else {
		fmt.Printf("FAILED | expected: %d | got: %d", expected, actual)
	}
}
