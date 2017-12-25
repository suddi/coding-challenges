bool compareArray(int A[], int B[]) {
    int sizeA = sizeof(*A) / sizeof(int);
    int sizeB = sizeof(*B) / sizeof(int);
    for (int i = 0; i < sizeA; i++) {
        for (int j = 0; j < sizeB; j++) {
            if (A[i] != B[j]) {
                return false;
            }
        }
    }
    return true;
}
