from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.scm import Git
from conan.errors import ConanInvalidConfiguration

countries = ["sweden", "finland", "denmark"]

class carRecipe(ConanFile):
    name = "car"
    version = "1.0"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of car package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "country": ["sweden", "denmark", "finland"]}
    default_options = {"shared": False, "country": "sweden"}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("fmt/8.1.1")
        self.requires("control_unit/1.0")

        # Depending on option -o country=
        if self.options.country:
          if self.options.country == "sweden":
            self.requires("engine/2.0")    
          elif self.options.country == "finland":
            self.requires("engine_fin/2.0")
          elif self.options.country == "denmark":
            self.requires("engine_den/2.0")

    def build_requirements(self):
        self.tool_requires("cmake/3.22.6")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        if self.options.country:
          tc.variables["COUNTRY"] = self.options.country
       
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["car"]

    

    

