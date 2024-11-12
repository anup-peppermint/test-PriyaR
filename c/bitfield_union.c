#include <stdio.h>

// Define a structure with bitfields
struct BitFields {
    unsigned int flag1 : 1;
    unsigned int flag2 : 1;
    unsigned int flag3 : 1;
    unsigned int reserved : 5;
};

// Define a union that contains the structure
union Data {
    struct BitFields bits;
    unsigned char byte;
};

int main() {
    union Data data;

    // Setting individual bitfields
    data.bits.flag1 = 1;
    data.bits.flag2 = 0;
    data.bits.flag3 = 1;
    data.bits.reserved = 0;

    // Output the byte representation
    printf("Combined byte: %X\n", data.byte);
    return 0;
}
