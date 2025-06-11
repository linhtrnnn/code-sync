int removeDuplicates(int* nums, int numsSize) {
    int* start = nums;
    int* end = nums + 1;
    bool twice = false;
    while (end < nums + numsSize) {
        if (*end > *start) {
            twice = false;
            start++;
            *start = *end;
            end++;
        } else if (!twice && *start == *end) {
            twice = true;
            start++;
            *start = *end;
            end++;
        } else {
            end++;
        }
    }

    return start - nums + 1;
}