use pyo3::prelude::*;
use std::collections::HashMap;

#[pyfunction]
pub fn two_sum_k(nums: Vec<i32>, target: i32) -> PyResult<Vec<usize>> {
    let mut map: HashMap<i32, usize> = HashMap::with_capacity(nums.len());

    for (i, &n) in nums.iter().enumerate() {
        if let Some(&j) = map.get(&n) {
            return Ok(vec![j, i]);
        }
        map.insert(target - n, i);
    }

    Ok(Vec::new())
}
