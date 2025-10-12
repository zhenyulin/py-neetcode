use pyo3::prelude::*;
use std::collections::HashMap;

#[pyfunction]
pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
    let (mut res, mut acc) = (0, 0);
    let mut counter = HashMap::with_capacity(nums.len() + 1);

    counter.insert(0, 1);

    for n in nums {
        acc += n;
        res += counter.get(&(acc - k)).copied().unwrap_or(0);
        *counter.entry(acc).or_insert(0) += 1;
    }

    res
}
