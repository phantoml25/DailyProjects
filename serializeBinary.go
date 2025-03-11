/*
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

class Node:

	def __init__(self, val, left=None, right=None):
	    self.val = val
	    self.left = left
	    self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
*/
package main

import (
	"regexp"
	"strconv"
	"strings"
)

type BinaryNode struct {
	left  *BinaryNode
	right *BinaryNode
	data  int64
}
type BinaryTree struct {
	root *BinaryNode
}

func (t *BinaryTree) insert(data int64) *BinaryTree {
	if t.root == nil {
		t.root = &BinaryNode{data: data, left: nil, right: nil}
	} else {
		t.root.insert(data)
	}
	return t
}
func (n *BinaryNode) insert(data int64) {
	if n == nil {
		return
	} else if data <= n.data {
		if n.left == nil {
			n.left = &BinaryNode{data: data, left: nil, right: nil}
		} else {
			n.left.insert(data)
		}
	} else {
		if n.right == nil {
			n.right = &BinaryNode{data: data, left: nil, right: nil}
		} else {
			n.right.insert(data)
		}
	}
}

/*
input string will contain following format:

	Node('val',left_node(repeat),right_node(repeat))
	left_node and right_node are for documentation only,
	use Node in code
*/
func serialize(root *BinaryNode) string {
	out_string := ""
	//Depth first traversal
	out_string += "Node('"
	out_string += strconv.FormatInt(root.data, 10)
	out_string += "',"
	//left traversal
	if root.left != nil {
		out_string += serialize(root.left)
		out_string += "),"
	} else {
		out_string += "empty,"
	}
	//right traversal
	if root.right != nil {
		out_string += serialize(root.right)

	} else {
		out_string += "empty"
	}
	out_string += ")"
	return out_string
}

func deserialize_child(nodes []string, currentNode *BinaryNode) {
	if len(nodes[0]) > 5 { //need to parse for empty children
		data := strings.Split(nodes[0], "'")
		currentNode.data, _ = strconv.ParseInt(data[1], 10, 64)
		data = strings.Split(data[2], ",")
		//check for parent's empty child
		if len(data) > 3 {
			if strings.Contains(data[3], "empty") {
				nodes[0] = data[3]
			}
		} else {
			nodes = nodes[1:]
		}
	} else { //left child filled
		data := strings.Split(nodes[0], "'")
		currentNode.data, _ = strconv.ParseInt(data[1], 10, 64)
		currentNode.left = &BinaryNode{}
		nodes = nodes[1:]
		deserialize_child(nodes[0:], currentNode.left)

		//check if empty child was left on top
		if !regexp.MustCompile(`\d`).MatchString(nodes[0]) {
			nodes = nodes[1:]
		} else {
			currentNode.right = &BinaryNode{}
			deserialize_child(nodes[0:], currentNode.right)
		}

	}
}

func deserialize(tree string) BinaryTree {
	root := BinaryNode{}
	deTree := BinaryTree{&root}
	nodes := strings.Split(tree, "Node")
	currentNode := deTree.root
	nodes = nodes[1:]
	if len(nodes[0]) > 5 { //need to parse for empty children
		data := strings.Split(nodes[0], "'")
		print(data)
		currentNode.data = 5
	} else { //left child filled
		data := strings.Split(nodes[0], "'")
		currentNode.data, _ = strconv.ParseInt(data[1], 10, 64)
		currentNode.left = &BinaryNode{}
		nodes = nodes[1:]
		deserialize_child(nodes[0:], root.left)
		currentNode.right = &BinaryNode{}
		deserialize_child(nodes[0:], root.right)
	}
	print(nodes)
	return deTree
}

func main() {
	root := BinaryNode{}
	tree := BinaryTree{&root}
	root.data = 5
	tree.insert(3)
	tree.insert(7)
	tree.insert(2)
	tree.insert(4)
	tree.insert(6)
	tree.insert(8)
	tree.insert(1)
	tree.insert(9)

	serialized := serialize(tree.root)
	deserialize(serialized)
	print(serialized)

}
