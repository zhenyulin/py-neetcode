use pyo3::prelude::*;

#[pyfunction]
pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
    let (mut i, mut s, mut res) = (0, 0, nums.len() + 1);

    for j in 0..nums.len() {
        s += nums[j];

        while s >= target {
            res = res.min(j - i + 1);
            s -= nums[i];
            i += 1;
        }
    }

    if res > nums.len() { 0 } else { res as i32 }
}
