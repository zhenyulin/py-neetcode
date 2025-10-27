use pyo3::prelude::*;

#[pyfunction]
pub fn k_closest(mut points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
    let k = k as usize;

    points.select_nth_unstable_by_key(k - 1, |v| {
        let (x, y) = (v[0], v[1]);
        x * x + y * y
    });
    points.truncate(k);
    points
}
