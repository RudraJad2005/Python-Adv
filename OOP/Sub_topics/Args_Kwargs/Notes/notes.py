# NOTES: *args and **kwargs

# *args collects extra positional arguments as a tuple.
# **kwargs collects extra keyword arguments as a dict.
# Use cases: flexible APIs, forwarding arguments to super() or other functions.

def demo_args(*args):
    print("args:", args)

def demo_kwargs(**kwargs):
    print("kwargs:", kwargs)

def both(x, *args, y=0, **kwargs):
    print("x:", x, "args:", args, "y:", y, "kwargs:", kwargs)

if __name__ == "__main__":
    demo_args(1, 2, 3)
    demo_kwargs(a=1, b=2)
    both(10, 20, 30, y=5, a=1, b=2)
