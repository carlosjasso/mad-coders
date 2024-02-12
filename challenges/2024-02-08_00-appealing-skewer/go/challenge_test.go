package main

import "testing"

type testCase struct {
	arg      []string
	expected int
}

var testCases = []testCase{
	{
		arg:      []string{"x", "x", "y"},
		expected: 2,
	},
	{
		arg:      []string{"x", "x", "x"},
		expected: 0,
	},
	{
		arg:      []string{"x", "x", "y", "y"},
		expected: 8,
	},
	{
		arg:      []string{"x", "y", "z", "a", "b", "c", "x"},
		expected: 3600,
	},
	{
		arg:      []string{"x", "y", "z", "a", "b", "x", "y"},
		expected: 2640,
	},
	{
		arg:      []string{"z", "z", "z", "z", "z", "z", "z", "z"},
		expected: 0,
	},
	{
		arg:      []string{"x"},
		expected: 1,
	},
	{
		arg:      []string{"x", "x", "x", "y"},
		expected: 0,
	},
	{
		arg:      []string{"x", "x", "x", "y", "y"},
		expected: 12,
	},
}

func TestCalculateValidCombinations(t *testing.T) {
	for i, test := range testCases {
		actual := calculateValidCombinations(test.arg)
		if actual == test.expected {
			t.Logf("TEST CASE %d | SUCCESS | expected: %d | got: %d", i+1, test.expected, actual)
		} else {
			t.Errorf("TEST CASE %d | FAILED | expected: %d | got: %d", i+1, test.expected, actual)
		}
	}
}
