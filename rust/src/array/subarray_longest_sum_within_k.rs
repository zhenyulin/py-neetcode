use pyo3::prelude::*;

#[pyfunction]
pub fn longest_sum_within_k(arr: Vec<i32>, k: i32) -> i32 {
    let (mut res, mut sum) = (0, arr[0]);
    let (mut i, mut j) = (0, 0);

    while i < arr.len() && j < arr.len() - 1 {
        if sum <= k {
            j += 1;
            sum += arr[j];
        }

        while sum <= k && i > 0 {
            i -= 1;
            sum += arr[i];
        }

        if sum > k {
            sum -= arr[i];
            i += 1;
        }

        res = res.max(j - i + 1);
    }

    res as i32
}
