#include <stdio.h>
#include <stddef.h>
#include <stdint.h>

#pragma pack(4)
struct y {
    int32_t a;
    int16_t b;
    char c[1024];
    int16_t d;
    int16_t e;
};

int main(void) {
    printf("Offsets in struct y (with #pragma pack(4)):\n");
    printf("a: %zu\n", offsetof(struct y, a));
    printf("b: %zu\n", offsetof(struct y, b));
    printf("c: %zu\n", offsetof(struct y, c));
    printf("d: %zu\n", offsetof(struct y, d));
    printf("e: %zu\n", offsetof(struct y, e));
    printf("sizeof(struct y): %zu\n", sizeof(struct y));
    return 0;
}

