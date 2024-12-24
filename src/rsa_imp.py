import rsa
import time
import random
import memory_profiler as mp

public_key, private_key = rsa.newkeys(1024)

num_runs = 1000
times = []
mems = []

for _ in range(num_runs):
    random_x = random.randint(0, 100)
    random_y = random.randint(0, 100)
    message = f"{random_x}, {random_y}".encode()
    start_t = time.perf_counter()
    mem_start = mp.memory_usage()[0]
    ciphertext = rsa.encrypt(message, public_key)
    decrypted_message = rsa.decrypt(ciphertext, private_key)
    mem_end = mp.memory_usage()[0]
    times.append(time.perf_counter() - start_t)
    mems.append(mem_end - mem_start)

print(f"Average time: {sum(times)/num_runs:.6f} s")
print(f"Average memory usage: {sum(mems)/num_runs:.6f} MB")
