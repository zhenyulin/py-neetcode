## Neetcode

> neat Python3 algorithms explained and summarised for selected problems extending [neetcode](https://neetcode.io/practice)

### Int

- **Greedy**

    - [Get Prime Factors](./src/int/get_prime_factors.py)


### String

- **Math Calculation** `O(1) time`
    
    > count combination

    - [Splits Count Equal Num Char](./src/string/splits_count_equal_num_char.py)

- **Greedy** `O(N) time` - *rolling update with condition*
    
    > substring(shortest, longest, len, min, max) -> greedy, sliding window

    - [Substring Longest Palindromic](./src/string/substring_longest_palindromic.py) `palindromic`
    - [Search Min Max Diff After Operation](./src/array/search_min_max_diff_with_operation.py) `all possible cases, sort pair iterate`
    - [Subarray Addition Multiple](./src/array/subarray_addition_multiple.py) `lazy rolling addition`

    - **Hashmap** `O(C) space` - *index/count related condition*
    
        > string(index, count, last, match) -> Hashmap

        - [Substring Longest with Char Replacement](./src/string/substring_longest_char_replacement.py) `{char: count}`
        - [Substring Longest without Repeating Characters](./src/string/substring_longest_without_repeating_characters.py) `{char: last}, seen[c] >= i`
        - [Splits Count Equal Unique Chars](./src/string/splits_count_equal_unique_chars.py) `{char: first}, {char: last}`

- **1D Dynamic Programming** `O(N) time, O(1 or N) space` - *multiple relations to between n-x and n*

    > subsequence, combination(count, match, min, max) -> dynamic programming

    - [Splits Count by Dict](./src/string/splits_count_by_dict.py.) `if match_condition: dp[n] += dp[n-1] or dp[n-2]`
    - [Splits Count Match by Dict](./src/string/splits_count_match_by_dict.py.) `dp[i] = True if any(dp[n-len(w)] and s[i-len(w):i] == w)`
    
- **2D Dynamic Programming** `O(M*N) time, O(M or N or M*N) space` - *multiple relations and multiple strings* 

    > two subsequences, subsequence match -> 2d dynamic programming

    - [Subsequence Count Longest Common of Two Strings](./src/string/subsequence_count_longest_common_two_strings.py.py)
    - [Subsequence Count Match Another String](./src/string/subsequence_count_match_target.py)

- **Backtracking or DFS** `O(N*O^L) time` - *conditional generation or search* 

    > combination(generate) -> backtracking, combination(dictionary) -> DFS

    - [Combination Generate Parentheses](./src/string/combination_generate_parentheses.py)
    - [Combination Dictionary Search Match Sum](./src/string/combination_dictionary_search_match_sum.py)



### 1D Array


- **Math Calculation** `O(1) time`

- **Binary Search** `O(LogN) time` - *search until match or left-right condition* 

    > sorted search, search peak -> binary search
    
    - [Rotated Sorted Array Search](./src/array/rotated_sorted_array_search.py)
    - [Rotated Sorted Array Min](./src/array/rotated_sorted_array_min.py) `target is converged boundary`
    - [Search Element Peak](./src/array/search_element_peak.py) `left on uphill, right on downhill`

    - **Greedy**

        - [Subsequence Fixed Size Max Min Gap](./src/array/subsequence_fixed_size_max_min_gap.py) `binary search on possible gap`

- **Greedy** `O(N) time` - *rolling update on condition* 

    > subarray(max, min, longest, except self) -> greedy

    - [Subarray Max Product](./src/array/subarray_max_product.py) `rolling vals, min, max`
    - [Subarray Min Size Sum](./src/array/subarray_min_size_sum.py) `rolling res, sliding window`
    - [Subarray Longest Consecutive](./src/array/subarray_longest_consecutive.py) `consecutive, set`
    - [Subarray Product Except Self](./src/array/subarray_product_except_self.py) `async except-self product`
    - [Triplet Check Increasing](./src/array/triplet_check_increasing.py) `anchor if elif else`
    
    - **Sliding Window** `O(1) space` - *forward and backward* 

        > subarray(area, remove, longest, shortest) -> sliding window

        - [Subarray Max Containable Area](./src/array/subarray_max_area_containable.py) `shrinking width updating min height`
        - [Subarray Total Patch Containable](./src/array/subarray_total_patch_containable.py) `update the bar on the smaller side`
        - [Subarray Shortest Remove  to Sort](./src/array/subarray_remove_shortest_to_sort.py) `shortest window`
        - [Subarray Longest Sum Within K](./src/array/subarray_longest_sum_within_k.py)
        - [Triplets Count Increasing Sum Within K](./src/array/triplet_count_increasing_sum_within_k.py)
    
    - **Hashmap** `O(N) space` - *index/count related condition* 
    
        > array(index, count, last) -> Hashmap

        - [Search Two Indexes Sum to K](./src/array/search_two_indexes_sum_to_k.py) `{match_condition: index}`
        - [Subarray Count Sum to K](./src/array/subarray_count_sum_to_k.py) `{sum: count}``sum[i:j] = sum[:j] - sum[:i]`
        - [Subarray Count Sum Divisible by K](.src/array/subarray_count_sum_divisible_by_k.py) `{sum%k: count}`

    - **Stack** `O(N) time, O(K) space`

        > stream sliding window max -> stack

    - [Stream Sliding Window Maxes](./src/array/stream_sliding_window_maxes.py) *[index of max until i]*

    - **Heap** `O(K*LogN or N*LogK) time, O(N) space` - *rank, sort* 
    
        > stream k, kth, median -> heap, window max -> stack

        - [Search K Elements Closest to Origin](./src/array/search_k_elements_closest_to_origin.py)
        - [Stream Find Median](./src/array/stream_find_median.py) *min max heaps*
        - [Stream Sliding Window Median](./src/array/stream_sliding_window_median.py) *min max heaps, lazy removal*

    - **Combinations** `O(N^2) time`

        - [(Triplet) Search Three Indexes Sum to K](./array/search_three_indexes_sum_to_k.py) `negative positive combinations`
        

- **1D Dynamic Programming** `O(N) time, O(N or 1) space` - *multiple relations to between n-x and n* 

    > subsequence or combination(fewest, sum to, longest) -> dynamic programming

    - [Combination Count Sum To K](./src/array/combination_count_sum_to_k.py) `dp[i] += dp[i-coin]`
    - [Subsequence Longest Increasing](./src/array/subsequence_longest_increasing.py.) `dp[j] = max(dp[i]+1 if nums[i] < nums[j])`
    - [Two Arrays Min Path Cost](./src/array/two_arrays_min_path_cost.py) `from_red, from_blue dp`

    - **Cached DFS**

        - [Combination Fewest Elements Sum to K](./src/array/combination_generate_sum_to_k.py) `dp[a] = min(dp[a], 1 + dp[a - c])`

- **2D Dynamic Programming**

    > subsequence(average)

    - [Subsequence Search Equal Average](./src/array/subsequence_search_equal_average.py) `dp[i] |= {s+a for s in dp[i+1] if s+a <= HALF}`

- **Backtracking, DFS** `O(N*O^L) time` - conditional combinations 

    > combination(generate) -> backtracking

    - [Combination Generate Sum to K](./src/array/combination_generate_sum_to_k.py)


### 2D Array

- **Binary Search** `O(LogM*LogN) time`

    > sorted search, search peak -> binary search

    - [Sorted Matrix Search](./src/array_2d/sorted_matrix_search.py)
    - [Search Element Peak](./src/array_2d/search_element_peak.py)

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

`n << 1 # n * 2` `n >> 1 # n // 2` `n & 1 # n % 2`

- **Bit Iteration, Shift** `O(1) time`

    > range(32) or range(31, -1, -1)

    - [Reverse Bits](./src/bit/reverse_bits.py)
    - [Bitwise AND non zero](./src/bit/bitwise_and_non_zero.py)
    - [Divide by Deduction](./src/bit/divide_by_deduction.py)
    - [Min Operation to Zero](./src/bit/min_operation_to_zero.py)

- **As an Array**

    > bit base(conversion, calculation)

    - [Add Negative Binary](./src/bit/add_nega_binary.py)
    - [Convert to Negative Base](./src/bit/convert_to_neg_base.py)


### Tree

- **Recursion** `O(N) time, O(N) space`

    - [Binary Search Tree Validate](./src/tree/bst_validate.py)

- **BFS** `O(N) time, O(N) space`

    - [Search Rightest Nodes](./src/tree/search_rightest_nodes.py)

- **DFS**


### Linked List

- **Two Pointers** `O(N) time, O(1) space`

    - [Reorder List Two Sides](./src/linked_list/reorder_list_two_sides.py)
    - Cycle Detection
    - Overlapping Point

### Graph

- **Topological Sort**
- **DSU** `O(Q) time` `{node: anchor/root}`

    - [Stream Largest Group](./src/graph/stream_largest_group.py)

- **DFS** `O(N^2) time` `{node: [connection]}`

    - [Count Groups](./src/graph/count_groups.py)



### Geometry

- **Triangle**

    - [Check Point in Triangle](./src/geometry/check_point_in_triangle.py)


### Data Structure Implementations

- [HashMap](./src/structure/hashmap.py)
- [Set](./src/structure/set.py)
- [Deque](./src/structure/deque.py)
- [Heap](./src/structure/heap.py)
- [LRU Cache](./src/structure/cache_lru.py)
- [MRU Cache](./src/structure/cache_mru.py)
- [LFU Cache](./src/structure/cache_lfu.py)
