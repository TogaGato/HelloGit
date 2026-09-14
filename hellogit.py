import qrcode
from qrcode.exceptions import DataOverflowError

def generar_qr():
    try:
        # Solicitar texto o URL
        text = input("Ingrese texto o URL: ").strip()
        
        if not text:
            print("❌ Error: La entrada no puede estar vacía")
            return
        
        # Solicitar nombre del archivo
        filename = input("Ingrese el nombre de la imagen (o presione Enter para 'qrcode.png'): ").strip()
        if not filename:
            filename = "qrcode.png"
        elif not filename.endswith(".png"):
            filename += ".png"
        
        # Determinar la versión automáticamente según el tamaño del texto
        # Versión máxima 40, pero usamos 40 para textos largos
        version = 40 if len(text) > 3000 else None  # None = auto-detección
        
        print("\n🔄 Generando código QR...")
        
        # Crear el código QR
        qr = qrcode.QRCode(
            version=version,  # None permite ajuste automático
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        
        qr.add_data(text)
        qr.make(fit=True)
        
        # Generar la imagen
        image = qr.make_image(
            fill_color="black",
            back_color="white"
        )
        
        # Guardar la imagen
        image.save(filename)
        
        # Mostrar resultado
        print("\n" + "=" * 50)
        print("         📱 QR GENERADOR DE CÓDIGOS QR")
        print("=" * 50)
        print(f"\n📝 Contenido: {text}")
        print(f"💾 Archivo: {filename}")
        print(f"📐 Versión: {qr.version}")
        print(f"📏 Tamaño: {qr.modules_count} x {qr.modules_count} píxeles")
        print("\n✅ QR CÓDIGO CREADO EXITOSAMENTE!")
        print("=" * 50)
        
        return True
        
    except DataOverflowError:
        print("❌ Error: El texto es demasiado largo para un código QR estándar")
        print("   Máximo recomendado: ~4296 caracteres alfanuméricos")
        print("   Intenta acortar el texto o usar un enlace más corto")
        
    except PermissionError:
        print("❌ Error: No tienes permisos para escribir en este directorio")
        print(f"   Intenta guardar en: ./{filename}")
        
    except Exception as error:
        print(f"❌ Error inesperado: {type(error).__name__}")
        print(f"   Detalles: {error}")
        print("   Verifica que tengas instalada la librería: pip install qrcode[pil]")

if __name__ == "__main__":
    generar_qr()