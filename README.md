# Py-Neetcode

> algorithm cheat sheet in Python summarised by data types

## Data Structure Implementations

- [HashMap](./src/structure/hashmap.py)
- [Set](./src/structure/set.py)
- [Deque](./src/structure/deque.py)
- [Heap](./src/structure/heap.py)
- [LRU Cache](./src/structure/cache_lru.py)
- [MRU Cache](./src/structure/cache_mru.py)
- [LFU Cache](./src/structure/cache_lfu.py)
- [Priority Cache](./src/structure/cache_priority.py)
- [Message Queue Scheduled](./src/structure/message_queue_scheduled.py)
- [Rate Limiter](./src/structure/rate_limiter.py)

## Algorithms by Data Structure

### Int

#### Greedy

- [Get Prime Factors](./src/int/get_prime_factors.py)

---

### String

#### Math Calculation `O(1) time`

> count combination

- [Splits Count Equal Num Char](./src/string/splits_count_equal_num_char.py)

#### Greedy `O(N) time` - _rolling update with condition_

> substring(shortest, longest, len, min, max) -> greedy, sliding window

- [Substring Longest Palindromic](./src/string/substring_longest_palindromic.py) `palindromic`
- [Combination Validate Parentheses](./src/string/combination_validate_parentheses.py) `left_min, left_max`

#### Greedy & Hashmap `O(C) space` - _index/count related condition_

> string(index, count, last, match) -> Hashmap

- [Group by Anagram](./src/string/group_by_anagram.py) `{sorted_string: list}`
- [Substring Longest with Char Replacement](./src/string/substring_longest_char_replacement.py) `{char: count}`
- [Substring Longest without Repeating Characters](./src/string/substring_longest_without_repeating_characters.py) `{char: last}, seen[c] >= i`
- [Substring Check Target Anagram](./src/string/substring_check_target_anagram.py) `{char: count}`
- [Splits Count Equal Unique Chars](./src/string/splits_count_equal_unique_chars.py) `{char: first}, {char: last}`
- [Splits Char Unique Part](./src/string/splits_char_unique_part.py) `{char: last}`

### 1D Dynamic Programming `O(N) time, O(1 or N) space` - _multiple relations to between n-x and n_

> subsequence, combination(count, match, min, max) -> dynamic programming

- [Splits Count by Dict](./src/string/splits_count_by_dict.py.) `if match_condition: dp[n] += dp[n-1] or dp[n-2]`
- [Splits Count Match by Dict](./src/string/splits_count_match_by_dict.py.) `dp[i] = True if any(dp[n-len(w)] and s[i-len(w):i] == w)`

#### 2D Dynamic Programming `O(M*N) time, O(M or N or M*N) space` - _multiple relations and multiple strings_

> two subsequences, subsequence match -> 2d dynamic programming

- [Subsequence Count Longest Common of Two Strings](./src/string/subsequence_count_longest_common_two_strings.py.py)
- [Subsequence Count Match Another String](./src/string/subsequence_count_match_target.py)

#### Backtracking or DFS `O(N*O^L) time` - _conditional generation or search_

> combination(generate) -> backtracking, combination(dictionary) -> DFS

- [Combination Generate Parentheses](./src/string/combination_generate_parentheses.py)
- [Combination Dictionary Search Match Sum](./src/string/combination_dictionary_search_match_sum.py)

---

### 1D Array

#### Binary Search `O(LogN) time` - _search until match or left-right condition_

> sorted search, search peak -> binary search

- [Rotated Sorted Array Search](./src/array/rotated_sorted_array_search.py)
- [Rotated Sorted Array Min](./src/array/rotated_sorted_array_min.py) `target is converged boundary`
- [Search Element Peak](./src/array/search_element_peak.py) `left on uphill, right on downhill`

#### Binary Search + Greedy

- [Subsequence Fixed Size Max Min Gap](./src/array/subsequence_fixed_size_max_min_gap.py) `binary search on possible gap`

#### Greedy `O(N) time` - _rolling update on condition_

> subarray(max, min, longest, except self) -> greedy

