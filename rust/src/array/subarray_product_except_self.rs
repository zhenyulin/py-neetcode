use pyo3::prelude::*;

/* 2x scans vs 1x two-sided scans

2x scans would be completely linear in memory therefore faster in reality
*/

#[pyfunction]
pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let (mut tmp, mut res) = (1, vec![1; n]);

    for i in 0..n {
        res[i] *= tmp;
        tmp *= nums[i];
    }

    tmp = 1;
    for i in (0..n).rev() {
        res[i] *= tmp;
        tmp *= nums[i];
    }

    res
}
