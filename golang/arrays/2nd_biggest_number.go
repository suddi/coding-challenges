package codingChallenges

import "math"

func solution(numbers []int64) int64 {
	var max1 int64 = math.MinInt64
	var max2 int64 = math.MinInt64

	for _, value := range numbers {
		if value > max1 {
			max2 = max1
			max1 = value
		} else if value < max1 {
			if value > max2 {
				max2 = value
			}
		}
	}

	return max2
}
