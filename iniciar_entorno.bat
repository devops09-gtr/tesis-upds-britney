@echo off
REM ========================================================
REM iniciar_entorno.bat - Instalador y lanzador para Windows
REM Proyecto de Tesis UPDS - Britney Arratia / Ing. Tarifa
REM ========================================================
title Tesis UPDS - Entorno de Deteccion de Anomalias Wi-Fi
color 0b

echo ========================================================
echo   TESIS DE GRADO - INGENIERIA EN REDES Y TELECOMUNICACIONES
echo   Evaluacion Experimental: Zeek + Isolation Forest
echo   Postulante: Britney Arratia  ^|  Tutor: Ing. Gonzalo Tarifa
echo ========================================================
echo.

REM 1. Verificar si Python esta instalado en Windows
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    py -3 --version >nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        color 0c
        echo [ERROR] No se detecto Python instalado en tu sistema Windows.
        echo Por favor descarga e instala Python desde: https://www.python.org/downloads/
        echo IMPORTANTE: Marca la casilla "Add Python to PATH" durante la instalacion.
        echo.
        pause
        exit /b 1
    ) else (
        set PY_CMD=py -3
    )
) else (
    set PY_CMD=python
)

echo [*] Python detectado correctamente.
echo.

REM 2. Crear entorno virtual si no existe
if not exist "venv\Scripts\activate.bat" (
    echo [*] Creando entorno virtual 'venv'...
    %PY_CMD% -m venv venv
    if %ERRORLEVEL% NEQ 0 (
        color 0c
        echo [ERROR] No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
    echo [+] Entorno virtual creado exitosamente.
    echo.
)

REM 3. Activar e instalar dependencias
echo [*] Verificando e instalando dependencias (Scikit-Learn, Pandas, Scapy)...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

echo.
echo ========================================================
echo   [OK] ENTORNO LISTO PARA TRABAJAR
echo ========================================================
echo   El entorno virtual esta activado.
echo   Para ejecutar la prueba piloto del pipeline, escribe:
echo       python src\test_pipeline.py
echo.
cmd /k
