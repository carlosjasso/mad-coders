package main

import "testing"

func TestSomething(t *testing.T) {
	t.Log("some result")
	t.Errorf("some error")
}
