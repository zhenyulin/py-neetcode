use pyo3::prelude::*;
use std::cmp::{max, min};

#[pyfunction]
pub fn smallest_range(mut nums: Vec<i32>, k: i32) -> i32 {
    nums.sort_unstable();

    let (n, m) = (nums[0], nums[nums.len() - 1]);
    nums.windows(2).fold(m - n, |res, w| {
        res.min(max(m - k, w[0] + k) - min(n + k, w[1] - k))
    })
}
