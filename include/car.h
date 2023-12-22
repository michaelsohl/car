#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define CAR_EXPORT __declspec(dllexport)
#else
  #define CAR_EXPORT
#endif

CAR_EXPORT void car();
CAR_EXPORT void car_print_vector(const std::vector<std::string> &strings);
