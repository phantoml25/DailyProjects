/*
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
*/

package main

import "container/list"

type wordNode struct {
	children [26]*wordNode

	//tells reader if this is the end of a word
	//node can still have more children
	isWordEnd bool
}

func dictionary_preproccess(indict []string) {
	var processed_dict = list.New()
	for i := 0; i < len(indict); i++ {
		letter1 := indict[i][0]
		if processed_dict.Front() == nil {
			processed_dict.PushFront(letter1)
		}
	}
}
