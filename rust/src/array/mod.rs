use pyo3::prelude::*;

mod circular_index_cover_cost;
mod consecutive_int_missing;
mod rotated_sorted_array_min;
mod rotated_sorted_array_search;
mod search_element_peak;
mod search_min_max_diff_with_operation;
mod search_two_indexes_sum_to_k;
mod sorted_array_two_indexes_sum_to_k;
mod stream_sliding_window_maxes;
mod subarray_addition_multiple;
mod subarray_count_sum_divisible_by_k;
mod subarray_count_sum_to_k;
mod subarray_longest_consecutive;
mod subarray_longest_sum_within_k;
mod subarray_max_area_containable;
mod subarray_max_product;
mod subarray_min_size_sum;
mod subarray_product_except_self;
mod subarray_shortest_remove_to_sort;
mod subarray_total_patch_containable;
mod subsequence_fixed_size_max_min_gap;
mod subsequence_min_jumps;
mod triplet_check_increasing;
mod triplet_count_increasing_sum_within_k;

#[pymodule]
pub mod array {
    use super::*;

    #[pymodule_export]
    use circular_index_cover_cost::can_complete_circuit;
    #[pymodule_export]
    use consecutive_int_missing::missing_number;
    #[pymodule_export]
    use rotated_sorted_array_min::find_min;
    #[pymodule_export]
    use rotated_sorted_array_search::search;
    #[pymodule_export]
    use search_element_peak::find_peak_element;
    #[pymodule_export]
    use search_min_max_diff_with_operation::smallest_range;
    #[pymodule_export]
    use search_two_indexes_sum_to_k::two_sum_k;
    #[pymodule_export]
    use sorted_array_two_indexes_sum_to_k::two_sum;
    #[pymodule_export]
    use stream_sliding_window_maxes::window_maxes;
    #[pymodule_export]
    use subarray_addition_multiple::range_addition;
    #[pymodule_export]
    use subarray_count_sum_divisible_by_k::subarray_div_by_k;
    #[pymodule_export]
    use subarray_count_sum_to_k::subarray_sum;
    #[pymodule_export]
    use subarray_longest_consecutive::longest_consecutive_sequence;
    #[pymodule_export]
    use subarray_longest_sum_within_k::longest_sum_within_k;
    #[pymodule_export]
    use subarray_max_area_containable::max_area;
    #[pymodule_export]
    use subarray_max_product::max_product;
    #[pymodule_export]
    use subarray_min_size_sum::min_sub_array_len;
    #[pymodule_export]
    use subarray_product_except_self::product_except_self;
    #[pymodule_export]
    use subarray_shortest_remove_to_sort::find_shortest_subarray_to_remove;
    #[pymodule_export]
    use subarray_total_patch_containable::total_patch;
    #[pymodule_export]
    use subsequence_fixed_size_max_min_gap::max_min_gap;
    #[pymodule_export]
    use subsequence_min_jumps::min_jump;
    #[pymodule_export]
    use triplet_check_increasing::increasing_triplet;
    #[pymodule_export]
    use triplet_count_increasing_sum_within_k::count_triplets;
}
