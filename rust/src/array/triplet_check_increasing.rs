use pyo3::prelude::*;

#[pyfunction]
pub fn increasing_triplet(nums: Vec<i32>) -> bool {
    let (mut a, mut b) = (i32::MAX, i32::MAX);

    for n in nums.into_iter() {
        if n <= a {
            a = n;
        } else if n <= b {
            b = n;
        } else {
            return true;
        }
    }

    false
}
