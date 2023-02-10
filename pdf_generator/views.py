import os
import pdfkit
from . import pdf_gen_route
from datetime import datetime
from flask import render_template, Response, request
from utils.models_creator import *

@pdf_gen_route.route("/download", methods=['GET'])
def route_download():

    args = request.args or request.get_json()

    arg_language = args.get('languageCode', 'ru')
    arg_client_id = args.get('clientId', None)
    arg_type_name = args.get('typeName', None)

    data = get_customer(arg_client_id)

    code = gen_code()
    type_id = create_new_type(code, arg_type_name)

    birth_date_string = data['birth_date']
    birth_date_obj = datetime.strptime(birth_date_string, '%d-%m-%Y')

    client_id = create_new_customer(data['name'], data['surname'], data['patronymic'], data['inn'], birth_date_obj)

    document_number = gen_code()
    create_new_document(document_number,client_id, type_id)

    data.update({
        'dtime': datetime.now().strftime('%d-%m-%Y')
    })

    lang_templates = {
        'ru': 'export.html',
        'en': 'export_en.html',
        'kg': 'export_kg.html',
    }

    full_template = lang_templates.get(
        arg_language if arg_language in lang_templates else 'ru'
    )

    out = render_template(full_template, data=data)

    # PDF options
    options = {
        "orientation": "portrait",
        "page-size": "A4",
        "margin-top": "1.0cm",
        "margin-right": "1.5cm",
        "margin-bottom": "1.0cm",
        "margin-left": "1.5cm",
        "encoding": "UTF-8",
    }
    
    # Build PDF from HTML 
    pdf = pdfkit.from_string(out, options=options)
    
    # Download the PDF
    return Response(pdf, mimetype="application/pdf")