import base64
import io
from fastapi import FastAPI, Request
import easyocr

app = FastAPI()
# Carga los idiomas que necesitas. 'es' para español, 'en' para inglés.
reader = easyocr.Reader(['es', 'en'])

@app.post("/ocr")
async def ocr_from_base64(request: Request):
    try:
        body = await request.json()
        image_base64 = body.get("image")
        if not image_base64:
            return {"error": "El campo 'image' es requerido en el cuerpo de la solicitud."}

        # Decodifica la imagen Base64 a datos binarios
        image_data = base64.b64decode(image_base64)
        
        # Realiza el OCR en la imagen con los bytes directamente
        result = reader.readtext(image_data)
        
        # Extrae solo el texto del resultado del OCR y únelo en una sola cadena
        extracted_text = [text for (bbox, text, prob) in result]
        full_text = " ".join(extracted_text)
        
        return {"text": full_text}
    except Exception as e:
        return {"error": str(e)}
