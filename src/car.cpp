#include <iostream>
#include "car.h"
#include <fmt/color.h>
#include <engine.h>
#include <control_unit.h>

void car(){
    

    #ifdef NDEBUG
    std::cout << "car/1.0: Release!\n";
    #else
    std::cout << "car/1.0: Debug!\n";
    #endif
    engine();
    control_unit();
    fmt::print(fg(fmt::color::red) | fmt::emphasis::bold, "This is a red car!\n");
}

void car_print_vector(const std::vector<std::string> &strings) {
    for(std::vector<std::string>::const_iterator it = strings.begin(); it != strings.end(); ++it) {
        std::cout << "car/1.0 " << *it << std::endl;
    }
}
