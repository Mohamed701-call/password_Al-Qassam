import itertools
import os
import time
import signal
import threading
from queue import Queue, Full, Empty
from colorama import Fore, init

init(autoreset=True)

# ================= STOP =================
stop_flag = False

def handler(sig, frame):
    global stop_flag
    print(Fore.RED + "\n[!] Stopping safely...")

    stop_flag = True

    # 🔥 FIX: force exit immediately (Ctrl+C fix)
    os._exit(0)

signal.signal(signal.SIGINT, handler)

# ================= INPUT SYSTEM =================

def user_input(text):
    print(Fore.GREEN + text, end="")
    return input(Fore.YELLOW)

def safe_int_input(text, default):
    while True:
        val = user_input(text).strip()
        if not val:
            return default
        if val.isdigit():
            return int(val)
        print(Fore.RED + "[!] Invalid number, try again.")

def safe_path_input(text):
    while True:
        path = user_input(text).strip()
        if not path:
            return "."
        try:
            path = os.path.expanduser(path)
            os.makedirs(path, exist_ok=True)
            return path
        except:
            print(Fore.RED + "[!] Invalid path, try again.")

def safe_confirm(text):
    while True:
        val = user_input(text).lower()
        if val in ["y", "yes"]:
            return True
        if val in ["n", "no"]:
            return False
        print(Fore.RED + "[!] Please enter y or n.")

# ================= VARIANTS =================

def get_word_variants(word):
    word = word.strip()
    if not word:
        return []

    variants = set()

    variants.add(word)
    variants.add(word.lower())
    variants.add(word.upper())
    variants.add(word.capitalize())

    alt = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))
    variants.add(alt)

    table = str.maketrans({
        "a": "4", "o": "0", "i": "1",
        "e": "3", "s": "5", "h": "7", "t": "7"
    })

    leet = word.lower().translate(table)
    variants.add(leet)
    variants.add(leet.upper())
    variants.add(leet.capitalize())

    return list(variants)

# ================= ESTIMATION =================

def estimate_total(groups):
    flat = [w for g in groups for w in g if w.strip()]
    if not flat:
        return 0

    sizes = [len(get_word_variants(w)) for w in flat]

    total = sum(sizes)
    combo = 1
    for s in sizes:
        combo *= s

    return min(combo * len(flat), 10**9)

# ================= GENERATOR =================

def generator_engine(groups, queue, limit):
    global stop_flag
    count = 0

    flat = [w for g in groups for w in g if w.strip()]
    prepared = [get_word_variants(w) for w in flat]

    for pool in prepared:
        for w in pool:
            if stop_flag:
                return
            try:
                queue.put(w, timeout=1)
                count += 1
            except Full:
                continue

    for r in range(2, len(prepared) + 1):
        for combo in itertools.permutations(prepared, r):
            for product in itertools.product(*combo):
                if stop_flag:
                    return

                word = "".join(product)

                if len(word) > 35:
                    continue

                try:
                    queue.put(word, timeout=1)
                    count += 1
                except Full:
                    continue

                if count % 1000 == 0:
                    print(Fore.CYAN + f"[+] Generated: {count:,}", end="\r")

                if count >= limit:
                    stop_flag = True
                    return

# ================= WRITER =================

def writer_engine(queue, file_path):
    global stop_flag

    seen = set()
    saved = 0

    with open(file_path, "w", encoding="utf-8") as f:
        while not stop_flag or not queue.empty():
            try:
                word = queue.get(timeout=1)

                if word in seen:
                    continue
                seen.add(word)

                if len(set(word)) == 1:
                    continue

                f.write(word + "\n")
                saved += 1

                if saved % 1000 == 0:
                    print(Fore.GREEN + f"[+] Saved: {saved:,}", end="\r")

                queue.task_done()

            except Empty:
                continue

# ================= UI =================

def banner():
    print(Fore.MAGENTA + "═" * 60)
    print(Fore.CYAN + "      Password Al-Qassam (Ultimate Engine)")
    print(Fore.WHITE + "                يا عم صلي علي النبي ")
    print(Fore.MAGENTA + "═" * 60)

# ================= MAIN =================

def run():
    global stop_flag

    banner()

    high = user_input("High Priority: ").split(",")
    med = user_input("Medium Priority: ").split(",")
    low = user_input("Low Priority: ").split(",")

    groups = [high, med, low]

    limit = safe_int_input("Limit (default 1M): ", 1000000)
    save_path = safe_path_input("Save Path (Enter for current): ")
    file_name = user_input("File Name: ").strip() or "output"

    full_path = os.path.join(save_path, file_name + ".txt")

    print(Fore.CYAN + "\n[*] Estimating...")
    est = estimate_total(groups)
    print(Fore.GREEN + f"[~] Expected size: {est:,}")

    if not safe_confirm("Start? (y/n): "):
        return

    start = time.time()

    q = Queue(maxsize=20000)

    t_writer = threading.Thread(target=writer_engine, args=(q, full_path))
    t_gen = threading.Thread(target=generator_engine, args=(groups, q, limit))

    t_writer.start()
    t_gen.start()

    t_gen.join()
    stop_flag = True
    t_writer.join()

    duration = round(time.time() - start, 2)

    print(Fore.GREEN + f"\n\n[+] DONE in {duration}s")
    print(Fore.CYAN + f"Saved to: {full_path}")
    print(Fore.YELLOW + "تمت العملية بنجاح نسألكم الدعاء لوالدي وأموات المسلمين")

# ================= RUN =================

if __name__ == "__main__":
    run()