- [Subarray Max Product](./src/array/subarray_max_product.py) `rolling vals, min, max`
- [Subarray Min Size Sum](./src/array/subarray_min_size_sum.py) `rolling res, sliding window`
- [Search Min Max Diff After Operation](./src/array/search_min_max_diff_with_operation.py) `all possible cases, sort pair iterate`
- [Subarray Longest Consecutive](./src/array/subarray_longest_consecutive.py) `consecutive, set`
- [Subarray Product Except Self](./src/array/subarray_product_except_self.py) `async except-self product`
- [Subarray Addition Multiple](./src/array/subarray_addition_multiple.py) `lazy rolling addition`
- [Consecutive Int Missing](./src/array/consecutive_int_missing.py) `sum diff`
- [Triplet Check Increasing](./src/array/triplet_check_increasing.py) `anchor if elif else`
- [Circular Index Cover Cost](./src/array/circular_index_cover_cost.py)

#### Greedy + Sliding/Two-Pointer Window `O(1) space` - _forward and backward_

> subarray(area, remove, longest, shortest) -> sliding window

- [Subarray Max Containable Area](./src/array/subarray_max_area_containable.py) `shrinking width updating min height`
- [Subarray Total Patch Containable](./src/array/subarray_total_patch_containable.py) `update the bar on the smaller side`
- [Subarray Shortest Remove to Sort](./src/array/subarray_shortest_remove_to_sort.py) `shortest window`
- [Subarray Longest Sum Within K](./src/array/subarray_longest_sum_within_k.py)
- [Triplets Count Increasing Sum Within K](./src/array/triplet_count_increasing_sum_within_k.py)
- [Sorted Array Two Indexes Sum to K](./src/array/sorted_array_two_indexes_sum_to_k.py)

#### Greedy + Implicit BFS

- [Subsequence Min Jumps](./src/array/subsequence_min_jumps.py)

#### Greedy & Hashmap `O(N) space` - _index/count related condition_

> array(index, count, last) -> Hashmap

- [Search Two Indexes Sum to K](./src/array/search_two_indexes_sum_to_k.py) `{match_condition: index}`
- [Subarray Count Sum to K](./src/array/subarray_count_sum_to_k.py) ` {sum: count}``sum[i:j] = sum[:j] - sum[:i] `
- [Subarray Count Sum Divisible by K](./src/array/subarray_count_sum_divisible_by_k.py) `{sum%k: count}`

#### Greedy & Stack `O(N) time, O(K) space`

> stream sliding window max, rectangle area -> stack

- [Stream Sliding Window Maxes](./src/array/stream_sliding_window_maxes.py) _[index of max until i]_
- [Subarray Max Area Rectangle](./src/array/subarray_max_area_rectangle.py) `[(left, height)]`

#### Greedy & Heap `O(K*LogN or N*LogK) time, O(N) space` - _rank, sort_

> stream k, kth, median, subgroups consecutive -> heap

- [Search K Elements Closest to Origin](./src/array/search_k_elements_closest_to_origin.py)
- [Stream Find Median](./src/array/stream_find_median_element.py) _min max heaps_
- [Stream Sliding Window Median](./src/array/stream_sliding_window_median.py) _min max heaps, lazy removal_
- [Subgroups Fixed Size Check Consecutive](./src/array/subgroups_fixed_size_check_consecutive.py)

#### Greedy & Combinations `O(N^2) time`

- [(Triplet) Search Three Indexes Sum to K](./array/search_three_indexes_sum_to_k.py) `negative positive combinations`

#### 1D Dynamic Programming `O(N) time, O(N or 1) space` - _multiple relations to between n-x and n_

> subsequence or combination(fewest, sum to, longest) -> dynamic programming

- [Combination Count Sum To K](./src/array/combination_count_sum_to_k.py) `dp[i] += dp[i-coin]`
- [Subsequence Longest Increasing](./src/array/subsequence_longest_increasing.py.) `dp[j] = max(dp[i]+1 if nums[i] < nums[j])`
- [Two Arrays Min Path Cost](./src/array/two_arrays_min_path_cost.py) `from_red, from_blue dp`

#### 1D Dynamic Programming + Cached DFS

- [Combination Fewest Elements Sum to K](./src/array/combination_generate_sum_to_k.py) `dp[a] = min(dp[a], 1 + dp[a - c])`

#### 2D Dynamic Programming

> subsequence(average)

