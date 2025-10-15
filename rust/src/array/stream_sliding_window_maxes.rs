use pyo3::prelude::*;
use std::collections::VecDeque;

#[pyfunction]
pub fn window_maxes(nums: Vec<i32>, k: usize) -> Vec<i32> {
    let n = nums.len();
    let mut res = Vec::with_capacity(n - k + 1);
    let mut stack = VecDeque::with_capacity(k);

    for i in 0..n {
        while stack.back().map(|&j| nums[j] < nums[i]).unwrap_or(false) {
            stack.pop_back();
        }

        stack.push_back(i);

        if i >= stack.front().copied().unwrap_or(0) + k {
            stack.pop_front();
        }

        if i >= k - 1 {
            res.push(nums[*stack.front().unwrap()]);
        }
    }

    res
}
