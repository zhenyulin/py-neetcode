use pyo3::prelude::*;

mod rotated_sorted_array_min;
mod rotated_sorted_array_search;
mod search_element_peak;
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
    use subsequence_fixed_size_max_min_gap::max_min_gap;
}