- [Subsequence Search Equal Average](./src/array/subsequence_search_equal_average.py) `dp[i] |= {s+a for s in dp[i+1] if s+a <= HALF}`

#### Backtracking, DFS `O(N*O^L) time` - conditional combinations

> combination(generate) -> backtracking

- [Combination Generate Sum to K](./src/array/combination_generate_sum_to_k.py)

---

### 2D Array

#### Binary Search `O(LogM*LogN) time`

> sorted search, search peak -> binary search

- [Sorted Matrix Search](./src/array_2d/sorted_matrix_search.py)
- [Search Element Peak](./src/array_2d/search_element_peak.py)

#### Greedy & Set `O(M*N) time, O(1) space`

- [Validate Soduku](./src/array_2d/validate_soduku.py)

#### BFS `O(M*N) time, O(M*N) space` - _shortest path_

> shortest path, shortest distance, edge areas -> BFS

- [Search Shortest Path](./src/array_2d/search_shortest_path.py)
- [Search Shortest Spread](./src/array_2d/search_shortest_spread.py)
- [Update Shortest Distance](./src/array_2d/update_by_shortest_distance.py)
- [Update by Area Surrounded](./src/array_ed/update_by_area_surrounded.py)

#### 2D Dynamic Programming or cached DFS `O(M*N) time, O(M*N) space`

> count longest path

- [Search Longest Path Increasing](./src/array_2d/search_longest_path_increasing.py)

#### DFS `O(M*N or M*N*O^L) time, O(O^L) space` - _known target_

> longest path, target sequence, edge areas -> DFS

- [Search Longest Path](./src/array_2d/search_longest_path.py)
- [Search Sequence](./src/array_2d/search_sequence.py)
- [Update by Area Surrounded](./src/array_ed/update_by_area_surrounded.py)

---

### Bit

`n << 1 <=> n * 2` `n >> 1 <=> n // 2` `n & 1 <=> n % 2`

#### Bit Iteration, Shift `O(1) time`

> range(32) or range(31, -1, -1)

- [Reverse Bits](./src/bit/reverse_bits.py)
- [Bitwise AND non zero](./src/bit/bitwise_and_non_zero.py)
- [Divide by Deduction](./src/bit/divide_by_deduction.py)
- [Min Operation to Zero](./src/bit/min_operation_to_zero.py)

#### As an Array

> bit base(conversion, calculation)

- [Add Negative Binary](./src/bit/add_nega_binary.py)
- [Convert to Negative Base](./src/bit/convert_to_neg_base.py)

---

### Tree

#### Recursion `O(N) time, O(N) space`

- [Invert](./src/tree/invert.py)
- [Binary Search Tree Validate](./src/tree/bst_validate.py)

#### BFS `O(N) time, O(N) space`

- [Search Rightmost Nodes](./src/tree/search_rightmost_nodes.py)

#### DFS or Backtracking `O(N) time, O(N) space`

- [Path Sum Max](./src/tree/path_sum_max.py)

---

### Linked List

#### Simple Forward `O(N) time, O(1) space`

- [Reverse](./src/linked_list/reverse.py)
- [Add Two Numbers](./src/linked_list/add_two_numbers.py)

#### Fast Slow Pointers `O(N) time, O(1) space`

- [Reorder from Mid Point](./src/linked_list/reorder_from_midpoint.py)
- [Cycle Detection](./src/linked_list/detect_cycle.py)

---

### Graph

#### DSU(Root Union) `O(C) time, O(N) space` `{node: root}`

> undirected set

- [Undirected Stream Largest Set](./src/graph/undirected_stream_largest_set.py.py)
- [Undirected Remove Cycle](./src/graph/undirected_remove_cycle.py)

#### Topological Sort `O(C) time, O(C+N) space` `{up: [downs]}, [up_counts]`

> directed cycle, paths

- [Directed Detect Cycle](./src/graph/directed_detect_cycle.py)
- [Directed Search Paths All Nodes](./src/graph/directed_search_pathes_all_nodes.py)

#### DFS `O(N^2) time` `{node: [connection]}`

> matrix count groups

- [(Undirected) Matrix Count Groups](./src/graph/matrix_count_groups.py)

---

### Geometry

#### Triangle

- [Check Point in Triangle](./src/geometry/check_point_in_triangle.py)
