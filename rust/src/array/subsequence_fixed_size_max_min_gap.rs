use pyo3::prelude::*;

#[pyfunction]
pub fn max_min_gap(nums: Vec<i32>, m: i32) -> i32 {
    fn possible(nums: &[i32], m: i32, gap: i32) -> bool {
        let (mut last, mut count) = (nums[0], m - 1);
        for &n in nums.iter().skip(1) {
            if n - last >= gap {
                last = n;
                count -= 1;
                if count == 0 {
                    return true;
                }
            }
        }
        false
    }

    let (mut l, mut r) = (0, nums[nums.len() - 1] - nums[0]);

    while l <= r {
        let mid = (l + r) / 2;

        if possible(&nums, m, mid) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    l - 1
}
