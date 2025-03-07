# IEEE-CS-i-dont-know-anything
🧠 Competitive Coding Task
Attempt these tasks in a language of your choice. Make sure to demonstrate all possible use-cases and mention time/space complexities of various operations. Provide screenshots of the usage.

📌 Task Levels
The challenge is divided into three levels of increasing complexity.

👞 Level 0: Basic Data Structure implementation
	Implement a doubly linked list with basic operations
Node creation
Insertion (head and tail)
Traversal (forward and backward) and printing. 

🔰 Level 1: Custom Data Structure implementation
Design a stack that supports the following operations in O(1) time and O(n) space:
push(x): Pushes element x onto the stack.
pop(): Removes the top element of the stack.
top(): Returns the top element without removing it.
getMin(): Returns the smallest element in the stack.
getMax(): Returns the largest element in the stack.
⚡ Level 2: Composite Data Structure implementation
Interval Merger: Maintain a set of non-overlapping intervals and efficiently merge them when new intervals are added.

Operations:

addInterval(start, end): Adds a new interval [start, end]. If it overlaps with existing intervals, merge them into one. Ensures the set of intervals remains non-overlapping and sorted.

getIntervals(): Returns the current set of non-overlapping, merged intervals in ascending order.


2

Time Complexity:

addInterval(): O(log n) for insertion and merging using balanced trees or sorted lists.
getIntervals(): O(n) for retrieval.

Space Complexity: O(n) (number of non-overlapping intervals).
Example:

addInterval(1, 5)
addInterval(6, 8)
addInterval(4, 7)
getIntervals() ➞ [[1, 8]]
🚀 Level 3: Composite Data Structure implementation
Design a Cache with Expiry (Time-Based Cache) that supports the following operations efficiently:

set(key, value, expiryTime): Stores the key-value pair with an expiration timestamp. If the key already exists, updates its value and expiry time.
get(key): Retrieves the value associated with the key if it exists and hasn't expired. Returns None if the key doesn’t exist or has expired.
Automatic Expiry: Expired keys should be removed automatically when get() or set() is called.

Constraints:
All operations should be optimized for fast lookups and efficient expiry handling.

Time Complexity:

set(key, value, expiryTime) → O(log n) (heap insertion)
get(key) → O(log n) (worst case, due to cleaning expired keys)

Space Complexity:

O(n) (number of active keys)
