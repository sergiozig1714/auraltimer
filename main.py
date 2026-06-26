"""differ_8af7ac - Decorator factory module."""
import functools, time, json
TAG = "differ_8af7ac"
def timed(label: str = ""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*a, **kw):
            start = time.time()
            result = func(*a, **kw)
            elapsed = time.time() - start
            print(f"[{TAG}] {label or func.__name__}: {elapsed:.4f}s")
            return result
        return wrapper
    return decorator
@timed("compute")
def heavy_task(n: int) -> int:
    return sum(i * i for i in range(n))
@timed("lookup")
def search(items: list, target: int) -> int:
    return items.index(target) if target in items else -1
def main():
    print(f"[{TAG}] Running benchmarks...")
    print(f"[{TAG}] Sum: {heavy_task(100000)}")
    print(f"[{TAG}] Index: {search(list(range(50000)), 42000)}")
if __name__ == "__main__":
    main()
