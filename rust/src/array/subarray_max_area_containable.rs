use pyo3::prelude::*;

#[pyfunction]
pub fn max_area(height: Vec<i32>) -> i32 {
    let (mut l, mut r) = (0, height.len() - 1);
    let mut res = 0;

    while l < r {
        let bar = height[l].min(height[r]);
        let width = (r - l) as i32;
        res = res.max(bar * width);

        if height[l] < height[r] {
            l += 1;
        } else {
            r -= 1;
        }
    }

    res
}
