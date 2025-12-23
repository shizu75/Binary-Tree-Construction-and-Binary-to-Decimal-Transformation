# Binary Tree Construction and Binary-to-Decimal Transformation

## Project Overview
This project demonstrates the use of a **custom binary tree data structure** to process binary representations of integers. The program converts a user-input integer into binary, inserts its bits into a tree following defined rules, performs an **inorder traversal**, and finally converts the traversal result back into a decimal number.

The project combines concepts from:
- Data Structures (Binary Trees)
- Binary Number Systems
- Tree Traversals
- Algorithmic Thinking in Python

---

## Objectives
- Convert a decimal number into its binary representation
- Insert binary digits into a binary tree using conditional logic
- Perform inorder traversal on the tree
- Convert the resulting binary sequence back into a decimal value
- Demonstrate the effect of traversal order on binary data

---

## Technologies Used
- Python 3
- Core Python Data Structures
- Recursion

---

## Key Concepts Covered
- Binary Tree implementation
- Recursive insertion logic
- Inorder traversal
- Binary-to-decimal and decimal-to-binary conversion
- Input handling and conditional flow

---

## Program Workflow

### 1. Tree Class Definition
A custom `Tree` class is defined with:
- `Data`: stores the binary digit (`'0'` or `'1'`)
- `left`: left child node
- `right`: right child node

---

### 2. Insert Logic
- `'0'` values are inserted into the **left subtree**
- `'1'` values are inserted into the **right subtree**
- If a node already exists, insertion continues recursively

This logic creates a structured binary tree based on bit values.

---

### 3. Inorder Traversal
- Traverses the tree in **Left → Root → Right** order
- Concatenates binary digits into a string
- Produces a reordered binary sequence

---

### 4. Binary Processing Logic
- The user inputs an integer
- The integer is converted to binary using Python’s built-in function
- Special handling ensures the first `'1'` is inserted correctly when leading zeros exist
- Remaining bits are inserted sequentially

---

### 5. Final Conversion
- The inorder traversal result is treated as a binary number
- Converted back into a decimal integer
- Final output demonstrates how tree traversal affects binary interpretation

---

## Example Output Flow
- User enters a decimal number
- Program displays:
  - Original number
  - Binary representation
  - Inorder traversal result (binary)
  - Final decimal value after traversal

---

## How to Run the Program

### Prerequisites
- Python 3 installed on your system

---

### Execution Steps
1. Save the script in a `.py` file
2. Run the script using Python
3. Enter an integer when prompted
4. Observe binary, inorder traversal, and decimal outputs

---

## Use Cases
- Learning binary trees and traversal techniques
- Understanding binary data manipulation
- Educational demonstrations for data structures
- Algorithm design practice

---

## Limitations
- Tree insertion logic is specific to binary characters `'0'` and `'1'`
- Not a traditional Binary Search Tree (BST)
- Designed for educational purposes rather than optimized computation

---

## Possible Enhancements
- Support for generic BST insertion
- Visualization of tree structure
- Support for preorder and postorder traversals
- Error handling for invalid inputs
- Integration with graphical tree visualization tools

---

## Learning Outcomes
- Strong understanding of tree-based data structures
- Hands-on experience with recursive algorithms
- Insight into binary number manipulation
- Clear understanding of traversal-based data transformation

---

## Author
This project was created as a practical exercise to explore binary trees, traversal algorithms, and binary number systems using Python.
