cmake_minimum_required (VERSION 2.8)
project(cmake)
set(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -D FREEGLUT_STATIC")

include_directories(${PROJECT_SOURCE_DIR}/../c++)
aux_source_directory(../c++ SrcFiles)

set(EXECUTABLE_OUTPUT_PATH  ${PROJECT_SOURCE_DIR}/../bin)
add_executable(a ${SrcFiles})


