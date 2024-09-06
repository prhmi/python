import segno

qrcode = segno.make_qr("https://doi.org/10.5281/zenodo.13556280")
qrcode.save(
    "ramkal.png",
    scale=20,
)
