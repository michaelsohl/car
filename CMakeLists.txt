cmake_minimum_required(VERSION 3.15)
project(car CXX)

add_library(car src/car.cpp)
target_include_directories(car PUBLIC include)

find_package(fmt)
find_package(engine)
find_package(control_unit)

set_target_properties(car PROPERTIES PUBLIC_HEADER "include/car.h")

target_link_libraries(car fmt::fmt)
target_link_libraries(car engine::engine)
target_link_libraries(car control_unit::control_unit)

install(TARGETS car)
