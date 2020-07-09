package main

import "fmt"

func fib(n int) int {
	if n < 2 {
		return n
	}
	return fib(n - 2) + fib(n - 1)
}

func main() {
	fmt.Printf("%d\n", fib(38))
}
