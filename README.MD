# Ejecutar

```
$env:FLASK_APP = "api-taller"
$env:FLASK_DEBUG = "1"
flask run
```

# Instalar Dependencias

`pip install -r requeriments.txt
`

# Crear Ambiente Virtual

```
python -m venv avtallerflask
.\avtallerflask\Scripts\activate
```

# Exportar Layer para Lambda

```
mkdir layers
cd layers
mkdir python
cd python
pip install -r ../../requeriments.txt -t .
cd ..
zip -r requests_layer.zip .
```
