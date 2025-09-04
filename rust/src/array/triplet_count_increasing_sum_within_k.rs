use pyo3::prelude::*;

#[pyfunction]
pub fn count_triplets(mut arr: Vec<i32>, t: i32) -> i32 {
    arr.sort_unstable();

    let mut res = 0;

    for a in 0..(arr.len() - 2) {
        let (mut b, mut c) = (a + 1, arr.len() - 1);

        while b < c {
            if arr[a] + arr[b] + arr[c] <= t {
                res += c - b;
                b += 1;
            } else {
                c -= 1;
            }
        }
    }

    res as i32
}
