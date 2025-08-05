use pyo3::prelude::*;

mod combination_generate_parentheses;
mod combination_validate_parentheses;
mod group_anagrams;
mod split_count_equal_num_char;
mod splits_char_unique_part;
mod splits_count_by_dict;
mod splits_count_equal_unique_chars;
mod splits_count_match_by_dict;
mod subsequence_count_longest_common_two_strings;
mod subsequence_count_match_target;
mod substring_check_target_anagram;
mod substring_longest_char_replacement;
mod substring_longest_palindrome;
mod substring_longest_without_repeating_characters;

#[pymodule]
pub mod string {
    use super::*;

    #[pymodule_export]
    use combination_generate_parentheses::generate_parentheses;
    #[pymodule_export]
    use combination_validate_parentheses::validate_parenthesis;
    #[pymodule_export]
    use group_anagrams::group_anagrams as group_anagrams_py;
    #[pymodule_export]
    use split_count_equal_num_char::num_ways;
    #[pymodule_export]
    use splits_char_unique_part::partition_lengths;
    #[pymodule_export]
    use splits_count_by_dict::ways_of_decoding;
    #[pymodule_export]
    use splits_count_equal_unique_chars::num_splits;
    #[pymodule_export]
    use splits_count_match_by_dict::word_break;
    #[pymodule_export]
    use subsequence_count_longest_common_two_strings::longest_common_subsequence;
    #[pymodule_export]
    use subsequence_count_match_target::num_match_subsequences;
    #[pymodule_export]
    use substring_check_target_anagram::check_inclusion;
    #[pymodule_export]
    use substring_longest_char_replacement::char_replacement;
    #[pymodule_export]
    use substring_longest_palindrome::longest_palindrome;
    #[pymodule_export]
    use substring_longest_without_repeating_characters::length_of_longest_substring;
}
