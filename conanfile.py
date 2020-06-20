from conans import ConanFile, CMake, tools
import os

class TslHopscotchMapConan(ConanFile):
    name = "tsl-hopscotch-map"
    version = "2.3.0"
    license = "MIT"
    description = "C++ implementation of a fast hash map and hash set using hopscotch hashing."
    homepage = "https://github.com/Tessil/hopscotch-map"
    url = "https://github.com/Tessil/conan-tsl-hopscotch-map"
    exports = "LICENSE"

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version))

    def package(self):
        self.copy("LICENSE", dst="licenses", keep_path=False, ignore_case=True)
        
        cmake = CMake(self)
        cmake.configure(source_folder="hopscotch-map-%s" % (self.version))
        cmake.install()

    def package_id(self):
        self.info.header_only()
