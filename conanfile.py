from conans import ConanFile, CMake, tools


class SoxrConan(ConanFile):
    name = "soxr"
    version = "0.1.3"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Soxr here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    source_subfolder = "soxr-{version}-Source".format(version=version)

    def source(self):
        url = "https://sourceforge.net/projects/soxr/files/soxr-{version}-Source.tar.xz".format(version=self.version)
        tools.get(url)
        
        insert_position = "project (soxr C)"
        tools.replace_in_file("{}/CMakeLists.txt".format(self.source_subfolder),
            insert_position, insert_position + '''
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["soxr"]

