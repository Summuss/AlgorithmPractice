# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.9

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "F:\Program Files\cmake-3.9.0-rc3-win64-x64\cmake-3.9.0-rc3-win64-x64\bin\cmake.exe"

# The command to remove a file.
RM = "F:\Program Files\cmake-3.9.0-rc3-win64-x64\cmake-3.9.0-rc3-win64-x64\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = F:\Datas\CodeProject\AlgorithmPractice

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = F:\Datas\CodeProject\AlgorithmPractice\build

# Include any dependencies generated for this target.
include CMakeFiles/c++practice.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/c++practice.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/c++practice.dir/flags.make

CMakeFiles/c++practice.dir/C++/main.cpp.obj: CMakeFiles/c++practice.dir/flags.make
CMakeFiles/c++practice.dir/C++/main.cpp.obj: CMakeFiles/c++practice.dir/includes_CXX.rsp
CMakeFiles/c++practice.dir/C++/main.cpp.obj: ../C++/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=F:\Datas\CodeProject\AlgorithmPractice\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/c++practice.dir/C++/main.cpp.obj"
	cd /d F:\Datas\CodeProject\AlgorithmPractice\build && g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\c++practice.dir\C++\main.cpp.obj -c F:\Datas\CodeProject\AlgorithmPractice\C++\main.cpp

CMakeFiles/c++practice.dir/C++/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/c++practice.dir/C++/main.cpp.i"
	cd /d F:\Datas\CodeProject\AlgorithmPractice\build && g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E F:\Datas\CodeProject\AlgorithmPractice\C++\main.cpp > CMakeFiles\c++practice.dir\C++\main.cpp.i

CMakeFiles/c++practice.dir/C++/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/c++practice.dir/C++/main.cpp.s"
	cd /d F:\Datas\CodeProject\AlgorithmPractice\build && g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S F:\Datas\CodeProject\AlgorithmPractice\C++\main.cpp -o CMakeFiles\c++practice.dir\C++\main.cpp.s

CMakeFiles/c++practice.dir/C++/main.cpp.obj.requires:

.PHONY : CMakeFiles/c++practice.dir/C++/main.cpp.obj.requires

CMakeFiles/c++practice.dir/C++/main.cpp.obj.provides: CMakeFiles/c++practice.dir/C++/main.cpp.obj.requires
	$(MAKE) -f CMakeFiles\c++practice.dir\build.make CMakeFiles/c++practice.dir/C++/main.cpp.obj.provides.build
.PHONY : CMakeFiles/c++practice.dir/C++/main.cpp.obj.provides

CMakeFiles/c++practice.dir/C++/main.cpp.obj.provides.build: CMakeFiles/c++practice.dir/C++/main.cpp.obj


# Object files for target c++practice
c______practice_OBJECTS = \
"CMakeFiles/c++practice.dir/C++/main.cpp.obj"

# External object files for target c++practice
c______practice_EXTERNAL_OBJECTS =

c++practice.exe: CMakeFiles/c++practice.dir/C++/main.cpp.obj
c++practice.exe: CMakeFiles/c++practice.dir/build.make
c++practice.exe: CMakeFiles/c++practice.dir/linklibs.rsp
c++practice.exe: CMakeFiles/c++practice.dir/objects1.rsp
c++practice.exe: CMakeFiles/c++practice.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=F:\Datas\CodeProject\AlgorithmPractice\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable c++practice.exe"
	cd /d F:\Datas\CodeProject\AlgorithmPractice\build && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\c++practice.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/c++practice.dir/build: c++practice.exe

.PHONY : CMakeFiles/c++practice.dir/build

CMakeFiles/c++practice.dir/requires: CMakeFiles/c++practice.dir/C++/main.cpp.obj.requires

.PHONY : CMakeFiles/c++practice.dir/requires

CMakeFiles/c++practice.dir/clean:
	cd /d F:\Datas\CodeProject\AlgorithmPractice\build && $(CMAKE_COMMAND) -P CMakeFiles\c++practice.dir\cmake_clean.cmake
.PHONY : CMakeFiles/c++practice.dir/clean

CMakeFiles/c++practice.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" F:\Datas\CodeProject\AlgorithmPractice F:\Datas\CodeProject\AlgorithmPractice F:\Datas\CodeProject\AlgorithmPractice\build F:\Datas\CodeProject\AlgorithmPractice\build F:\Datas\CodeProject\AlgorithmPractice\build\CMakeFiles\c++practice.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/c++practice.dir/depend

