#include <iostream>
#include <soxr.h>

int main() {
    std::cout << "soxr " << SOXR_THIS_VERSION_STR << std::endl;
    std::cout << soxr_version() << std::endl;
    return 0;
}
