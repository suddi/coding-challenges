package codingChallenges

import "math"

/*
   Given a string of upper case characters, from which you have to retrieve
   the 7 letters:
   "B", "A", "L", "L" "O", "O", "N"

   Return how many times you can retrieve these characters from the string.
*/
func solution(input string) int64 {
	characters := map[rune]int64{
		'B': 0,
		'A': 0,
		'L': 0,
		'O': 0,
		'N': 0,
	}
	occurences := map[rune]byte{
		'B': 1,
		'A': 1,
		'L': 2,
		'O': 2,
		'N': 1,
	}

	for _, char := range input {
		if _, ok := characters[char]; ok {
			characters[char]++
		}
	}

	var minOccurence int64 = math.MaxInt64
	for char, freq := range characters {
		occurence := freq / int64(occurences[char])
		if occurence < minOccurence {
			minOccurence = occurence
		}
	}

	return minOccurence
}
