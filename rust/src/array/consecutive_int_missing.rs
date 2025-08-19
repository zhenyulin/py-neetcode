use pyo3::prelude::*;

#[pyfunction]
pub fn missing_number(nums: Vec<i32>) -> i32 {
    let mut diff = 0;

    for (i, n) in nums.iter().enumerate() {
        diff += i as i32 + 1 - n;
    }

    diff
}
