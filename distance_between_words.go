/*
	Find an efficient algorithm to find the smallest distance (measured in number of words)
	between any two given words in a string.

	For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world",
	return 1 because there's only one word "cat" in between the two words.

	Concept:
		Process the string into a list, storing the word as the key and associating each instance of that word in the string
		as an integer location attached to it.

		When searching for the distance between words, simply grab the locations of each word and then find the two locations
		with the smallest difference between them
*/

package main

func stringProcess(input string) {

}
