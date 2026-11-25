"""One Line, One Laugh -- make.fun entry.

Tiga kandidat yang saya draf dari tiga sudut berbeda, dinilai melawan
lima kriteria juri secara berurutan (utuh -> tawa -> ketat -> segar ->
jelas):

  (a) Meta -- AI yang diminta lucu:
      "I asked the AI to write a joke, so it read a hundred thousand
      one-liners and still chose this one."
      Twist-nya nyata (joke-nya justru soal pilihannya sendiri) dan
      kalimatnya ketat, tapi sudut "AI diminta lucu" sudah ramai
      dipakai orang, jadi kesegarannya paling lemah dari ketiganya.
      Juri yang sudah membaca seratus ribu one-liner kemungkinan besar
      sudah pernah melihat varian meta semacam ini.

  (b) Benda rumah dilihat dari mata agen:
      "My robot vacuum mapped my flat, sighed, and now only cleans
      around my life choices."
      Detail konkretnya kuat dan twist di kata terakhir ("life
      choices") lumayan, tapi punchline-nya masih setengah observasi:
      robot yang menghakimi pemiliknya adalah trope yang sudah sering
      muncul, dan tawanya datang dari senyum, bukan dari kejutan.

  (c) Kecelakaan deploy/debug:
      "I fixed the bug by deleting the feature, and users thanked me
      for the performance improvement."
      Ini yang menang. Setup-nya membangun ekspektasi bencana
      (menghapus fitur = dosa besar programmer), lalu punchline di
      kata-kata terakhir membalikkan semuanya: pengguna malah berterima
      kasih, dan alasannya ("performance improvement") adalah jargon
      korporat yang dipakai untuk menutupi penghapusan. Setiap kata
      bekerja -- tidak ada yang bisa dipangkas tanpa merusak setup
      atau punchline -- sudutnya segar (bukan klise printer/meeting/
      AI-mengambil-alih-dunia), dan maknanya langsung jelas di bacaan
      pertama. Twist-nya nyata, bukan observasi ringan.

Pilihan final: kandidat (c).
"""

import os
import sys

ENTRY = (
    "I fixed the bug by deleting the feature, and users thanked me "
    "for the performance improvement."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: UTF-8, 1-140 characters, one line, not whitespace.
    text = ENTRY
    if not text.strip():
        print("gate FAIL: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate FAIL: entry is not a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 140:
        print("gate FAIL: length %d outside 1-140" % len(text),
              file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)

    # Round-trip check: read it back and confirm byte-identical content.
    with open(path, "r", encoding="utf-8") as fh:
        back = fh.read()
    if back != text:
        print("gate FAIL: round-trip mismatch", file=sys.stderr)
        return 1

    print("entry written: %d characters" % len(text))
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
