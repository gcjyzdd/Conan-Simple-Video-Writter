from conans import ConanFile, CMake, tools

class HelloConan(ConanFile):
    name = "VideoWriter"
    version = "1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello here>"
    settings = "os", "compiler", "arch"
    options = {}
    default_options = {}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/gcjyzdd/Simple-Video-Writter.git")
        self.run(
            "cd Simple-Video-Writter && git checkout 1.0 && git submodule update --init --recursive")

    def build(self):
        pass

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="Simple-Video-Writter")
        self.run("cmake --build . --config Release")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["videowriter"]