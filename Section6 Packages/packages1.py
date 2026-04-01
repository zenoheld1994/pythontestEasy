#organize related modules into a directory hierarchy, 
#it is simply a collection of modules organized into a directory
#module is 1 python file whike a package is a collection of modules in a dir
#and also a special fine named __init__.py that files distingues the directory as a python package
#packages help manage large codebases by organizing them into smaller, reusable components
#Also allow you to logically group modules that share a common functionality
# Adv
#Modularity
#Namespace prevents conflicts between identifiers in different modules by providing a separate namespace for each package
#Reusability
#Mainability
#my_package/
# __init.py__
# module1.py
# module2.py

#subpackages 
#a package can contain other packages (called subpackages). better organization
# my_package/
# __init.py__
# module1.py
# module2.py
# sub_package/
#  __init.py__
#  submodule1.py