from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "VideoWriter"
    version = "1.3"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = {}
    generators = "cmake"

    def config_options(self):
        self.settings.build_type = "Release"
        if self.settings.os == "Windows":
            self.settings.compiler.runtime = "MD"

    def source(self):
        self.run("git clone https://github.com/gcjyzdd/Simple-Video-Writter.git")
        self.run(
            "cd Simple-Video-Writter && git checkout " + str(self.version) + " && git submodule update --init --recursive")

    def build(self):
        pass

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="Simple-Video-Writter")
        if self.settings.os != "Windows":
            self.run("cmake --build . --config Release -j 8")
        else:
            self.run("cmake --build . --config Release")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["videowriter"]
