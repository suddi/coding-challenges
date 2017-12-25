#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest.h"
#include "../utils.h"

int *solution(int A[], int size) {
    for (int i = 0; i < size; i++) {
        int current = A[i];
        int j = i - 1;

        while (j >= 0 && current < A[j]) {
            A[j + 1] = A[j];
            j -= 1;
        }

        A[j + 1] = current;
    }

    return A;
}

TEST_CASE("Testing solution()") {
    auto testCase1 = [] () {
        int input[] = {5, 2, 2, 4, 1, 3, 7, 9};
        int size = sizeof(input) / sizeof(int);
        int expectedResult[] = {1, 2, 2, 3, 4, 5, 7, 9};
        return compareArray(solution(input, size), expectedResult);
    };
    CHECK(testCase1() == true);

    auto testCase2 = [] () {
        int input[] = {2, 4, 6, 2, 0, 8};
        int size = sizeof(input) / sizeof(int);
        int expectedResult[] = {0, 2, 2, 4, 6, 8};
        return compareArray(solution(input, size), expectedResult);
    };
    CHECK(testCase2() == true);

    auto testCase3 = [] () {
        int input[] = {1, 3, 5, 7, 3, 9, 1, 5};
        int size = sizeof(input) / sizeof(int);
        int expectedResult[] = {1, 1, 3, 3, 5, 5, 7, 9};
        return compareArray(solution(input, size), expectedResult);
    };
    CHECK(testCase3() == true);
}
