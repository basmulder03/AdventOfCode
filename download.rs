extern crate reqwest;

use std::env;
use std::fs;
use std::io::Write;

fn main() {
    // get year, day, and session id from command line arguments
    let mut args = env::args();
    let year = args.nth(1).expect("expected year number");
    let year: u32 = year.parse().expect("invalid year number");
    let day = args.nth(2).expect("expected day number");
    let day: u32 = day.parse().expect("invalid day number");
    let session_id = args.nth(3).expect("expected session id");

    // construct url for input data
    let url = format!("https://adventofcode.com/{}/day/{}/input", year, day);

    // create client and send request for input data
    let client = reqwest::Client::new();
    let mut res = client
        .get(&url)
        .header("Cookie", format!("session={}", session_id)) // include session cookie in request header
        .send()
        .expect("error sending request");

    // read response text and store as string
    let input = res.text().expect("error reading response");

    // create directory for input data if it does not already exist
    let dir = format!("input/{}", year);
    if !fs::metadata(&dir).is_ok() {
        fs::create_dir(&dir).expect("error creating directory");
    }

    // create file for input data
    let path = format!("{}/day{:02}.txt", dir, day);
    let mut file = fs::File::create(&path).expect("error creating file");

    // write input data to file
    file.write_all(input.as_bytes()).expect("error writing to file");
}
