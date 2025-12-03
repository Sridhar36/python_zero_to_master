# def iter_errors_from_log(path):
#     with open(path, "r", encoding="utf-8") as f:
#         for line in f:
#             if "ERROR" in line:
#                 yield line.strip()
#
# # usage
# for error_line in iter_errors_from_log("app.log"):
#     print(error_line)
#     # maybe assert conditions or count errors
#
#
#
#
# def squares_gen(n):
#     for i in range(n):
#         yield i * i
#
# nums = squares_gen(10_000_000)   # almost no memory used yet
# for x in nums:                   # values produced one by one
#     if x > 100:
#         break

'''
Generator function:
    A special function that remembers its state between calls.
    Uses yield instead of return.
    Returns a generator object (an iterator) that you can loop over.
    Produces values one by one, on demand (lazy).
'''

def simple_gen():
    print("Start")
    yield 1          # pause here, return 1
    print("Middle")
    yield 2          # pause here, return 2
    print("End")

g = simple_gen()
print(next(g))   # Start\n1
print(next(g))   # Middle\n2
# next(g) now -> StopIteration (because generator is exhausted)
