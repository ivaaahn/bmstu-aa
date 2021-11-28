cmake_minimum_required(VERSION 3.20)
project(lab_04)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS "-O0")

include_directories(app)

add_executable(lab_04
        app/errors.cpp
        app/errors.hpp
        app/main.cpp
        app/point.cpp
        app/point.hpp
        app/points.cpp
        app/points.hpp)

find_package(Threads REQUIRED)
target_link_libraries(${PROJECT_NAME} Threads::Threads)