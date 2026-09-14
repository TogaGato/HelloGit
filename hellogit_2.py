#Código alternativo que funcina con instalación Básica
import qrcode

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
        
        print("\n🔄 Generando código QR...")
        
        # Crear el código QR
        qr = qrcode.QRCode(
            version=None,  # Auto-detección
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        
        qr.add_data(text)
        qr.make(fit=True)
        
        # Crear imagen - método alternativo que no requiere Pillow
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Guardar imagen
        img.save(filename)
        
        # Mostrar resultado
        print("\n" + "=" * 50)
        print("         📱 GENERADOR DE CÓDIGOS QR")
        print("=" * 50)
        print(f"\n📝 Contenido: {text}")
        print(f"💾 Archivo: {filename}")
        if hasattr(qr, 'version'):
            print(f"📐 Versión: {qr.version}")
        print("\n✅ QR CREADO EXITOSAMENTE!")
        print("=" * 50)
        
    except ImportError:
        print("❌ Error: Falta la librería Pillow")
        print("   Instala con: pip install Pillow")
        
    except Exception as error:
        print(f"❌ Error: {error}")
        print("   Verifica que tengas instalado: pip install qrcode")

if __name__ == "__main__":
    generar_qr()