# import from a module
from my_module import my_func
my_func()


# import from a package
from my_main_package import some_main_script
# print(some_main_script)
print(some_main_script.report_main())


# or
from my_main_package.some_main_script import report_main
print(report_main)


# import from a sub package
from my_main_package.sub_package import my_subscript
# print(my_subscript)
print(my_subscript.sub_report())