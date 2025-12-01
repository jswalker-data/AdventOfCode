use std::fs;

fn main() {
    let input = fs::read_to_string("src/input.txt").expect("Couldn't read file!");
    let count = count_zeroes(&input);
    println!("The password is: {}", count);
}

fn count_zeroes(input: &str) -> i32 {
    let mut position = 50;
    let mut count = 0;

    for line in input.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }

        let direction: &str = &line[0..1];
        let distance: i32 = line[1..].parse().expect("Not valid!");

        position = match direction {
            "L" => (position + distance) % 100,
            "R" => (position - distance).rem_euclid(100),
            _ => panic!("Invalid entry"),
        };

        if position == 0 {
            count += 1;
        }
    }

    count
}
