use pyo3::prelude::*;

// Patience sorting: maintain `tails` where tails[i] is the smallest tail of
// all increasing subsequences of length i+1. Binary search gives O(N log N).
#[pyfunction]
pub fn longest_increasing_subsequence(nums: Vec<i32>) -> usize {
    let mut tails: Vec<i32> = Vec::new();

    for &num in &nums {
        let pos = tails.partition_point(|&x| x < num);
        if pos == tails.len() {
            tails.push(num);
        } else {
            tails[pos] = num;
        }
    }

    tails.len()
}
