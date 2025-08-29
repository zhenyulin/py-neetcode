use pyo3::prelude::*;

#[pyfunction]
pub fn total_patch(heights: Vec<i32>) -> PyResult<i32> {
    // search from the two ends for the shorter bar for filling
    // and iterate inside to fill up the possible tallest bar on the lower side
    let (mut i, mut j) = (0, heights.len() - 1);
    let (mut fill, mut left, mut right) = (0, 0, 0);

    while i < j {
        if heights[i] > heights[j] {
            right = right.max(heights[j]);
            fill += right - heights[j];
            j -= 1;
        } else {
            left = left.max(heights[i]);
            fill += left - heights[i];
            i += 1;
        }
    }

    Ok(fill)
}
