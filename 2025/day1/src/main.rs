use std::fs;

fn main() {
    let input = fs::read_to_string("src/input.txt").expect("Couldn't read file!");
    let count_1 = count_zeroes_part1(&input);
    let count_2 = count_zeroes_part2(&input);
    println!("The password for part 1 is: {}", count_1);
    println!("The password for part 2 is: {}", count_2);
}

fn count_zeroes_part1(input: &str) -> i32 {
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

fn count_zeroes_part2(input: &str) -> i32 {
    let mut position = 50;
    let mut count = 0;

    for line in input.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }

        let direction: &str = &line[0..1];
        let distance: i32 = line[1..].parse().expect("Not valid!");

        count += count_clicks_through_zero(position, direction, distance);

        position = match direction {
            "L" => (position + distance) % 100,
            "R" => (position - distance).rem_euclid(100),
            _ => panic!("Invalid entry"),
        };
    }

    count
}

fn count_clicks_through_zero(start: i32, direction: &str, distance: i32) -> i32 {
    match direction {
        "L" => {
            let first_zero_distance = if start == 0 { 100 } else { 100 - start };

            if distance < first_zero_distance {
                return 0;
            }

            1 + (distance - first_zero_distance) / 100
        }
        "R" => {
            let first_zero_distance = if start == 0 { 100 } else { start };

            if distance < first_zero_distance {
                return 0;
            }

            1 + (distance - first_zero_distance) / 100
        }
        _ => panic!("Invalid entry"),
    }
}
