package Soundex

/***************
* Soundex Test - Daily Project 6/23/24
* By: Kevin Adams
* Implement American Soundex as prescribed here: https://en.wikipedia.org/wiki/Soundex
* To run, rename file and package to main
***************/

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	consonants := map[string]int{"b": 1, "f": 1, "p": 1, "v": 1, "c": 2, "g": 2, "j": 2, "k": 2, "q": 2, "s": 2, "x": 2, "z": 2, "d": 3, "t": 3, "l": 4, "m": 5, "n": 5, "r": 6, "a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0, "h": 0, "w": 0}
	doubleVowels := map[string]int{"y": 0, "h": 0, "w": 0}
	yn := map[string]int{"y": 1, "n": 1}
	end := false

	//perform tasks in a loop for ease of use
	for !end {
		//first, read in a line from stdin
		fmt.Printf("Enter a word to process: ")
		reader := bufio.NewScanner(os.Stdin)
		reader.Scan()
		err := reader.Err()
		if err != nil {
			log.Fatal(err)
		}
		line := reader.Text()
		//then, split off the first word for processing
		words := strings.Split(line, " ")
		word := words[0]
		chars := strings.Split(word, "")
		//start processing the word
		i := 0
		startLetter := ""
		startSound := -1
		prevSound := -1
		outString := ""
		for i < len(chars) {
			if i == 0 {
				startLetter = chars[0]
				startSound = consonants[startLetter]
				prevSound = consonants[startLetter]
				outString += startLetter
			} else if consonants[chars[i]] == startSound {
				//repeated start sound, do not add
			} else if consonants[chars[i]] == 0 {
				//Vowel, do not add
			} else if consonants[chars[i]] == prevSound {
				_, hwy := doubleVowels[chars[i-1]]
				//Double sound, check if consecutive consonants
				if consonants[chars[i]] == consonants[chars[i-1]] {
					//Double consonants with same sound, do not add
				} else if hwy { //Next, check if separated by a non-h/w/y vowel
					//previous character was h/w/y, Double sound, do not add
				} else {
					//Separated by non-h/w/y vowel, add
					outString += strconv.Itoa(consonants[chars[i]])
					prevSound = consonants[chars[i]]
				}
			} else {
				//new consonant, add to outString
				outString += strconv.Itoa(consonants[chars[i]])
				prevSound = consonants[chars[i]]
			}
			i++
		}
		for len(outString) < 4 {
			outString += "0"
		}
		fmt.Printf("That word becomes: %s\n", outString[:4])
		fmt.Printf("Process another word? y/n\n")
		reader.Scan()
		_, ok := yn[reader.Text()]
		for !ok {
			fmt.Printf("Invalid input. Please try again: ")
			reader.Scan()
		}
		if reader.Text() == "n" {
			end = true
		}
	}

}
