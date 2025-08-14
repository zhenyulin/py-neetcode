use pyo3::prelude::*;

#[pyfunction]
pub fn find_min(nums: Vec<i32>) -> PyResult<i32> {
    let (mut l, mut r) = (0usize, nums.len() - 1);

    while l < r {
        let m = (l + r) / 2;
        if nums[m] < nums[r] {
            r = m;
        } else {
            l = m + 1;
        }
    }
    Ok(nums[l])
}
