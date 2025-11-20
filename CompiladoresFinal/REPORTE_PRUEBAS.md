# Reporte de Pruebas - Compilador ScriptLang

## Resumen de Ejecución

### Pruebas Válidas

| Test | Descripción | Estado |
|------|-------------|--------|
| test01_basico | escena inicio { | ✅ Pasó |
| test02_multiple | escena menu { | ✅ Pasó |
| test03_cadena | escena cap1 { | ✅ Pasó |
| test04_dialogos | escena intro { | ✅ Pasó |
| test05_loop | escena menu { | ✅ Pasó |
| test06_underscores | escena nivel_1 { | ✅ Pasó |
| test07_numeros | escena nivel1 { | ✅ Pasó |
| test08_comentarios | // Comentario | ✅ Pasó |
| test09_especiales | escena inicio { | ✅ Pasó |
| test10_complejo | escena entrada { | ✅ Pasó |

### Pruebas con Errores Esperados

| Test | Tipo de Error | Estado |
|------|---------------|--------|
| error01_inexistente | Semántico | ❌ No detectado |
| error02_duplicada | Semántico | ❌ No detectado |
| error03_sin_punto_coma | Semántico | ❌ No detectado |
| error04_sin_punto_coma2 | Semántico | ❌ No detectado |
| error05_sin_llave_abre | Semántico | ❌ No detectado |
| error06_sin_llave_cierra | Semántico | ❌ No detectado |
| error07_string_sin_cerrar | Semántico | ✅ Detectado |
| error08_typo | Semántico | ❌ No detectado |
| error09_sin_nombre | Semántico | ❌ No detectado |
| error10_sin_string | Semántico | ❌ No detectado |

---
*Generado automáticamente por run_tests.py*
