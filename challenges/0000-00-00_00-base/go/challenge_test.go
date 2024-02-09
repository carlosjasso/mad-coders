package main

import "testing"

func TestSomething(t *testing.T) {
	DoSomething()
	t.Log("some result")
	t.Errorf("some error")
}
