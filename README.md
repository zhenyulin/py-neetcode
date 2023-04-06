## Neetcode

> neat Python3 algorithms explained and summarised for selected problems extending [neetcode](https://neetcode.io/practice)

### String

- **Greedy** - *rolling update with condition* `O(N) time`

    > substring(shortest, longest, len, min, max) -> greedy, sliding window

    - [Substring Longest Palindromic](./src/string/substring_longest_palindromic.py) `palindromic`

    - **Hashmap** - *index/count related condition* `O(N) space`, **Sliding Window** - *substring with condition*
    
        > string(index, count, last, match) -> Hashmap

        - [Substring Longest without Repeating Characters](./src/string/substring_longest_without_repeating_characters.py) `{char: index (last seen)}`
        - [Substring Longest with Char Replacement](./src/string/substring_longest_char_replacement.py) `{char: count}`

- **1D Dynamic Programming** - *multiple relations to between n-x and n, combination count* `O(N) time, O(1 or N) space`

    > subsequence, combination(count, match, min, max) -> dynamic programming

    - [Combination Count by Dict](./src/string/combination_count_by_dict.py.) `if match_condition: dp[n] += dp[n-1] or dp[n-2]`
    - [Combination Count Match by Dict](./src/string/combination_count_match_by_dict.py.) `dp[i] = True if any(dp[n-len(w)] and s[i-len(w):i] == w)`
    
- **2D Dynamic Programming** - *multiple relations and multiple strings* `O(M*N) time, O(1 or M*N) space`

    > two subsequences -> 2d dynamic programming

    - [Two Strings Subsequence Longest Common](./src/string/two_strings_subsequence_longest_common.py)

- **Backtracking or DFS** - *conditional generation or search* `O(N*O^L) time`

    > combination(generate) -> backtracking

    - [Combination Generate Parentheses](./src/string/combination_generate_parentheses.py)



### 1D Array


- **Math Calculation** - `O(1) time`

- **Binary Search** - *search in sorted sequence with target condition* `O(LogN) time`

    > sorted search -> binary search
    
    - [Rotated Sorted Array Min](./src/array/rotated_sorted_array_min.py) `target is converged boundary`
    - [Rotated Sorted Array Search](./src/array/rotated_sorted_array_search.py)

- **Greedy** - *rolling update on condition* `O(N) time`

    > subarray(longest, min, max, area, sum) -> greedy, sliding window

    - [Subarray Max Product](./src/array/subarray_max_product.py) `rolling vals, min, max`
    - [Subarray Min Size Sum](./src/array/subarray_min_size_sum.py) `rolling res, sliding window`
    - [Subarray Longest Consecutive](./src/array/subarray_longest_consecutive.py) `consecutive, set`
    
    - **Sliding Window** - *forward and backward* `O(1) space`

        - [Except Self Product](./src/array/except_self_product.py) `async except-self product`
        - [Window with Max Area](./src/array/window_max_area.py) `shrinking width updating min height`
    
    - **Hashmap** - *index/count related condition* `O(N) space`
    
        > array(index, count, last) -> Hashmap

        - [Elements Indexes Sum](./src/array/elements_index_sum.py) `{match_condition: index}`
        - [Subarray Count Sum to K](./src/array/subarray_count_sum_to_k.py) `{sum: count}``sum[i:j] = sum[:j] - sum[:i]`

    - **Heap or Stack** - *rank, sort* `O(N) time, O(N) space`
    
        > k, kth -> heap

        - [Find K Elements Closest to Origin](./src/array/find_k_elements_closest_to_origin.py)
        - [Stream Find Median](./src/array/stream_find_median.py) *min max heaps*
        

- **1D Dynamic Programming** - *multiple relations to between n-x and n* `O(N) time, O(N) space`

    > subsequence or combination(fewest, sum to, longest) -> dynamic programming

    - [Combination Fewest Elements Sum to](./src/array/combination_fewest_elements_sum_to.py) `dp[a] = min(dp[a], 1 + dp[a - c])`
    - [Subsequence Longest Increasing](./src/array/subsequence_longest_increasing.py.) `dp[j] = max(dp[i]+1 if nums[i] < nums[j])`

- **2D Dynamic Programming** - **

- **Backtracking, Recursion, DFS** - conditional combinations `O(N*O^L) time`

    > combination(generate) -> backtracking

    - [Combination Generate Sum to](./src/array/combination_generate_sum_to.py)


### 2D Array

- **Search with Memory**

    - [Validate Soduku](./src/array_2d/validate_soduku.py)

- **Binary Search** `O(LogM*LogN) time`

    > sorted search -> binary search

    - [Sorted Matrix Search](./src/array_2d/sorted_matrix_search.py)

- **BFS** - *shortest path* `O(M*N) time, O(M*N) space`

    > shortest length -> BFS

    - [Search Length Shortest Path](./src/array_2d/search_length_shortest_path.py)

- **DFS** - *known target* `O(M*N*O^L) time, O(O^L) space`

    > longest length, target -> DFS

    - [Search Word](./src/array_2d/search_word.py)

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
