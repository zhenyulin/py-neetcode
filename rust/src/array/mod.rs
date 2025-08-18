use pyo3::prelude::*;

mod rotated_sorted_array_min;
mod rotated_sorted_array_search;
mod search_element_peak;
mod search_min_max_diff_with_operation;
mod subarray_longest_consecutive;
mod subarray_max_product;
mod subarray_min_size_sum;
mod subarray_product_except_self;
mod subsequence_fixed_size_max_min_gap;

#[pymodule]
pub mod array {
    use super::*;

    #[pymodule_export]
    use rotated_sorted_array_min::find_min;
    #[pymodule_export]
    use rotated_sorted_array_search::search;
    #[pymodule_export]
    use search_element_peak::find_peak_element;
    #[pymodule_export]
    use search_min_max_diff_with_operation::smallest_range;
    #[pymodule_export]
    use subarray_longest_consecutive::longest_consecutive_sequence;
    #[pymodule_export]
    use subarray_max_product::max_product;
    #[pymodule_export]
    use subarray_min_size_sum::min_sub_array_len;
    #[pymodule_export]
    use subarray_product_except_self::product_except_self;
    #[pymodule_export]
    use subsequence_fixed_size_max_min_gap::max_min_gap;
}
