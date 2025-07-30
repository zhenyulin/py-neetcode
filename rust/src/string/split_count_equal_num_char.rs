use pyo3::prelude::*;

const MOD_BASE: u64 = 1_000_000_007;

// s.len() >= 3

#[pyfunction]
pub fn num_ways(s: &str) -> PyResult<i32> {
    let ones = s.chars().filter(|&c| c == '1').count() as u64;

    if ones == 0 {
        let len = s.len() as u64;
        let res = ((len - 1) * (len - 2) / 2) % MOD_BASE;
        return Ok(res as i32);
    }

    if ones % 3 != 0 {
        return Ok(0);
    }

    let split_one = ones / 3;
    let split_two = 2 * split_one;

    let mut first: u64 = 0;
    let mut second: u64 = 0;
    let mut count: u64 = 0;

    for char in s.chars() {
        if char == '1' {
            count += 1;
        }

        if count == split_one {
            first += 1;
        } else if count == split_two {
            second += 1;
        } else if count > split_two {
            break;
        }
    }

    Ok(((first * second) % MOD_BASE) as i32)
}
