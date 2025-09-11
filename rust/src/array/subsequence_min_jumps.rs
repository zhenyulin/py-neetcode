use pyo3::prelude::*;

#[pyfunction]
pub fn min_jump(nums: Vec<i32>) -> i32 {
    let (mut step, mut i, mut j) = (0, 0, 0);

    while j < nums.len() - 1 {
        let mut max = i;
        (i..j + 1).for_each(|k| {
            max = max.max(k + nums[k] as usize);
        });
        (i, j) = (j + 1, max);
        step += 1;
    }

    step
}
