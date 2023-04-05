## Neetcode

> neat Python3 solutions explained for selected problems extending [neetcode](https://neetcode.io/practice)

### String

- **Greedy** - *rolling update with condition*

    * [Substring Longest Palindromic](./src/string/substring_longest_palindromic.py) *'palindromic'*

    - **Hashmap** - *index related condition*
    - **Sliding Window** - *substring with condition*

        * [Substring Longest without Repeating Characters](./src/string/substring_longest_without_repeating_characters.py) *{char: index (last seen)}*
        * [Substring Longest with Char Replacement](./src/string/substring_longest_char_replacement.py) *{char: count}*

- **Backtracking, Recursion, DFS** - conditional combinations

    - [Combination Generate Parentheses](./src/string/combination_generate_parentheses.py)

- **Dynamic Programming** - *multiple ways or relations to between n-2 or n-1 and n*

    - [Combination Count by Dict](./src/string/combination_count_by_dict.py.) *if match: += dp[n-1] or dp[n-2]*
    - [Combination Match by Dict](./src/string/combination_match_by_dict.py.) *dp[i] if any(dp[n-len(w)] and s[i-len(w):i] == w)*

### 1D Array

- **Greedy** - *rolling update on condition*

    - [Subarray Max Product](./src/array/subarray_max_product.py) *rolling vals, min, max*
    - [Subarray Min Size Sum](./src/array/subarray_min_size_sum.py) *rolling res, sliding window*
    * [Subarray Longest Consecutive](./src/array/subarray_longest_consecutive.py) *consecutive, set*

- **Two Way Iteration** - *forward and backward, can be combined with **Greedy***

    - [Except Self Product](./src/array/except_self_product.py) *decouple prefix/suffix product*
    - [Window with Max Area](./src/array/window_max_area.py) *shrinking width with max min*

- **Hashmap** - *index related condition*

    * [Elements Indexes Sum](./src/array/elements_index_sum.py) *{match: index}*

- **Binary Search** - *search in sorted sequence with target condition*
    
    * [Rotated Sorted Array Min](./src/array/rotated_sorted_array_min.py) *target is converged boundary*
    * [Rotated Sorted Array Search](./src/array/rotated_sorted_array_search.py)

- **Backtracking, Recursion, DFS** - conditional combinations

    - [Combination Generate to Sum](./src/array/combination_generate_to_sum.py)

- **Dynamic Programming** - *multiple ways or relations to between n-2 or n-1 and n*

    - [Combination Fewest Elements Sum](./src/array/combination_fewest_elements_sum.py) *dp[a] = min(dp[a], 1 + dp[a - c])*
    - [Subsequence Longest Increasing](./src/array/subsequence_longest_increasing.py.) *dp[j] = max(dp[i]+1 if nums[i] < nums[j])*

- **Prefix/Suffix Array** - *sum of subarray*

- **Heap or Stack**


### 2D Array

- **BFS**

- **DFS**

    - [Search Word](./src/array/search_word.py)

- **Dynamic Programming**

- **Binary Search**

    - [Sorted Matrix Search](./src/array_2d/sorted_matrix_search.py)

- **Search with Memory**

    - [Validate Soduku](./src/array_2d/validate_soduku.py)


### Tree

- **BFS**

- **DFS**

- **Recursive**


### Linked List

- **Two Pointers**

    * Cycle Detection
    * Overlapping Point

### Graph

- **Topological Sort**

### Bit Manipulation
