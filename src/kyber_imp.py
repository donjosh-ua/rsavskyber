from kyber_py.ml_kem import ML_KEM_1024 as kem
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time
import random
import memory_profiler as mp

ek, dk = kem.keygen()
key, ct = kem.encaps(ek)
_key = kem.decaps(dk, ct)

assert key == _key

num_runs = 1000
times = []
mems = []

for _ in range(num_runs):

    random_x = random.randint(0, 100)
    random_y = random.randint(0, 100)
    message = f"{random_x}, {random_y}".encode()

    start_t = time.perf_counter()
    mem_start = mp.memory_usage()[0]

    cipher = AES.new(key[:32], AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(message, AES.block_size))

    cipher = AES.new(key[:32], AES.MODE_CBC, iv=iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)

    mem_end = mp.memory_usage()[0]
    times.append(time.perf_counter() - start_t)
    mems.append(mem_end - mem_start)

print(f"Average time: {sum(times)/num_runs:.6f} s")
print(f"Average memory usage: {sum(mems)/num_runs:.6f} MB")
