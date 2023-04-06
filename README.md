## Neetcode

> neat Python3 solutions explained for selected problems extending [neetcode](https://neetcode.io/practice)

### String

`len, count, index, last, match`

- **Greedy** - *rolling update with condition* `O(N) time`

    - [Substring Longest Palindromic](./src/string/substring_longest_palindromic.py) `palindromic`

    - **Hashmap** - *index/count related condition* `O(N) space`, **Sliding Window** - *substring with condition*

        * [Substring Longest without Repeating Characters](./src/string/substring_longest_without_repeating_characters.py) `{char: index (last seen)}`
        * [Substring Longest with Char Replacement](./src/string/substring_longest_char_replacement.py) `{char: count}`

- **1D Dynamic Programming** - *multiple relations to between n-x and n* `O(N) time, O(N) space`

    - [Combination Count by Dict](./src/string/combination_count_by_dict.py.) `if match_condition: dp[n] += dp[n-1] or dp[n-2]`
    - [Combination Match by Dict](./src/string/combination_match_by_dict.py.) `dp[i] = True if any(dp[n-len(w)] and s[i-len(w):i] == w)`

- **2D Dynamic Programming** - *multiple relations and multiple strings* `O(N^2) time O(N^2) space`

- **Backtracking or DFS** - *conditional combinations or search* `O(N*O^L) time`

    - [Combination Generate Parentheses](./src/string/combination_generate_parentheses.py)

### 1D Array

`min, max, vals, match, count, length, area, sum, product, consecutive, increasing`

- **Math Calculation** - `O(1) time`

- **Binary Search** - *search in sorted sequence with target condition* `O(LogN) time`
    
    - [Rotated Sorted Array Min](./src/array/rotated_sorted_array_min.py) `target is converged boundary`
    - [Rotated Sorted Array Search](./src/array/rotated_sorted_array_search.py)

- **Heap or Stack** - *rank, sort* `O(N) time, O(N) space`

    - [Find K Elements Closest to Origin](./src/array/find_k_elements_closest_to_origin.py)
    - [Stream Find Median](./src/array/stream_find_median.py) *min max heaps*

- **Greedy** - *rolling update on condition* `O(N) time`

    - [Subarray Max Product](./src/array/subarray_max_product.py) `rolling vals, min, max`
    - [Subarray Min Size Sum](./src/array/subarray_min_size_sum.py) `rolling res, sliding window`
    - [Subarray Longest Consecutive](./src/array/subarray_longest_consecutive.py) `consecutive, set`

    - **Sliding Window** - *subarray shriking*
        - [Window with Max Area](./src/array/window_max_area.py) `shrinking width updating min height`

    - **Prefix Sum Hashmap or Array** - `sum[i:j] = sum[:j] - sum[:i]` `O(N) space`

        - [Subarray Count Sum to K](./src/array/subarray_count_sum_to_k.py) `{sum: count}`

- **Hashmap** - *index/count related condition* `O(N) space`

    - [Elements Indexes Sum](./src/array/elements_index_sum.py) `{match_condition: index}`

- **Two Way Iteration** - *forward and backward*

    - [Except Self Product](./src/array/except_self_product.py) `async except-self product`

- **1D Dynamic Programming** - *multiple relations to between n-x and n* `O(N) time, O(N) space`

    - [Combination Fewest Elements Sum](./src/array/combination_fewest_elements_sum.py) `dp[a] = min(dp[a], 1 + dp[a - c])`
    - [Subsequence Longest Increasing](./src/array/subsequence_longest_increasing.py.) `dp[j] = max(dp[i]+1 if nums[i] < nums[j])`

- **Backtracking, Recursion, DFS** - conditional combinations `O(N*O^L) time`

    - [Combination Generate to Sum](./src/array/combination_generate_to_sum.py)


### 2D Array

`path, length, target`

- **BFS** - *shortest path* `O(M*N) time, O(M*N) space`

    - [Search Length Shortest Path](./src/array_2d/search_length_shortest_path.py)

- **DFS** - *known target* `O(M*N*O^L) time, O(O^L) space`

    - [Search Word](./src/array_2d/search_word.py)

- **Binary Search** `O(LogM*LogN) time`

    - [Sorted Matrix Search](./src/array_2d/sorted_matrix_search.py)

- **Search with Memory**

    - [Validate Soduku](./src/array_2d/validate_soduku.py)

- **2D Dynamic Programming**


### Tree

- **BFS**

    - [Search Rightest Nodes](./src/tree/search_rightest_nodes.py)

- **DFS**

- **Recursive**


### Linked List

- **Two Pointers**

    - Cycle Detection
    - Overlapping Point

### Graph

- **Topological Sort**

### Bit Manipulation
