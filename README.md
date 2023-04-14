## Neetcode

> neat Python3 algorithms explained and summarised for selected problems extending [neetcode](https://neetcode.io/practice)

### String

- **Math Calculation** `O(1) time`
    
    > count combination

    - [Substring Count Equal One Split](./src/string/substring_count_equal_one_split.py)

- **Greedy** `O(N) time` - *rolling update with condition*
    
    > substring(shortest, longest, len, min, max) -> greedy, sliding window

    - [Substring Longest Palindromic](./src/string/substring_longest_palindromic.py) `palindromic`

    - **Hashmap** `O(C) space` - *index/count related condition*
    
        > string(index, count, last, match) -> Hashmap

        - [Substring Longest with Char Replacement](./src/string/substring_longest_char_replacement.py) `{char: count}`
        - [Substring Longest without Repeating Characters](./src/string/substring_longest_without_repeating_characters.py) `{char: last}, seen[c] >= i`
        - [Substring Count Equal Unique Chars Split](./src/string/substring_count_equal_unique_chars_split.py) `{char: first}, {char: last}`

- **1D Dynamic Programming** `O(N) time, O(1 or N) space` - *multiple relations to between n-x and n*

    > subsequence, combination(count, match, min, max) -> dynamic programming

    - [Combination Count by Dict](./src/string/combination_count_by_dict.py.) `if match_condition: dp[n] += dp[n-1] or dp[n-2]`
    - [Combination Count Match by Dict](./src/string/combination_count_match_by_dict.py.) `dp[i] = True if any(dp[n-len(w)] and s[i-len(w):i] == w)`
    
- **2D Dynamic Programming** `O(M*N) time, O(M or N or M*N) space` - *multiple relations and multiple strings* 

    > two subsequences, subsequence match -> 2d dynamic programming

    - [Subsequence Count Longest Common of Two Strings](./src/string/subsequence_count_longest_common_two_strings.py.py)
    - [Subsequence Count Match Another String](./src/string/subsequence_count_match_target.py)

- **Backtracking or DFS** `O(N*O^L) time` - *conditional generation or search* 

    > combination(generate) -> backtracking

    - [Combination Generate Parentheses](./src/string/combination_generate_parentheses.py)



### 1D Array


- **Math Calculation** `O(1) time`

- **Binary Search** `O(LogN) time` - *search until match or left-right condition* 

    > sorted search, search peak -> binary search
    
    - [Rotated Sorted Array Search](./src/array/rotated_sorted_array_search.py)
    - [Rotated Sorted Array Min](./src/array/rotated_sorted_array_min.py) `target is converged boundary`
    - [Search Element Peak](./src/array/search_element_peak.py) `left on uphill, right on downhill`

- **Greedy** `O(N) time` - *rolling update on condition* 

    > subarray(longest, min, max, area, sum) -> greedy, sliding window

    - [Subarray Max Product](./src/array/subarray_max_product.py) `rolling vals, min, max`
    - [Subarray Min Size Sum](./src/array/subarray_min_size_sum.py) `rolling res, sliding window`
    - [Subarray Longest Consecutive](./src/array/subarray_longest_consecutive.py) `consecutive, set`
    
    - **Sliding Window** `O(1) space` - *forward and backward* 

        - [Except Self Product](./src/array/except_self_product.py) `async except-self product`
        - [Window with Max Area](./src/array/window_max_area.py) `shrinking width updating min height`
        - [Subarray Remove Shortest to Sort](./src/array/subarray_remove_shortest_to_sort.py) `shortest window`
    
    - **Hashmap** `O(N) space` - *index/count related condition* 
    
        > array(index, count, last) -> Hashmap

        - [Elements Indexes Sum](./src/array/elements_index_sum.py) `{match_condition: index}`
        - [Subarray Count Sum to K](./src/array/subarray_count_sum_to_k.py) `{sum: count}``sum[i:j] = sum[:j] - sum[:i]`

    - **Heap or Stack** `O(N) time, O(N) space` - *rank, sort* 
    
        > k, kth -> heap

        - [Find K Elements Closest to Origin](./src/array/find_k_elements_closest_to_origin.py)
        - [Stream Find Median](./src/array/stream_find_median.py) *min max heaps*
        

- **1D Dynamic Programming** `O(N) time, O(N) space` - *multiple relations to between n-x and n* 

    > subsequence or combination(fewest, sum to, longest) -> dynamic programming

    - [Combination Fewest Elements Sum to](./src/array/combination_fewest_elements_sum_to.py) `dp[a] = min(dp[a], 1 + dp[a - c])`
    - [Subsequence Longest Increasing](./src/array/subsequence_longest_increasing.py.) `dp[j] = max(dp[i]+1 if nums[i] < nums[j])`

- **2D Dynamic Programming**

    > subsequence(average)

    - [Subsequence Search Equal Average](./src/array/subsequence_search_equal_average.py) `dp[i] |= {s+a for s in dp[i+1] if s+a <= HALF}`

- **Backtracking, Recursion, DFS** `O(N*O^L) time` - conditional combinations 

    > combination(generate) -> backtracking

    - [Combination Generate Sum to](./src/array/combination_generate_sum_to.py)


### 2D Array

- **Binary Search** `O(LogM*LogN) time`

    > sorted search -> binary search

    - [Sorted Matrix Search](./src/array_2d/sorted_matrix_search.py)

- **Search with Memory** `O(M*N) time, O(1) space`

    - [Validate Soduku](./src/array_2d/validate_soduku.py)

- **BFS** `O(M*N) time, O(M*N) space` - *shortest path* 

    > shortest path -> BFS

    - [Search Length Shortest Path](./src/array_2d/search_length_shortest_path.py)
    - [Search Update Shortest Distance](./src/array_2d/search_update_shortest_distance.py.py)

- **2D Dynamic Programming or cached DFS** `O(M*N) time, O(M*N) space`

    > count longest path

    - [Search Longest Path Increasing](./src/array_2d/search_longest_path_increasing.py)

- **DFS** `O(M*N*O^L) time, O(O^L) space` - *known target* 

    > target, longest path -> DFS

    - [Search Word](./src/array_2d/search_word.py)


### Bit Manipulation

`n << 1 ~ n * 2` `n >> 1 ~ n // 2` `n & 1 ~ n % 2`

- **Bit Iteration** `O(1) time O(1) space`

    - [Reverse Bits](./src/bit/reverse_bits.py)
    - [Bitwise AND non zero](./src/bit/bitwise_and_non_zero.py)

- **Bit Base Calculation**

    - [Add Negative Binary](./src/bit/add_nega_binary.py)
    - [Convert to Negative Base](./src/bit/convert_to_neg_base.py)

- **Bit Flip**

    - [Min Operation to Zero](./src/bit/min_operation_to_zero.py)

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
