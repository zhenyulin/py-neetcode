use pyo3::prelude::*;
use std::iter;

#[pyfunction]
pub fn largest_area_rectangle(heights: Vec<i32>) -> i32 {
    let n = heights.len();
    let mut res = 0;
    let mut stack = Vec::with_capacity(n);

    for (i, &h) in heights.iter().chain(iter::once(&0)).enumerate() {
        let mut left = i;

        while stack.last().map(|&(_, height)| height > h).unwrap_or(false) {
            let (start, height) = stack.pop().unwrap();
            let width = (i - start) as i32;
            res = res.max(width * height);
            left = start;
        }

        stack.push((left, h));
    }

    res
}
