extern crate aoc_util;

use std::env;
use std::fs;

fn main() {
    let mut args = env::args();
    let day = args.nth(1).expect("expected day number");
    let day: u32 = day.parse().expect("invalid day number");
    let input = fs::read_to_string(format!("input/day{:02}.txt", day)).expect("error reading input");

    let part1 = solve_part1(&input);
    println!("Part 1: {}", part1);

    let part2 = solve_part2(&input);
    println!("Part 2: {}", part2);
}

fn solve_part1(input: &str) -> String {
    // solve part 1 and return the solution as a string
    String::new()
}

fn solve_part2(input: &str) -> String {
    // solve part 2 and return the solution as a string
    String::new()
}