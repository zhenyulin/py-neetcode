use pyo3::prelude::*;

#[pyfunction]
pub fn find_shortest_subarray_to_remove(arr: Vec<i64>) -> i32 {
    let n = arr.len();

    let mut a = 0;
    while a + 1 < n && arr[a + 1] >= arr[a] {
        a += 1;
    }

    if a == n - 1 {
        return 0;
    }

    let mut b = n - 1;
    while b > 0 && arr[b] >= arr[b - 1] {
        b -= 1;
    }

    let mut res = b.min(n - 1 - a);

    let (mut i, mut j) = (0, b);

    while i <= a && j < n {
        if arr[i] <= arr[j] {
            res = res.min(j - 1 - i);
            i += 1;
        } else {
            j += 1;
        }
    }

    res as i32
}
