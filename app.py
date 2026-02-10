import streamlit as st
import google.generativeai as genai

# --- Imagen corporativa Zotal ---
logo_url = "https://www.zotal.com/wp-content/uploads/2023/05/zotal_laboratorio_logo.png"
st.set_page_config(page_title="Zotal — Asistente", page_icon=logo_url)

# Header con logo y texto de bienvenida
col1, col2 = st.columns([1, 10])
with col1:
    st.image(logo_url, width=120)
with col2:
    st.markdown(f"<h1 style='color:#0A0C4A; margin:0; padding-top:6px;'>Zotal — Asistente Técnico</h1>", unsafe_allow_html=True)
    st.markdown("**Bienvenido a Zotal. Consulta nuestros productos y recomendaciones.**")

# Pequeño estilo adicional para botones y llamadas a la acción
st.markdown(
    """
    <style>
    .stButton>button { background-color: #0A0C4A; color: white; }
    </style>
    """,
    unsafe_allow_html=True
)


# 1. Configuración de seguridad para la API Key
# En la nube, no pondremos la clave aquí por seguridad.
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash') # El 1.5 es más estable para demos largas

# 2. Tu base de conocimientos (Pega aquí el texto de las fichas)
contexto = """
ARPON DIAZIPOL
ARPON DIAZIPOL es un insecticida emulsionable que combina las propiedades de eficacia y volteo a bajas concentraciones propias de la Cipermetrina con el potente y prolongado efecto residual de la Deltametrina, obteniéndose de este modo unos insuperables resultados en la desinsectación de todo tipo de instalaciones ganaderas. Su amplio espectro de acción incluye tanto a insectos voladores como insectos rastreros. La combinación Cipermetrina/Deltametrina/Tetrametrina rinde unos espectaculares resultados en la eliminación de moscas al actuar ambos ingredientes de un modo potente, simultáneo y sostenido sobre el insecto. 
DOSIFICACIÓN: Se emplea diluido del 0,3 al 1%.
PROPIEDADES E INDICACIONES: 
ARPÓN DIAZIPOL es un insecticida emulsionable que combina las propiedades de eficacia y volteo a bajas concentraciones propias de la Cipermetrina con el potente y prolongado efecto residual de la Deltametrina, obteniéndose de este modo resultados insuperables en la desinsectación de todo tipo de instalaciones ganaderas, como establos, granjas, perreras, mataderos (áreas de estabulación de animales) clínicas veterinarias (zonas de hospitalización, jaulas...) y vehículos de transporte de animales. Su amplio espectro de acción incluye tanto a insectos voladores (moscas, mosquitos, abejorros, avispas, tábanos) como insectos reptantes (pulgas, garrapatas, chinches, escarabajos, cucarachas, arañas, hormigas, piojos...). La combinación Cipermetrina/Deltametrina/Tetrametrina rinde unos espectaculares resultados en la eliminación de moscas al actuar ambos ingredientes de un modo potente, simultáneo y sostenido sobre el insecto. 
MODO DE EMPLEO: 
Dependiendo del grado de infestación y de la persistencia que se desee, ARPÓN DIAZIPOL se emplea mezclando con agua a concentraciones que van del 0,3% al 1%. Una vez mezclado debe aplicarse por pulverización sobre la superficie a tratar a razón de 5 litros por cada 100 m2 para superficies impermeables o de 10 litros por cada 100 m2 para superficies no impermeables. Una vez preparada la emulsión en agua debe utilizarse antes de 12 horas. Antes de usar el producto léase detenidamente la etiqueta. Ventílese adecuadamente antes de entrar en el recinto. No deberá mezclarse con ningún otro producto. No aplicar en presencia de animales ni personas. No aplicar en áreas accesibles a niños. Evitar el contacto de los animales y personas con superficies tratadas o expuestas. 
Plazo de seguridad: 24 a 48 horas. 
Modo de empleo: pulverización. No reutilizar el envase. Eliminar el envase y los restos de producto de un modo seguro. Limpiar adecuadamente el equipo de aplicación. El producto es tóxico para gatos, abejas y organismos acuáticos. No eliminar el producto a través de desagües, alcantarillas o a cursos de agua. 
A FIN DE EVITAR RIESGOS PARA LAS PERSONAS Y EL MEDIO AMBIENTE SIGA LAS INSTRUCCIONES DE USO. 
USO GANADERO: PERSONAL NO PROFESIONAL. PERSONAL PROFESIONAL. PERSONAL PROFESIONAL ESPECIALIZADO.
SANITAS Dual 
DESINFECTANTE INSECTICIDA AMPLIO ESPECTRO 
400 
MICROBIOS 
ÁCARO ROJO 
ALPHITOBIUS 
SANITAS 
MICROBIOS 
Dual 
INSECTICIDA DESINFECTANTE 
ÁCARO ROJO 
ALPHITOBIUS 
USO EN EL ENTORNO GANADERO 
Desinfectante-insecticida de última generación que combina 4 principios activos desinfectantes (Glutaraldehido, Cloruro de Didecil Dimetil Amonio, Cloruro de Alquil Dimetil Bencilamonio y Ácido Glicólico) que unidos ejercen una acción desinfectante de muy amplio espectro que comprende bacterias, virus y hongos. La gran capacidad de penetración de estos compuestos, unida a la acción de los tensioactivos de su excipiente, asegura una acción desinfectante inmediata e intensa incluso en presencia de materia orgánica. Además, en su composición se incluye alfacipermetrina, que lo convierte en un eficaz insecticida, frente a todo tipo de insectos y ácaros, como ácaro rojo, moscas, mosquitos, cucarachas, pulgas, hormigas, arañas; garrapatas y otros.  
COMPOSICIÓN 
Glutaraldehido 
Didecil dimetil cloruro de amonio 7,25% 
Alquildimetilbencil cloruro de amonio 10% 
Ácido glicólico 15,92% 
Alfacipermetrina 1,4% 
Excipiente c.s.p. 6% 
100% 
APLICACIONES: 
Indicado para la desinfección y desinsectación completa de naves, locales, recintos e instalaciones de ganadería, avicultura (broilers, ponedoras y salas de incubación, en ausencia de animales y huevos) y cunicultura, perreras y otros recintos en los que se alberguen animales. Asimismo, puede ser utilizado en la desinfección y desinsectación de maquinaria y aparatos, así como para el tratamiento de medios de transporte de ganado, clínicas veterinarias (áreas destinadas a animales, jaulas de hospitalización...) y mataderos (área de estabulación de animales). 
INDICACIONES, DOSIS RECOMENDADAS Y MODO DE EMPLEO: 
Debido a su extraordinaria eficacia, solo es necesaria una aplicación del producto para conseguir las condiciones higiénico-sanitarias adecuadas. 
Se debe realizar una limpieza en profundidad previa de la instalación a tratar. El producto se puede usar mediante frotamiento, pulverización o inmersión (en el caso de que la desinfección sea de utensilios o maquinaria). Debe aplicarse a la dosis recomendada, dejándolo actuar, al menos durante 30 minutos. Se debe diluir el producto en agua según las siguientes proporciones: 
• Locales y recintos: 
Acción Bactericida: 0,5% (aplicar en condiciones limpias y dejar actuar 30 minutos). 
Acción Fungicida: 16% (aplicar en condiciones limpias y dejar actuar 30 minutos). Insecticida: 0,5% 
Medios de transporte: 0,5% (50 ml de SANITAS DUAL en 10 I de agua). 
• Vados sanitarios: 1% (100 ml de SANITAS DUAL en 10 I de agua). 
Aplicar a razón de: 
• Superficies no porosas: 100 ml de dilución/m2 
• Superficies porosas: 300 ml de dilución/m2 
CONSEJOS DE UTILIZACIÓN: 
Utilizar en ambientes bien ventilados. Aplicar el tratamiento en ausencia de animales 
y asegurar una óptima ventilación del recinto antes del realojo de los animales. Esperar un plazo de seguridad: 24-48 horas. 
NÚMERO DE REGISTRO: 0987-P

PREVIO Diox
DESINFECTANTE Y ACTIVADOR PARA PREPARACIÓN DE DIÓXIDO DE CLORO
Previo Diox es un desinfectante de amplio espectro (virus, bacterias, hongos,...) para el tratamiento del agua de consumo animal y humano, y sus canalizaciones, eliminando el biofilm, así como tratamiento desinfectante en la industria alimentaria: frutas, verduras, industrias cárnicas, etc; también se usa en sistemas de refrigeración de agua.
DESCRIPCIÓN: Previo Diox es un desinfectante de amplio espectro (virus, bacterias, hongos,...) para el tratamiento del agua de consumo animal y humano, así como tratamiento desinfectante en la industria alimentaria: frutas, verduras, industrias cárnicas, etc; también se usa en sistemas de refrigeración de agua. 
Desinfecta los sistemas de almacenamiento y distribución de agua, eliminando también el biofilm y las algas, evitando la aparición de los mismos. No da sabor ni olor al agua tratada, no se originan cloraminas ni compuestos halogenados tóxicos, THM. 
Alta rapidez de acción, por lo que disminuye los tiempos de contacto y buen comportamiento en presencia de materia orgánica. 
Previo Diox es suministrado en dos componentes, Previo Diox componente A y Previo Diox componente B que deben ser mezclados en el momento de la aplicación. 
MODO DE EMPLEO Y DOSIFICACIÓN: 
Añadir Previo Diox componente B (suministrado en botellas de 1 kg) en el envase de Previo Diox Componente A (suministrado en garrafa de 24 kg) y agitar durante unos segundos. Dejar que se produzca la reacción en función de la temperatura del agua: 
• 6 h a 10° C 
• 30 min a 20° C 
• 20 min a 30° C 
• 10 min a 40° C 
COMPOSICIÓN COMPONENTE A 
Clorito Sódico 
1,55% 
COMPOSICIÓN COMPONENTE B 
Ácido Clorhídrico 
FORMATOS DISPONIBLES 
Componente A 
Componente B 
13,5% 
Una vez conseguida la reacción, dosificar directamente en el agua. 
La mezcla resultante tiene una concentración de 0,75% de dióxido de cloro. Se debe obtener un residual de 0,5 ppm. 
Dosificación estándar: 1 L de mezcla por cada 20 m3 de agua. Esta dosificación puede variar en función de las condiciones de agua de partida. 
OBSERVACIONES: 
Una vez mezclados los componentes A y B, se recomienda almacenar el envase bien cerrado, en un lugar ventilado, protegido de la luz y de temperaturas extremas por un máximo de 30 días. 
Los envases no podrán ser reutilizados.

PREVIO Saludine
HIGIENIZANTE TRATAMIENTO DE AGUAS
Desinfectante de agua de bebida a base de peróxido de hidrógeno, especialmente indicado para aguas de consumo animal en explotaciones ganaderas. De alto poder oxidante y desinfectante, permite eliminar el biofilm e impedir su reaparición controlando de esta forma la aparición de diarreas. 
Inhibidor de la incrustación. Controla la corrosión. Cumple la norma UNE 902 para tratamiento de aguas de consumo para peróxidos de hidrógeno. 
DOSIFICACIÓN: Diluir en agua una proporción de 30-50 ml /m3.
PREVIO Saludine es un producto para la higienización del agua de consumo y las superficies destinadas a estar en contacto con la misma, en base a peróxido de hidrógeno, ingrediente activo, de alto poder oxidante y desinfectante, sin el olor y otras desventajas del cloro, como la aparición de cloraminas, sustancias con alto efecto irritante. Su composición permite eliminar el biofilm e impedir su reaparición controlando de esta forma la aparición de diarreas. Inhibidor de la incrustación. Controla la corrosión. PREVIO Saludine tiene una extraordinaria eficacia bactericida, virucida y fungicida que garantiza una completa desinfección del agua de bebida. 
INDICACIONES, DOSIS RECOMENDADAS Y MODO DE EMPLEO: PREVIO Saludine está indicado para la higienización del agua en balsas, estanques o depósitos y limpieza de los sistemas de almacenamiento y distribución. 
HIGIENIZACIÓN EL AGUA: 
Aplicar el producto repartido en diferentes puntos de la masa de 
agua, en las siguientes cantidades: 
-Tratamiento de choque: 300 ml de PREVIO Saludine por cada metro cúbico de agua. 
-Tratamiento de mantenimiento: 30-50 ml de PREVIO Saludine por cada metro cúbico de agua. 
LIMPIEZA DE CONDUCCIONES: 
Emplear una solución del 1,5% al 3% de PREVIO Saludine. 
Aplicación: recirculación, dejando actuar durante 3 horas. 
El producto también puede ser aplicado en continuo mediante bomba dosificadora.


SANITAS Neozital
DESINFECTANTE OXIDANTE
Desinfectante de uso ganadero de amplio espectro que, gracias a su principio activo, el ácido peracético, proporciona una excelente capacidad de desinfección a concentraciones muy reducidas. Su fórmula es extremadamente potente, siendo capaz de eliminar bacterias, hongos y virus, pero a la vez completamente biodegradable, por lo que no genera residuos potencialmente peligrosos para el medio ambiente. Sus dosis de uso van del 0,3 al 1%. 
DOSIFICACIÓN: Rutinaria 
0,3% 
Normal 
0,5% 
Estricta 
1%
APLICACIONES: 
SANITAS® NEOZITAL® es un desinfectante de amplio espectro que, gracias a su principio activo, el ácido peracético, proporciona una excelente capacidad de desinfección a concentraciones muy reducidas. Su fórmula es extremadamente potente, siendo capaz de eliminar bacterias, hongos y virus, pero a la vez completamente biodegradable, por lo que no genera residuos potencialmente peligrosos para el medio ambiente. 
Es un producto de gran capacidad para la desinfección completa de todo tipo de locales e instalaciones de ganadería, avicultura, cunicultura, perreras, así como otros recintos en los que se alberguen animales. Asimismo, puede ser utilizado en la desinfección de utensilios, maquinaria y aparatos, tanto para clínicas veterinarias (áreas destinadas a animales, jaulas de hospitalización...) como para mataderos (área de estabulación de animales). 
INDICACIONES, DOSIS RECOMENDADAS Y MODO DE EMPLEO: SANITAS® NEOZITAL® se puede utilizar para la desinfección de todo tipo de instalaciones, bien sea mediante frotamiento, pulverización o nebulización, siendo igualmente eficaz de todas maneras. 
El producto se aplicará a la dosis recomendada, dejándolo secar en el lugar de aplicación, si esto no fuese posible, permitiendo su acción durante al menos 15 minutos. Los utensilios pueden ser desinfectados por inmersión en una solución al 0,5% durante un mínimo de media hora, y aclarado luego con abundante agua, si su tamaño lo permite, o bien ser desinfectado por pulverización. 
Aplicar en ausencia de animales. En la desinfección por nebulización, retirar a los animales del recinto, pudiendo ser reintroducidos cuando las paredes se hayan secado. 
SANITAS® NEOZITAL® se utiliza diluido en agua a concentraciones de 0,5% (1 parte en 200 de agua) a 1% (1 parte en 50 de agua) según la carga de suciedad presente. En aquellas zonas donde se ha confirmado la presencia de patógenos víricos, el producto puede ser utilizado a un 1%. Para vados sanitarios, medios de transporte y contenedores se recomienda la aplicación del producto al 0,5%. 
En nebulización aérea se debe utilizar el producto a la dosis de 0,5%. Como norma general, se recomienda la aplicación de 0,1-0,3 litros del producto diluido por cada metro cuadrado. 
USO EXCLUSIVO POR PERSONAL ESPECIALIZADO. 
N° DE REGISTRO: 01228-P

Zotal G Clásico 
Zotal D Clásico
DESINFECTANTE DESODORIZANTE
ZOTAL es un desinfectante y fungicida, de tipo fenólico, que presenta una gran eficacia allí donde existe materia orgánica abundante y condiciones de suciedad. 
DOSIFICACIÓN: Se emplea diluido en agua al 5%.
PROPIEDADES E INDICACIONES: 
ZOTAL en su registro ganadero, está indicado para la desinfección general de todo tipo de locales e instalaciones de uso ganadero, como establos, pocilgas, zahúrdas, gallineros, conejeras, perreras, boxes, etc. que puedan albergar bacterias y hongos. Asimismo, el registro doméstico puede ser utilizado en almacenes, cuarteles, patios, chalets, casas de campo y otras instalaciones de uso privado o público. Por su acción desinfectante y olor característico, elimina olores desagradables proporcionando un ambiente de higiene y limpieza. 
Debe aplicarse en zonas ventiladas y emulsionado (diluido en agua) al 5% para riegos y baldeos de superficies (paredes, suelos, etc.). Debe removerse la emulsión antes de su uso. En inodoros, urinarios, letrinas, etc., puede usarse puro (sin diluir). 
APLICACIONES: 
El preparado ZOTAL, desinfectante en forma de líquido emulsionable, debe su acción a su contenido en fenoles sintéticos, confiriéndole propiedades bactericidas, fungicidas, desodorizantes y frente a virus como el SARS Cov2. Para su utilización eficaz es necesario diluirlo en agua y aplicar por contacto. El resto de componentes favorecen la acción desinfectante y bactericida, ayudando a la limpieza y asegurando la humectación y penetración del producto, consiguiéndose con ello una mayor eficacia del mismo. 
MODO DE EMPLEO: 
ZOTAL se emplea emulsionado al 5% en agua (disuelto) en riegos y baldeos o por frotamiento (cepillo, escoba, etc...) remojo o pulverización. De esta forma, está recomendado para desinfectar aquellos lugares que puedan albergar microbios ejerciendo sus ingredientes activos una acción sinérgica y persistente. 
N° DE REGISTRO ZOTAL G CLÁSICO (antiguo Zotal Z): 11683-P N° DE REGISTRO ZOTAL D CLÁSICO (antiguo Zotal D): 
23-20/40-12008
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Consulta sobre productos ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        full_prompt = f"Eres un experto en Zotal. Usa este contexto: {contexto}. Pregunta: {prompt}"
        # Usamos stream=True para que la respuesta salga letra a letra (sensación de velocidad)
        response = model.generate_content(full_prompt, stream=True)
        
        def stream_data():
            for chunk in response:
                yield chunk.text
        
        full_response = st.write_stream(stream_data())
        st.session_state.messages.append({"role": "assistant", "content": full_response})