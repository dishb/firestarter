from setuptools import setup

VERSION = "0.0.2"
DESCRIPTION = "A cross-platform CLI to help you jump right into developing projects with Python."

# with open("README.md", "r", encoding = "utf-8") as file:
#     LONG_DESCRIPTION = file.read()
#     file.close()

with open("requirements.txt", "r", encoding = "utf-8") as file:
    REQUIREMENTS = file.read()
    REQUIREMENTS = REQUIREMENTS.split()
    file.close()

setup(name = "firestarter",
      version = VERSION,
      author = "Dishant B. (@dishb)",
      author_email = "code.dishb@gmail.com",
      description = DESCRIPTION,
      long_description = "LONG_DESCRIPTION",
      long_description_content_type = "text/markdown",
      packages = ["firestarter",
                  "firestarter._core",
                  "firestarter._fuel",
                  "firestarter._utils"
                  ],
      entry_points = {"console_scripts": ["firestarter = firestarter._core._entry_points:_console"]},
      install_requires = REQUIREMENTS,
      python_requires = ">=3.9",
      keywords = ["firestarter",
                  "quickstart"
                  "build tool",
                  "project quickstart",
                  "cli",
                  "tool",
                  "developers",
                  "developing",
                  "firestarter tool",
                  "project maker",
                  "boilerplate",
                  "base files",
                  "python",
                  "cross-platform",
                  "python3"
                  ],
      license = "None",
      project_urls = {"Documentation": "https://github.com/dishb/firestarter/tree/main/docs",
                      "Source": "https://github.com/dishb/firestarter/",
                      "Issue Tracker": "https://github.com/dishb/firestarter/issues"
                      },
      url = "https://github.com/dishb/firestarter",
      classifiers = ["Programming Language :: Python :: 3.9",
                     "Programming Language :: Python :: 3.10",
                     "Programming Language :: Python :: 3.11",
                     "Programming Language :: Python :: 3.12",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: MIT License",
                     "Environment :: Console",
                     "Intended Audience :: Developers",
                     "Natural Language :: English",
                     "Topic :: Software Development",
                     "Topic :: Software Development :: Build Tools",
                     "Topic :: Software Development :: Libraries :: Python Modules",
                     "Topic :: Utilities"
                     ]
     )
