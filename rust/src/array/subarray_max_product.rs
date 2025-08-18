use pyo3::prelude::*;

#[pyfunction]
pub fn max_product(nums: Vec<i32>) -> i32 {
    let (mut res, mut _max, mut _min) = (nums[0], nums[0], nums[0]);

    for &n in &nums[1..] {
        let (a, b, c) = (n, n * _max, n * _min);
        _max = a.max(b).max(c);
        _min = a.min(b).min(c);
        res = res.max(_max);
    }
    res
}
