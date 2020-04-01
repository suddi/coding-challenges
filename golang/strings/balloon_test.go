package codingChallenges

import "testing"

type TestCase struct {
	Input          string
	ExpectedResult int64
}

func TestSolution(t *testing.T) {
	tests := map[byte]TestCase{
		1: TestCase{
			"AGEASEBESLOLOBN",
			1,
		},
		2: TestCase{
			"AGEASEBESLOLOBNDSOENOLBOLVA",
			2,
		},
		3: TestCase{
			"XEBEALPLOWQOA",
			0,
		},
	}

	for caseNumber, test := range tests {
		result := solution(test.Input)

		if result != test.ExpectedResult {
			t.Errorf("Test Case %d: FAILED", caseNumber)
		}
	}
}
