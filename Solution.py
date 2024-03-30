Questions:

1. Implement a function that checks whether a given string is a palindrome or not.

fn is_palindrome(s: &str) -> bool {
    let s = s.to_lowercase(); // Convert string to lowercase for case insensitivity
    let s = s.chars().filter(|c| c.is_alphanumeric()).collect::<String>(); // Filter out non-alphanumeric characters
    s.chars().eq(s.chars().rev()) // Check if the string is equal to its reverse
}

fn main() {
    // Test examples
    println!("{}", is_palindrome("A man, a plan, a canal, Panama")); // true
    println!("{}", is_palindrome("racecar")); // true
    println!("{}", is_palindrome("hello")); // false
}

2. Given a sorted array of integers, implement a function that returns the index of the first occurrence of a given number.

fn first_occurrence(arr: &[i32], target: i32) -> Option<usize> {
    arr.iter().position(|&x| x == target)
}

fn main() {
    let arr = vec![1, 2, 2, 3, 4, 4, 4, 5, 6];
    let target = 4;
    match first_occurrence(&arr, target) {
        Some(index) => println!("First occurrence of {} is at index {}", target, index),
        None => println!("{} is not found in the array", target),
    }
}

3. Given a string of words, implement a function that returns the shortest word in the string.

fn shortest_word(s: &str) -> &str {
    s.split_whitespace().min_by_key(|word| word.len()).unwrap_or("")
}

fn main() {
    let sentence = "The quick brown fox jumps over the lazy dog";
    println!("Shortest word: {}", shortest_word(sentence));
}

4. Implement a function that checks whether a given number is prime or not.

fn is_prime(num: u64) -> bool {
    if num <= 1 {
        return false;
    }
    // We only need to check divisibility up to the square root of num
    let sqrt_num = (num as f64).sqrt() as u64;
    for i in 2..=sqrt_num {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let num = 17;
    if is_prime(num) {
        println!("{} is prime", num);
    } else {
        println!("{} is not prime", num);
    }
}

5. Given a sorted array of integers, implement a function that returns the median of the array.

fn median(arr: &[i32]) -> f64 {
    let len = arr.len();
    if len % 2 == 0 {
        // If the length of the array is even, return the average of the middle two elements
        let mid = len / 2;
        (arr[mid - 1] as f64 + arr[mid] as f64) / 2.0
    } else {
        // If the length of the array is odd, return the middle element
        arr[len / 2] as f64
    }
}

fn main() {
    let arr = vec![1, 2, 3, 4, 5];
    println!("Median: {}", median(&arr));
}

6. Implement a function that finds the longest common prefix of a given set of strings.

fn longest_common_prefix(strs: Vec<String>) -> String {
    if strs.is_empty() {
        return String::new();
    }
    
    let mut prefix = String::new();
    for (i, c) in strs[0].chars().enumerate() {
        if strs.iter().all(|s| s.chars().nth(i) == Some(c)) {
            prefix.push(c);
        } else {
            break;
        }
    }
    prefix
}

fn main() {
    let strings = vec![
        String::from("flower"),
        String::from("flow"),
        String::from("flight")
    ];
    println!("Longest common prefix: {}", longest_common_prefix(strings));
}

7. Implement a function that returns the kth smallest element in a given array.

fn kth_smallest(arr: Vec<i32>, k: usize) -> Option<i32> {
    let mut sorted = arr.clone();
    sorted.sort();
    sorted.get(k - 1).cloned()
}

fn main() {
    let arr = vec![3, 2, 1, 5, 4];
    let k = 3;
    match kth_smallest(arr, k) {
        Some(kth) => println!("The {}th smallest element is {}", k, kth),
        None => println!("Array is empty or k is out of range"),
    }
}

8. Given a binary tree, implement a function that returns the maximum depth of the tree.

// Definition of a binary tree node
#[derive(Debug)]
struct TreeNode {
    val: i32,
    left: Option<Box<TreeNode>>,
    right: Option<Box<TreeNode>>,
}

impl TreeNode {
    fn new(val: i32) -> Self {
        TreeNode { val, left: None, right: None }
    }
}

fn max_depth(root: Option<Box<TreeNode>>) -> i32 {
    match root {
        None => 0,
        Some(node) => {
            let left_depth = max_depth(node.left);
            let right_depth = max_depth(node.right);
            1 + std::cmp::max(left_depth, right_depth)
        }
    }
}

fn main() {
    // Example binary tree
    let root = Some(Box::new(TreeNode {
        val: 3,
        left: Some(Box::new(TreeNode {
            val: 9,
            left: None,
            right: None,
        })),
        right: Some(Box::new(TreeNode {
            val: 20,
            left: Some(Box::new(TreeNode {
                val: 15,
                left: None,
                right: None,
            })),
            right: Some(Box::new(TreeNode {
                val: 7,
                left: None,
                right: None,
            })),
        })),
    }));

    println!("Maximum depth of the binary tree: {}", max_depth(root));
}

9. Reverse a string in Rust

fn reverse_string(s: &str) -> String {
    let mut chars: Vec<char> = s.chars().collect();
    chars.reverse();
    chars.into_iter().collect()
}

fn main() {
    let s = "hello";
    println!("Original string: {}", s);
    println!("Reversed string: {}", reverse_string(s));
}

10. Check if a number is prime in Rust

fn is_prime(num: u64) -> bool {
    if num <= 1 {
        return false;
    }
    let sqrt_num = (num as f64).sqrt() as u64;
    for i in 2..=sqrt_num {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    let num = 17;
    if is_prime(num) {
        println!("{} is prime", num);
    } else {
        println!("{} is not prime", num);
    }
}

11. Merge two sorted arrays in Rust

fn merge_sorted_arrays(arr1: &[i32], arr2: &[i32]) -> Vec<i32> {
    let mut merged = Vec::with_capacity(arr1.len() + arr2.len());
    let (mut i, mut j) = (0, 0);

    // Iterate over both arrays and compare elements
    while i < arr1.len() && j < arr2.len() {
        if arr1[i] < arr2[j] {
            merged.push(arr1[i]);
            i += 1;
        } else {
            merged.push(arr2[j]);
            j += 1;
        }
    }

    // Append remaining elements from arr1 (if any)
    while i < arr1.len() {
        merged.push(arr1[i]);
        i += 1;
    }

    // Append remaining elements from arr2 (if any)
    while j < arr2.len() {
        merged.push(arr2[j]);
        j += 1;
    }

    merged
}

fn main() {
    let arr1 = [1, 3, 5];
    let arr2 = [2, 4, 6];

    let merged = merge_sorted_arrays(&arr1, &arr2);
    println!("Merged sorted array: {:?}", merged);
}

12. Find the maximum subarray sum in Rust

fn max_subarray_sum(arr: &[i32]) -> i32 {
    let mut max_sum = arr[0];
    let mut current_sum = arr[0];

    for &num in arr.iter().skip(1) {
        // Determine whether to start a new subarray or extend the current one
        current_sum = num.max(current_sum + num);
        // Update the maximum sum encountered so far
        max_sum = max_sum.max(current_sum);
    }

    max_sum
}

fn main() {
    let arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
    println!("Maximum subarray sum: {}", max_subarray_sum(&arr));
}

