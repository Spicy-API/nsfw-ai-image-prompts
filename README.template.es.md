<!--
  Este archivo lo genera scripts/build_readme.py a partir de README.template.es.md, data/*.json y data/i18n/es.json.
  Edita la plantilla o los datos y luego ejecuta: python3 scripts/build_readme.py
  Palabras clave: prompts nsfw, prompts de imagen ia nsfw, prompts para ia de adultos, generador de imágenes ia sin censura,
  prompts para imágenes sin censura, generador de prompts nsfw, prompts para editar imágenes con ia, editor de imágenes ia sin censura,
  imagen a prompt nsfw, prompts boudoir ia, prompts anime nsfw, prompts hentai ia, prompts qwen image, prompts seedream nsfw,
  prompts z-image, nsfw ai image prompts, nsfw prompts, uncensored ai image prompts, nsfw image prompt generator,
  nsfw image to prompt, nsfw ai image editor prompts, uncensored ai image generator
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <b>Español</b> · <a href="README.ru.md">Русский</a></p>

<h1 align="center">NSFW AI Image Prompts</h1>

<p align="center">
  <b>{{PROMPT_COUNT}} prompts de imagen con IA NSFW para copiar y pegar (incluidos {{EDIT_COUNT}} prompts de edición sin censura) y {{SHOWCASE_COUNT}} resultados reales junto a los prompts que los generaron, para Qwen Image 2.1, Seedream 5.0, Qwen Image 3.0 Pro, Z-Image Spicy y otros modelos de imagen sin censura.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/image%20prompts-{{PROMPT_COUNT}}-ff4d6d" alt="{{PROMPT_COUNT}} prompts de imagen">
  <img src="https://img.shields.io/badge/edit%20prompts-{{EDIT_COUNT}}-8b5cf6" alt="{{EDIT_COUNT}} prompts de edición">
  <img src="https://img.shields.io/badge/showcase-{{SHOWCASE_COUNT}}-10b981" alt="{{SHOWCASE_COUNT}} ejemplos reales">
  <img src="https://img.shields.io/badge/updated-{{READ_ON}}-blue" alt="Actualizado: {{READ_ON}}">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#mejores-modelos-para-imágenes-nsfw">Modelos</a> ·
  <a href="#ejemplos-reales-resultados-y-sus-prompts">Ejemplos</a> ·
  <a href="#los-prompts">Prompts</a> ·
  <a href="#de-imagen-nsfw-a-prompt">Imagen → prompt</a> ·
  <a href="#guía-rápida">Guía rápida</a> ·
  <a href="#ejecuta-un-prompt-en-60-segundos">Ejecutar</a> ·
  <a href="#preguntas-frecuentes">Preguntas frecuentes</a>
</p>

> **Solo para mayores de 18 años. Todos los personajes de este repositorio son adultos.** Los prompts indican una edad adulta y evitan a propósito las descripciones que sugieran juventud. Los prompts de edición son para imágenes tuyas, de adultos que den su consentimiento o de personajes ficticios que hayas generado. Nunca los uses para "desvestir" o sexualizar la foto de una persona real. Consulta las [Reglas](#reglas).

> Lo mantiene el equipo de [SpicyAPI](https://spicyapi.ai/es?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=disclosure-es), donde puedes ejecutar todos los prompts de aquí. Los prompts son texto plano y funcionan con cualquier modelo de imagen que los acepte.

---

## Por qué existe este repositorio

La mayoría de las listas de prompts NSFW son montones de etiquetas de la época de Stable Diffusion. Los modelos de imagen actuales (Qwen Image, Seedream, Z-Image) leen **frases completas**: quién aparece, qué lleva puesto, dónde está, la luz, el objetivo. Todos los prompts de aquí están escritos así e incluyen:

- el **modelo** para el que se escribió, elegido a partir de los resultados de prueba publicados por SpicyAPI,
- los **ajustes** exactos (relación de aspecto, resolución o tamaño, y el LoRA cuando se usa),
- el **costo de una imagen** con los precios actuales del catálogo,
- un **consejo** que explica por qué funciona.

Los consejos son recomendaciones prácticas, no resultados de benchmarks. Los [ejemplos reales](#ejemplos-reales-resultados-y-sus-prompts) son la parte de este repositorio con resultados reales.

## Contenido

- [Mejores modelos para imágenes NSFW](#mejores-modelos-para-imágenes-nsfw)
- [Ejemplos reales: resultados y sus prompts](#ejemplos-reales-resultados-y-sus-prompts)
- [Cómo escribir un prompt de imagen NSFW](#cómo-escribir-un-prompt-de-imagen-nsfw)
- [Los prompts](#los-prompts)
{{PROMPTS_TOC}}
- [De imagen NSFW a prompt](#de-imagen-nsfw-a-prompt)
- [Guía rápida](#guía-rápida)
- [Ejecuta un prompt en 60 segundos](#ejecuta-un-prompt-en-60-segundos)
- [Deja que un LLM escriba tus prompts](#deja-que-un-llm-escriba-tus-prompts)
- [De imagen a video](#de-imagen-a-video)
- [Preguntas frecuentes](#preguntas-frecuentes)
- [Reglas](#reglas)

---

## Mejores modelos para imágenes NSFW

Recomendaciones probadas, sacadas de las [clasificaciones públicas de SpicyAPI](https://spicyapi.ai/es/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es) (metodología v2.1, {{READ_ON}}):

- **[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)** (recomendado): Spicy Index 73, Freedom 96.3, desde $0.024 por imagen. Prompts largos (hasta 5000 caracteres), 15 relaciones de aspecto y edición a partir de 1 a 10 imágenes de referencia dentro de la misma familia.
- **[Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: #1 en el Spicy Index de imagen (80.5), Freedom 92. Hasta tres LoRAs; aquí se usa en todos los prompts de anime.
- **[MiniMax H3 Image LoRA](https://spicyapi.ai/es/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 100, generó todos los prompts de prueba explícitos; trae tu propio LoRA.
- **[Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 94.3, el acabado más "fotográfico" para looks editoriales y de campaña.
- **[Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 98, la mejor opción cuando la imagen lleva texto (portadas, pósteres).
- **🌶️ [Z-Image Spicy](https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=picks-es)**: Freedom 98.8 a $0.01235, el más barato para borradores y grandes volúmenes; anatomía más floja.
- No recomendados para NSFW: Krea 2 (Freedom 10), Wan 2.7 de texto a imagen (suaviza casi siempre los desnudos), FLUX.1 Dev LoRA (explícito 0/6). Prefect Pony XL todavía tiene muy pocos datos de prueba.

Todos los modelos de imagen sin censura, en el orden del catálogo (primero los más populares). ✅ Freedom 90+ · ◐ 70–89 · ⚠️ menos de 70 · 🧪 menos de 15 pruebas.

{{MODEL_TABLE}}

---

## Ejemplos reales: resultados y sus prompts

{{SHOWCASE_COUNT}} casos reales sacados de las páginas de los modelos y de la [biblioteca de prompts](https://spicyapi.ai/es/prompts?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=showcase-es) de SpicyAPI, cada uno generado con el modelo indicado. Cada caso muestra un resultado junto al prompt exacto que lo generó; los casos de edición también muestran la imagen de entrada. Los modelos aparecen de más a menos popular. Haz clic en una imagen para verla en tamaño completo.

{{SHOWCASE}}

Algunos resultados contienen desnudos; en esos casos aquí solo se muestra el prompt, y el resultado está en spicyapi.ai.

---

## Cómo escribir un prompt de imagen NSFW

```
[Shot type] of [an adult, age range, look] + [wardrobe or state] + [pose / action]
+ [setting] + [light: source and direction] + [lens / film look] + [mood or style]
```

Es decir: tipo de plano + un adulto (rango de edad, aspecto) + vestuario o estado + pose / acción + escenario + luz (fuente y dirección) + objetivo / acabado de película + ambiente o estilo. Los prompts se escriben en inglés.

| Sí | No |
|---|---|
| "Photorealistic boudoir portrait of a woman in her early 30s…" | "Hot girl, sexy, beautiful" |
| Nombra la fuente de luz y el lado: *window light from the left* | "Good lighting" |
| Nombra un objetivo o un acabado de película: *85mm, shallow depth of field, 35mm film* | "High quality, 8k, masterpiece" |
| Describe la tela: *black lace, ivory silk, sheer mesh, satin* | "Sexy outfit" |
| Una sola pose, con las manos haciendo algo: *hands on her knees*, *holding a coffee cup* | Poses complicadas con las dos manos en el encuadre |
| Indica una edad adulta siempre: *in her 30s*, *adult man in his 40s* | Descripciones que sugieran juventud |
| Pon entre comillas las palabras exactas de carteles y portadas | Esperar que el modelo invente un texto correcto |

Qwen Image y Seedream prefieren frases naturales a listas de etiquetas. Deja las palabras negativas fuera del prompt principal (escribir "no clothes" puede confundir a los modelos; describe lo que *sí* hay). Qwen Image 3.0 Pro acepta un campo `negative_prompt` si lo necesitas.

---

## Los prompts

Cada prompt indica el modelo para el que se escribió; la mayoría funcionan en cualquiera de los modelos recomendados. Cambia a Z-Image Spicy para borradores baratos y vuelve a Qwen Image 2.1 o Seedream 5.0 Pro para las versiones finales.

{{PROMPTS}}

---

## De imagen NSFW a prompt

¿Quieres recrear el aspecto de una imagen de referencia? Descríbela en este orden y ya tienes un prompt:

1. **Plano:** retrato, cuerpo entero, primer plano, cenital, POV, plano general.
2. **Sujeto:** adulto, rango de edad, complexión, pelo, expresión. Nunca describas a una persona real identificable.
3. **Vestuario:** prenda, tela, color, cómo se lleva (abierta, caída del hombro).
4. **Pose:** dónde están las manos, dónde carga el peso, adónde mira.
5. **Escenario:** habitación, objetos, hora del día.
6. **Luz:** fuente, dirección, temperatura de color, dura o suave.
7. **Cámara:** distancia focal, profundidad de campo, película o aspecto de móvil.
8. **Estilo:** fotorrealista, editorial, cine negro, anime (y entonces añade el LoRA), pintura al óleo.

O pega tu descripción en el [redactor de prompts con LLM](#deja-que-un-llm-escriba-tus-prompts) de más abajo. Para conservar exactamente un personaje o un conjunto, sáltate el prompt y usa un [prompt de edición](#prompts-para-editar-imágenes-sin-censura) con la propia imagen como referencia (solo con imágenes tuyas, de adultos que den su consentimiento o de personajes generados).

---

## Guía rápida

**Objetivos y cámara**

| Escribe | Efecto |
|---|---|
| `85mm, shallow depth of field` | Retrato favorecedor, fondo desenfocado |
| `35mm film` | Natural, documental, algo de grano |
| `50mm` | Neutro, perspectiva fiel al ojo |
| `macro` | Detalle extremo: encaje, joyas, piel |
| `wide shot, 24mm` | Entorno, figura pequeña en el encuadre |
| `overhead / top-down` | Gráfico, plano, ideal para camas y bañeras |
| `POV` | Primera persona, cercano |
| `smartphone photo, slight grain` | Contenido de creador creíble |

**Luz**

| Ambiente | Escribe |
|---|---|
| Suave, romántico | window light, sheer curtains, golden hour |
| Dramático | single hard key light, deep shadows, chiaroscuro |
| Noir | slatted light from blinds, black and white |
| Cálido, íntimo | candlelight, firelight, tungsten lamp |
| Glamour | softbox, beauty dish, high key |
| Neón | magenta and cyan neon, wet reflections |
| Contraluz | rim light, silhouette, glowing edges |

**Looks y estilos** (escríbelos en inglés): editorial fashion photography · boudoir photography · fine-art nude photography · Kodachrome / Portra 400 film · black and white · film noir · 1950s pin-up · oil painting · watercolor anime (LoRA) · storybook anime illustration (LoRA) · cyberpunk.

**Realismo**: natural skin texture · visible pores · slight film grain · imperfect lived-in room · mixed practical light. Evita "flawless", "perfect skin" y "8k", que empujan hacia un aspecto de plástico.

---

## Ejecuta un prompt en 60 segundos

**Sin código:** pega cualquier prompt en el [generador de imágenes con IA sin censura de SpicyAPI Studio](https://spicyapi.ai/es/create/uncensored-ai-image-generator?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=run-es) y revisa el precio antes de generar.

**cURL:**

```bash
export SPICY_API_KEY="sk-spicy-..."   # https://spicyapi.ai/es/console

curl -s https://api.spicyapi.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $SPICY_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "model": "alibaba/qwen-image-2.1/text-to-image",
    "input": {
      "prompt": "Photorealistic boudoir portrait of a woman in her early 30s in black lace lingerie, soft window light from the left, 85mm, natural skin texture",
      "aspect_ratio": "2:3",
      "resolution": "1k"
    }
  }'

# Consulta hasta que data.state sea "succeeded" y luego descarga data.output.assets[0].url
curl -s "https://api.spicyapi.ai/api/v1/jobs/recordInfo?taskId=TASK_ID" \
  -H "Authorization: Bearer $SPICY_API_KEY"
```

**Anime con un LoRA** (Qwen Image 2.1 LoRA): añade `"loras": [{"path": "https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora/resolve/main/qwen_image_2512_storybook_anime_lora.safetensors", "scale": 1}]` a `input` y usa `"model": "alibaba/qwen-image-2.1-lora/text-to-image"`.

**Edición** (Qwen Image 2.1 Edit): usa `"model": "alibaba/qwen-image-2.1/edit"` con `"image_urls": ["https://.../your-image.jpg"]` y la instrucción de edición como `prompt`.

¿Prefieres pedírselo a un agente? Instala **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.es.md)** en Claude Code, Cursor o Codex y di: *"genera el prompt B01 de nsfw-ai-image-prompts con Qwen Image 2.1"*.

---

## Deja que un LLM escriba tus prompts

Pega este prompt de sistema en cualquier modelo de chat (en SpicyAPI, [Grok 4.7](https://spicyapi.ai/es/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=llm-es) y [Grok 4.3](https://spicyapi.ai/es/models/grok-4-3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=llm-es) obtuvieron las puntuaciones más altas en las pruebas de escritura para adultos):

```text
You write prompts for adult text-to-image models. Every character is an adult aged 21 or older; never use
descriptors that suggest youth and never depict real, identifiable people.
Given a short idea (or a description of a reference image), return ONE prompt of 40–90 words in this order:
shot type, subject (with adult age), wardrobe and fabric, pose and hands, setting, light source and direction,
lens or film look, style. Use natural sentences, not tag lists. Put any on-image text in quotes.
```

---

## De imagen a video

Cualquier imagen fija de aquí puede convertirse en un clip. Úsala como primer fotograma en un modelo de imagen a video; el repositorio **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.es.md)** tiene 116 prompts de movimiento escritos para eso. En las pruebas de SpicyAPI, el mejor modelo de video NSFW para todo es [Wan 3.0](https://spicyapi.ai/es/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=i2v-es) (Freedom 96, $0.45 por clip de 5 segundos a 720p).

---

## Preguntas frecuentes

### ¿Cuál es el mejor modelo de IA para imágenes NSFW?
En las pruebas publicadas por SpicyAPI: **Qwen Image 2.1** (Spicy Index 73, Freedom 96.3, desde $0.024) para la mayoría de los casos, **Qwen Image 2.1 LoRA** (#1 en el índice de imagen) y **MiniMax H3 Image LoRA** (Freedom 100) para tus propios estilos, **Seedream 5.0 Pro** para un acabado fotográfico, **Qwen Image 3.0 Pro** cuando la imagen lleva texto y **Z-Image Spicy** para los borradores más baratos. Consulta [Mejores modelos para imágenes NSFW](#mejores-modelos-para-imágenes-nsfw).

### ¿Cómo se escribe un buen prompt de imagen NSFW con IA?
Escribe frases completas en este orden: plano, sujeto adulto con su edad, vestuario y tela, pose, escenario, luz, objetivo, estilo. Nombra la fuente de luz y un objetivo; olvídate de "8k masterpiece". Consulta [Cómo escribir un prompt de imagen NSFW](#cómo-escribir-un-prompt-de-imagen-nsfw).

### ¿Puedo editar una foto con un editor de imágenes con IA sin censura?
Sí, con Qwen Image 2.1 Edit: envía de 1 a 10 imágenes de referencia y una instrucción ("change the outfit to…", "relight to candlelight…"). Edita solo imágenes tuyas, de adultos que den su consentimiento o de personajes generados; está prohibido "desvestir" fotos de personas reales. Consulta los [prompts de edición](#prompts-para-editar-imágenes-sin-censura).

### ¿Cómo se hacen imágenes de anime o de estilo hentai con IA?
Usa Qwen Image 2.1 LoRA con un LoRA de anime abierto (los LoRAs storybook-anime y watercolor-anime que usa SpicyAPI en sus propios ejemplos), empieza el prompt con la frase de estilo del LoRA y diseña todos los personajes como adultos. Consulta [Anime e ilustración](#anime-e-ilustración-qwen-image-21-lora).

### ¿Estos prompts funcionan en Stable Diffusion, ComfyUI o Midjourney?
Los prompts en forma de frases funcionan en cualquier modelo moderno, incluidos Qwen-Image y Z-Image autoalojados en ComfyUI. Los checkpoints SDXL/Pony prefieren listas de etiquetas, así que allí conviértelos en etiquetas más cortas. Midjourney no permite contenido para adultos.

### ¿Cuánto cuesta una imagen NSFW con IA?
En SpicyAPI ({{READ_ON}}): Z-Image Spicy $0.01235, Qwen Image 2.1 $0.024 (1k), Qwen Image 2.1 LoRA $0.03, Seedream 5.0 Pro $0.036, Qwen Image 3.0 Pro $0.04, Qwen Image 2.1 Edit $0.036. Sin suscripción; las imágenes fallidas se reembolsan.

### ¿Hay algún generador de prompts de imagen NSFW?
Usa el [prompt de sistema para LLM](#deja-que-un-llm-escriba-tus-prompts) con cualquier modelo de chat, o describe una imagen de referencia con la [lista de imagen a prompt](#de-imagen-nsfw-a-prompt).

---

## Reglas

- **Solo adultos.** Nada de contenido sexual que involucre a menores de 18 años o a quien parezca menor de 18, en ningún estilo, incluido el anime. Una edad declarada no cambia el aspecto de un personaje.
- **Nada de personas reales sin consentimiento documentado.** Nada de deepfakes sexuales, de cambios de cara de personas reales en contenido sexual ni de fotos reales "desvestidas". Las figuras públicas no son una excepción.
- **Cumple la ley** del lugar donde vives y donde vive tu público, y las normas de las plataformas donde publiques.
- Normas completas de SpicyAPI: [Política de contenidos](https://spicyapi.ai/es/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=rules-es) · [Política de uso aceptable](https://spicyapi.ai/es/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts&utm_content=rules-es).

## Relacionados

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.es.md)**: lista, ordenada según pruebas, de herramientas, APIs y modelos de IA sin censura para imagen, video y texto.
- **[nsfw-ai-video-prompts](https://github.com/Spicy-API/nsfw-ai-video-prompts/blob/main/README.es.md)**: prompts de video NSFW, prompts para el primer fotograma y 128 casos con resultados reales.
- **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.es.md)**: genera imágenes y videos NSFW desde Claude Code, Cursor, Codex y otros agentes.
- Datos legibles por máquina: [`data/image-prompts.json`](data/image-prompts.json), [`data/showcase.json`](data/showcase.json).

## Cómo contribuir

Se aceptan pull requests con prompts. Añádelos a `data/image-prompts.json` (solo personajes adultos, modelo + ajustes + consejo) y luego ejecuta `python3 scripts/build_readme.py`. Las comprobaciones están en `scripts/check_prompts.py`.

## Licencia

Prompts y documentación: [CC0 1.0](LICENSE). Las imágenes de los ejemplos están alojadas en SpicyAPI y se enlazan, no se redistribuyen.

<p align="center"><sub>⭐ Dale una estrella al repositorio si algún prompt te ha ahorrado unos cuantos intentos.</sub></p>
