# RSA Montgomery Multiplication Playground

This repository is a small, educational RSA project focused on modular exponentiation performance.

It contains three implementations that all use the same fixed RSA key material, so you can compare arithmetic strategies directly:

- `rsa.py`: pure Python square-and-multiply (`(a * b) % n` in the loop)
- `rsa_mont.py`: pure Python Montgomery reduction and exponentiation
- `rsapow.py`: Python built-in `pow(base, exp, mod)` (implemented in optimized C)

## Important notes

- This code is for learning and benchmarking, not production cryptography.
- The private key is embedded in source code.
- Encryption is textbook RSA without padding (no OAEP/PKCS#1 v1.5).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Quick correctness check

Run this once to verify all implementations round-trip a message correctly:

```bash
python - <<'PY'
import rsa, rsa_mont, rsapow

message = b"benchmark-check"
for mod in (rsa, rsa_mont, rsapow):
    ciphertext = mod.encrypt(message)
    plaintext = mod.decrypt(ciphertext)
    print(f"{mod.__name__:8s} ok={plaintext == message}")
PY
```

## Benchmarking implementations against each other

There are a lot of tools that give accurate statistical benchmarks, I like to use `hyperfine`

Install hyperfine using: `sudo apt install hyperfine`

You can now use it to benchmark a specific script:

`hyperfine "python rsa.py 1"`

it should give an output like the following:

### Tips for fair results

- Run on an idle machine and close heavy background apps.
- Use the same Python interpreter for all runs.

## Expected outcome

You will usually see:

- `rsapow.py` fastest (optimized C internals)
- `rsa.py` typically faster than `rsa_mont.py`, Python-level overhead prevents the Montgomery Multiplication optimization to make the intended Effect

## Final Notes

If you find a bug, and or an optimization feel free to open a pull request or contact me directly.
