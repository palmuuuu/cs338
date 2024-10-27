import base64

encoded_command = "bQBzAGgAdABhACAAaAB0AHQAcAA6AC8ALwBuAG8AbgBtAGEAbABpAGMAaQBvAHUAcwBjAGEAcAB0AGMAaABhAC4AbQBlAHQAYQBwAHIAbwBiAGwAZQBtAHMALgBjAG8AbQAvAE0AZQB0AGEAQwBUAEYAewBGADQAawAzAF8AYwA0AHAAVABjAGgAQABzAF8AcgB1AE4AXwBtADQAbAB3ADQAcgAzAH0A"

padding_needed = len(encoded_command) % 4
if padding_needed != 0:
    encoded_command += "=" * (4 - padding_needed)

decoded_command = base64.b64decode(encoded_command).decode('utf-8')
print(decoded_command)
