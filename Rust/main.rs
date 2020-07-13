fn fib( n: u128 ) -> u128 {
    if n < 2 {
        return n;
    }

	return fib(n - 2) + fib(n - 1);
}

fn main() {
	println!("{}", fib(38));
}
