#include <limits.h>

int myAtoi(char* s) {
    // Skip whitespaces
    while (*s == ' ') {
        s++;
    }

    int sign = 1;
    if (*s == '-') {
        sign = -1;
        s++;
    } else if (*s == '+') {
        s++;
    }

    // Skip leading zeros
    while (*s == '0') {
        s++;
    }

    long long result = 0;
    while (*s >= '0' && *s <= '9') {
        result = result * 10 + (*s - '0');
        if (sign == 1 && result > INT_MAX) {
            return INT_MAX;
        }
        if (sign == -1 && -result < INT_MIN) {
            return INT_MIN;
        }
        s++;
    }

    return (int)(sign * result);
}
