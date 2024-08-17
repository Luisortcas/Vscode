import pyotp
import time 
import qrcode

encriptador = pyotp.random_base32()

totp = pyotp.TOTP(encriptador)

print(encriptador)

uri = pyotp.totp.TOTP(encriptador).provisioning_uri(name='Andres lozano', 
                                            issuer_name='VIOMEETS-ERACLES')

print(uri)

qrcode.make(uri).save('HEIMDALL.png')


print(totp.now())

time.sleep(59)

print(totp.now())

input_code = input('Ingrese el codigo VIO-ERACLES:')

print(totp.verify(input_code))