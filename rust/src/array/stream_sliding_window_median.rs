use pyo3::prelude::*;
use std::cmp::Reverse; // use this can avoid the -i32:MIN overflow
use std::collections::{BinaryHeap, HashMap};

/// Generic prune for a BinaryHeap where `get_val` extracts the original i32 value
/// represented by the heap's top element.
/// - `heap` is mutated by popping expired elements.
/// - `expired` maps value -> remaining expired count to remove lazily.
fn prune<T, F>(heap: &mut BinaryHeap<T>, expired: &mut HashMap<i32, i32>, accessor: F)
where
    T: Ord,
    F: Fn(&T) -> i32,
{
    while let Some(top) = heap.peek() {
        let v = accessor(top);
        let Some(count) = expired.get_mut(&v) else {
            break;
        };
        *count -= 1;
        heap.pop();

        if *count == 0 {
            expired.remove(&v);
        }
    }
}

#[pyfunction]
pub fn sliding_window_median(nums: Vec<i32>, k: usize) -> Vec<f64> {
    if k == 0 {
        return vec![];
    }

    let mut res: Vec<f64> = Vec::with_capacity(nums.len().saturating_sub(k) + 1);
    let mut left: BinaryHeap<i32> = BinaryHeap::new(); // max-heap
    let mut right: BinaryHeap<Reverse<i32>> = BinaryHeap::new(); // min-heap by Reverse
    let mut expired: HashMap<i32, i32> = HashMap::new();

    for i in 0..nums.len() {
        // Insert: push into left, then move the largest from left to right.
        // Ensure the ordering between left and right.
        left.push(nums[i]);
        right.push(Reverse(left.pop().expect("non-empty"))); // left is guaranteed to be non-empty

        // Ensure left has at least as many elements as right, storing potential median in left
        if i < k && right.len() > left.len() {
            left.push(right.pop().expect("non-empty").0); // right is guaranteed to be non-empty
        }

        // handle sliding expiration
        if i >= k {
            let expiring = nums[i - k];
            *expired.entry(expiring).or_insert(0) += 1;

            // If the expiring value belongs to left (<= max of left), we need to
            // move one element from right to left to keep sizes consistent
            if &expiring <= left.peek().expect("non-empty") {
                left.push(right.pop().expect("non-empty").0);
            }

            // Prune both heaps of any expired tops (do not rebalance here;
            // the prior move from right->left keeps sizes consistent as in Python)
            prune(&mut left, &mut expired, |v| *v);
            prune(&mut right, &mut expired, |v| v.0);
        }

        // record median when window is full
        if i >= k - 1 {
            let l = *left.peek().expect("non-empty") as f64;
            res.push(if k % 2 == 1 {
                // odd window size -> median is top of left
                l
            } else {
                // even window size -> average of tops of left and right
                (l + right.peek().expect("non-empty").0 as f64) / 2.0
            })
        }
    }

    res
}
