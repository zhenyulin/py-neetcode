use pyo3::prelude::*;

/* NOTE: set vs sort
- for set, each lookup would perform a hash + probe logic, with the probe jumps around RAM
    - while for sorted array, the memory scan would be linear
    - especially when the hash algorithm is expensive, the O(N) would be slower than O(NLogN)
        - std::collections::HashSet uses SipHash, more expensive than AHashSet
*/

#[pyfunction]
pub fn longest_consecutive_sequence(mut nums: Vec<i32>) -> i32 {
    if nums.is_empty() {
        return 0;
    }
    nums.sort_unstable();

    let (mut res, mut m) = (1, 1);
    for i in 1..nums.len() {
        if nums[i] == nums[i - 1] {
            continue;
        }
        if nums[i] == nums[i - 1] + 1 {
            m += 1;
        } else {
            res = res.max(m);
            m = 1;
        }
    }
    res.max(m)
}
