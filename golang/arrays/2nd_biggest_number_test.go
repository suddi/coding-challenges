package codingChallenges

import (
	"fmt"
	"math"
	"testing"
)

type TestCase struct {
	Input          []int64
	ExpectedResult int64
}

func TestSolution(t *testing.T) {
	tests := map[int16]TestCase{
		1: TestCase{
			[]int64{4, 4, -5, 3, 2, 3, 7, 7, 8, 8},
			7,
		},
		2: TestCase{
			[]int64{-1, -2, -15, -1, -2, -1, -2},
			-2,
		},
		3: TestCase{
			[]int64{1, 1, 1, 1},
			math.MinInt64,
		},
	}

	for caseNumber, test := range tests {
		result := solution(test.Input)

		if result != test.ExpectedResult {
			fmt.Println(result)
			t.Errorf("Test Case %d: FAILED", caseNumber)
		}
	}
}
