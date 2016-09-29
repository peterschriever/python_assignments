try:
    raise ValueError("test")
    print("print statement")
    raise AssertionError("Foo")

except ValueError:
    print("ValueError being handled through except block.")

except AssertionError:
    print("AssertionError being handled through except block.")

finally:
    print("finally block reached.")
    print("finally block reached1.")
