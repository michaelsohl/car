cmake_minimum_required(VERSION 3.15)
project(car CXX)

add_library(car src/car.cpp)
target_include_directories(car PUBLIC include)

find_package(fmt)

if (COUNTRY STREQUAL "denmark")
  find_package(engine_den)
elseif(COUNTRY STREQUAL "finland")
  find_package(engine_fin)  
else()
  find_package(engine)
endif()

find_package(control_unit)

set_target_properties(car PROPERTIES PUBLIC_HEADER "include/car.h")

target_link_libraries(car fmt::fmt)

if (COUNTRY STREQUAL "denmark")
  target_link_libraries(car engine_den::engine_den)
elseif(COUNTRY STREQUAL "finland")
  target_link_libraries(car engine_fin::engine_fin)
else()
  target_link_libraries(car engine::engine)
endif()

target_link_libraries(car control_unit::control_unit)

install(TARGETS car)
