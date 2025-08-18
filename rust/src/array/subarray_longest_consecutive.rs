use pyo3::prelude::*;
use std::collections::HashSet;

#[pyfunction]
pub fn longest_consecutive_sequence(nums: Vec<i32>) -> i32 {
    let set: HashSet<i32> = nums.into_iter().collect();
    let mut res = 0;

    for &n in &set {
        // avoid repeated check for previous intermediate point
        if !set.contains(&(n - 1)) {
            let mut m = 1;
            while set.contains(&(n + m)) {
                m += 1;
            }
            res = res.max(m);
        }
    }

    res
}
