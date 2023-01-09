extern crate aoc_util;

use std::env;
use std::fs;

fn main() {
    // get day number from command line arguments
    let mut args = env::args();
    let day = args.nth(1).expect("expected day number");
    let day: u32 = day.parse().expect("invalid day number");

    // read input from file
    let input = fs::read_to_string(format!("input/day{:02}.txt", day)).expect("error reading input");

    // solve part 1 and print the solution
    let part1 = solve_part1(&input);
    println!("Part 1: {}", part1);

    // solve part 2 and print the solution
    let part2 = solve_part2(&input);
    println!("Part 2: {}", part2);
}

fn solve_part1(input: &str) -> String {
    // total fuel required
    let mut total_fuel = 0;

    // iterate over each line of input
    for line in input.lines() {
        // parse mass from line
        let mass: i32 = line.parse().expect("invalid input");

        // calculate fuel required for mass and add to total fuel
        total_fuel += (mass / 3) - 2;
    }

    // return total fuel as a string
    total_fuel.to_string()
}

fn solve_part2(input: &str) -> String {
    // total fuel required
    let mut total_fuel = 0;

    // iterate over each line of input
    for line in input.lines() {
        // parse mass from line
        let mut mass: i32 = line.parse().expect("invalid input");

        // calculate fuel required for mass and add to total fuel, while mass is positive
        while mass > 0 {
            mass = (mass / 3) - 2;
            if mass > 0 {
                total_fuel += mass;
            }
        }
    }

    // return total fuel as a string
    total_fuel.to_string()
}